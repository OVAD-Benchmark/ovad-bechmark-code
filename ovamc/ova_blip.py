import os
import sys

sys.path.insert(0, os.getcwd())
from BLIP.models.blip import load_checkpoint
import yaml
import json
import torch
import GPUtil
import argparse
import itertools
import numpy as np
import dill as pickle
import torch.nn.functional as F
import torchvision.transforms as transforms

from ovamc.data_loader import OVAD_Boxes
from ovamc.misc import object_attribute_templates, ovad_validate

import ipdb


def get_arguments():
    parser = argparse.ArgumentParser(description="Blip evaluation")
    parser.add_argument(
        "--dataset_name",
        type=str,
        default="ovad2000",
        help="dataset name",
    )
    parser.add_argument(
        "--ann_file",
        type=str,
        default="datasets/ovad/ovad2000.json",
        help="annotation file with images and objects for attribute annotation",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="output/OVAD_Benchmark2000/multimodal_ovac/blip/",
        help="dir where models are",
    )
    parser.add_argument(
        "--dir_data",
        type=str,
        default="datasets/ovad_box_instances/2000_img",
        help="image data dir",
    )
    parser.add_argument(
        "--model_arch",
        type=str,
        default="base",
        help="architecture name",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="all",
        help="prompt",
    )
    parser.add_argument(
        "--average_syn",
        action="store_true",
    )
    parser.add_argument(
        "--object_word",
        action="store_true",
    )
    parser.add_argument(
        "-bs",
        "--batch_size",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-is",
        "--image_size",
        type=int,
        default=-1,
    )

    return parser.parse_args()


model_versions = {
    "base": "ovamc/BLIP/weights/model_base.pth",
    "base14M": "ovamc/BLIP/weights/model_base_14M.pth",
    "baseCapfilt": "ovamc/BLIP/weights/model_base_capfilt_large.pth",
    "baseRetrieval": "ovamc/BLIP/weights/model_base_retrieval_coco.pth",
    "baseVQA": "ovamc/BLIP/weights/model_vqa.pth",
    "baseRetrievalFlicker": "ovamc/BLIP/weights/model_base_retrieval_flickr.pth",
}


def encode_blip(text_list, model, device):
    if isinstance(text_list[0], list):
        # it is a list of list of strings
        avg_synonyms = True
        sentences = list(itertools.chain.from_iterable(text_list))
        print("flattened_sentences", len(sentences))
    elif isinstance(text_list[0], str):
        avg_synonyms = False
        sentences = text_list
    text = model.tokenizer(
        sentences,
        padding="max_length",
        truncation=True,
        max_length=30,
        return_tensors="pt",
    ).to(device)

    with torch.no_grad():
        text_output = model.text_encoder(
            text.input_ids,
            attention_mask=text.attention_mask,
            return_dict=True,
            mode="text",
        )
        text_features = F.normalize(
            model.text_proj(text_output.last_hidden_state[:, 0, :]), dim=-1
        )

    print("text_features.shape", text_features.shape)
    if avg_synonyms:
        synonyms_per_cat = [len(x) for x in text_list]
        text_features = text_features.split(synonyms_per_cat, dim=0)
        text_features = [x.mean(dim=0) for x in text_features]
        text_features = torch.stack(text_features, dim=0)
        print("after stack", text_features.shape)

    return text_features


def main(args):
    object_word = "object" if args.object_word else ""
    use_prompts = ["a", "the", "none"]
    if args.prompt in use_prompts or args.prompt == "photo":
        use_prompts = [args.prompt]

    # load annotations
    annotations = json.load(open(args.ann_file, "r"))
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Loading Blip")
    if args.model_arch == "baseRetrieval":
        from BLIP.models.blip_itm import blip_itm

        config = yaml.load(
            open("ovamc/BLIP/configs/retrieval_coco.yaml", "r"), Loader=yaml.Loader
        )
        med_config = "ovamc/BLIP/configs/med_config.json"
        model = blip_itm(
            med_config=med_config,
            pretrained=model_versions[args.model_arch],
            image_size=config["image_size"],
            vit="base",
        )
    elif args.model_arch == "baseRetrievalFlicker":
        from BLIP.models.blip_itm import blip_itm

        config = yaml.load(
            open("ovamc/BLIP/configs/retrieval_flickr.yaml", "r"), Loader=yaml.Loader
        )
        med_config = "ovamc/BLIP/configs/med_config.json"
        model = blip_itm(
            med_config=med_config,
            pretrained=model_versions[args.model_arch],
            image_size=config["image_size"],
            vit="base",
        )
    else:
        config = yaml.load(
            open("ovamc/BLIP/configs/pretrain.yaml", "r"), Loader=yaml.Loader
        )
        med_config = "ovamc/BLIP/configs/bert_config.json"
        if args.image_size != -1 and args.image_size != config["image_size"]:
            image_size = args.image_size
            args.output_dir += "_imgsz{}".format(image_size)

            from BLIP.models.blip_itm import blip_itm

            ipdb.set_trace()
            model = blip_itm(
                med_config=med_config,
                pretrained="",
                image_size=config["image_size"],
                vit="base",
            )
            weights = model_versions[args.model_arch]
            model, msg = load_checkpoint(model, weights)
            print(msg)
        else:
            image_size = config["image_size"]

            from BLIP.models.blip_pretrain import blip_pretrain as blip

            model = blip(
                med_config=med_config,
                image_size=image_size,
                vit=config["vit"],
                vit_grad_ckpt=config["vit_grad_ckpt"],
                vit_ckpt_layer=config["vit_ckpt_layer"],
                queue_size=config["queue_size"],
            )
            weights = model_versions[args.model_arch]
            model, msg = load_checkpoint(model, weights)
            print(msg)
            # checkpoint = torch.load(weights)
            # model.load_state_dict(checkpoint["model"], strict=False)

    model = model.to(device)
    model.eval()

    # Make transform
    channel_stats = dict(
        mean=[0.48145466, 0.4578275, 0.40821073],
        std=[0.26862954, 0.26130258, 0.27577711],
    )

    transform = transforms.Compose(
        [
            transforms.Resize(
                size=(config["image_size"], config["image_size"]), interpolation=2
            ),
            transforms.ToTensor(),
            transforms.Normalize(**channel_stats),
        ]
    )

    dataset = OVAD_Boxes(root=args.dir_data, transform=transform)
    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=4,
        pin_memory=False,
    )

    # make dir to save results and embeddings
    args.output_dir += (
        "_{}".format(args.model_arch.replace("/", ""))
        + ("_avsyn" if args.average_syn else "")
        + "_prompt-{}".format(args.prompt)
        + "{}".format(object_word)
    )
    os.makedirs(args.output_dir, exist_ok=True)
    att_emb_path = os.path.join(
        args.output_dir, "att_blip_{}.pkl".format(args.model_arch.replace("/", ""))
    )

    if os.path.isfile(att_emb_path):
        print("Loading attribute text embeddings", att_emb_path)
        att_emb = pickle.load(open(att_emb_path, "rb"))
        text_features = torch.Tensor(att_emb["text_features"]).to(device)
        len_synonyms = att_emb["len_synonyms"]
    else:
        print("Calculating attribute text embeddings")
        # unconditional embeddings
        all_att_templates = []
        for att_dict in annotations["attributes"]:
            att_w_type = att_dict["name"]
            att_type, att_list = att_w_type.split(":")
            is_has = att_dict["is_has_att"]
            dobj_name = (
                att_type.replace(" tone", "")
                # So far only for tone worked to remove the word
                # .replace(" color", "")
                # .replace(" pattern", "")
                # .replace(" expression", "")
                # .replace(" type", "")
                # .replace(" length", "")
            )

            # extend the maturity to include other words
            if att_list == "young/baby":
                att_list += "/kid/kids/child/toddler/boy/girl"
            elif att_list == "adult/old/aged":
                att_list += "/teen/elder"
            att_templates = []
            for syn in att_list.split("/"):
                for prompt in use_prompts:
                    for template in object_attribute_templates[is_has][prompt]:
                        if is_has == "has":
                            att_templates.append(
                                template.format(
                                    attr=syn, dobj=dobj_name, noun=object_word
                                ).strip()
                            )
                        elif is_has == "is":
                            att_templates.append(
                                template.format(attr=syn, noun=object_word).strip()
                            )
            all_att_templates.append(att_templates)

        att_templates_syn = all_att_templates
        len_synonyms = [len(att_synonyms) for att_synonyms in all_att_templates]
        att_ids = [
            [att_dict["id"]] * len(att_synonyms)
            for att_dict, att_synonyms in zip(
                annotations["attributes"], att_templates_syn
            )
        ]
        att_ids = list(itertools.chain.from_iterable(att_ids))
        all_att_templates = list(itertools.chain.from_iterable(all_att_templates))

        text_features = encode_blip(all_att_templates, model, device)

        att_emb = {
            "att_cls": [att["name"] for att in annotations["attributes"]],
            "len_synonyms": len_synonyms,
            "att_ids": att_ids,
            "all_att_templates": all_att_templates,
            "text_features": text_features.cpu().numpy(),
        }

        print("Saving attribute text embeddings", att_emb_path)
        with open(att_emb_path, "wb") as t:
            pickle.dump(att_emb, t)

    pred_vectors = []
    label_vectors = []
    indx_max_syn = []
    with torch.no_grad():
        for i, (images, labels) in enumerate(data_loader):
            att_label, obj_label = torch.stack(labels[0], axis=1), labels[1]
            label_vectors.append(att_label.cpu().numpy())

            # predict
            images = images.to(device)
            image_embeds = model.visual_encoder(images)
            image_atts = torch.ones(image_embeds.size()[:-1], dtype=torch.long).to(
                device
            )
            image_features = F.normalize(
                model.vision_proj(image_embeds[:, 0, :]), dim=-1
            )

            logits = image_features @ text_features.T

            # split into synonyms
            x_attrs_syn = logits.split(len_synonyms, dim=1)
            # take arg max
            x_attrs_maxsyn = []
            x_attrs_idxsyn = []
            for x_syn in x_attrs_syn:
                if args.average_syn:
                    xmax_val = x_syn.mean(axis=1)
                    xmax_idx = torch.zeros((1, args.batch_size))
                else:
                    xmax_val, xmax_idx = x_syn.max(axis=1)
                x_attrs_maxsyn.append(xmax_val)
                x_attrs_idxsyn.append(xmax_idx)
            idx_attrs = torch.stack(x_attrs_idxsyn, axis=1)
            x_attrs = torch.stack(x_attrs_maxsyn, axis=1)

            pred_vectors.append(x_attrs.cpu().numpy())
            indx_max_syn.append(idx_attrs.cpu().numpy())

            if i % 50 == 0:
                print("Processed {} out of {}".format(i, len(data_loader)), end="\r")
                if 0 < i < 300:
                    GPUtil.showUtilization(all=True)

    pred_vectors = np.concatenate(pred_vectors, axis=0)
    label_vectors = np.concatenate(label_vectors, axis=0)
    indx_max_syn = np.concatenate(indx_max_syn, axis=0)
    ovad_validate(
        annotations["attributes"],
        pred_vectors,
        label_vectors,
        args.output_dir,
        args.dataset_name,
    )


if __name__ == "__main__":
    args = get_arguments()
    main(args)
