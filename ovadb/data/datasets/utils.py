from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES

categories_base = [
    {"id": 1, "name": "person"},
    {"id": 2, "name": "bicycle"},
    {"id": 3, "name": "car"},
    {"id": 4, "name": "motorcycle"},
    {"id": 7, "name": "train"},
    {"id": 8, "name": "truck"},
    {"id": 9, "name": "boat"},
    {"id": 15, "name": "bench"},
    {"id": 16, "name": "bird"},
    {"id": 19, "name": "horse"},
    {"id": 20, "name": "sheep"},
    {"id": 23, "name": "bear"},
    {"id": 24, "name": "zebra"},
    {"id": 25, "name": "giraffe"},
    {"id": 27, "name": "backpack"},
    {"id": 31, "name": "handbag"},
    {"id": 33, "name": "suitcase"},
    {"id": 34, "name": "frisbee"},
    {"id": 35, "name": "skis"},
    {"id": 38, "name": "kite"},
    {"id": 42, "name": "surfboard"},
    {"id": 44, "name": "bottle"},
    {"id": 48, "name": "fork"},
    {"id": 50, "name": "spoon"},
    {"id": 51, "name": "bowl"},
    {"id": 52, "name": "banana"},
    {"id": 53, "name": "apple"},
    {"id": 54, "name": "sandwich"},
    {"id": 55, "name": "orange"},
    {"id": 56, "name": "broccoli"},
    {"id": 57, "name": "carrot"},
    {"id": 59, "name": "pizza"},
    {"id": 60, "name": "donut"},
    {"id": 62, "name": "chair"},
    {"id": 65, "name": "bed"},
    {"id": 70, "name": "toilet"},
    {"id": 72, "name": "tv"},
    {"id": 73, "name": "laptop"},
    {"id": 74, "name": "mouse"},
    {"id": 75, "name": "remote"},
    {"id": 78, "name": "microwave"},
    {"id": 79, "name": "oven"},
    {"id": 80, "name": "toaster"},
    {"id": 82, "name": "refrigerator"},
    {"id": 84, "name": "book"},
    {"id": 85, "name": "clock"},
    {"id": 86, "name": "vase"},
    {"id": 90, "name": "toothbrush"},
]
categories_base_names = [x["name"] for x in categories_base]

categories_novel17 = [
    {"id": 5, "name": "airplane"},
    {"id": 6, "name": "bus"},
    {"id": 17, "name": "cat"},
    {"id": 18, "name": "dog"},
    {"id": 21, "name": "cow"},
    {"id": 22, "name": "elephant"},
    {"id": 28, "name": "umbrella"},
    {"id": 32, "name": "tie"},
    {"id": 36, "name": "snowboard"},
    {"id": 41, "name": "skateboard"},
    {"id": 47, "name": "cup"},
    {"id": 49, "name": "knife"},
    {"id": 61, "name": "cake"},
    {"id": 63, "name": "couch"},
    {"id": 76, "name": "keyboard"},
    {"id": 81, "name": "sink"},
    {"id": 87, "name": "scissors"},
]
categories_novel17_names = [x["name"] for x in categories_novel17]

categories_novel32 = [
    {"id": x["id"], "name": x["name"]}
    for x in COCO_CATEGORIES
    if x["name"] not in categories_base_names
]
categories_novel32_names = [x["name"] for x in categories_novel32]

# taken from https://github.com/lvis-dataset/lvis-api/blob/master/data/coco_to_synset.json
coco_to_synset = {
    "bench": {
        "coco_cat_id": 15,
        "meaning": "a long seat for more than one person",
        "synset": "bench.n.01",
    },
    "baseball bat": {
        "coco_cat_id": 39,
        "meaning": "an implement used in baseball by the batter",
        "synset": "baseball_bat.n.01",
    },
    "kite": {
        "coco_cat_id": 38,
        "meaning": "plaything consisting of a light frame covered with tissue paper; flown in wind at end of a string",
        "synset": "kite.n.03",
    },
    "orange": {
        "coco_cat_id": 55,
        "meaning": "orange (FRUIT of an orange tree)",
        "synset": "orange.n.01",
    },
    "boat": {
        "coco_cat_id": 9,
        "meaning": "a vessel for travel on water",
        "synset": "boat.n.01",
    },
    "carrot": {
        "coco_cat_id": 57,
        "meaning": "deep orange edible root of the cultivated carrot plant",
        "synset": "carrot.n.01",
    },
    "bicycle": {
        "coco_cat_id": 2,
        "meaning": "a wheeled vehicle that has two wheels and is moved by foot pedals",
        "synset": "bicycle.n.01",
    },
    "book": {
        "coco_cat_id": 84,
        "meaning": "a written work or composition that has been published",
        "synset": "book.n.01",
    },
    "toothbrush": {
        "coco_cat_id": 90,
        "meaning": "small brush; has long handle; used to clean teeth",
        "synset": "toothbrush.n.01",
    },
    "tie": {
        "coco_cat_id": 32,
        "meaning": "neckwear consisting of a long narrow piece of material worn under a collar and tied in knot at the front",
        "synset": "necktie.n.01",
    },
    "sandwich": {
        "coco_cat_id": 54,
        "meaning": "two (or more) slices of bread with a filling between them",
        "synset": "sandwich.n.01",
    },
    "toilet": {
        "coco_cat_id": 70,
        "meaning": "a plumbing fixture for defecation and urination",
        "synset": "toilet.n.02",
    },
    "stop sign": {
        "coco_cat_id": 13,
        "meaning": "a traffic sign to notify drivers that they must come to a complete stop",
        "synset": "stop_sign.n.01",
    },
    "wine glass": {
        "coco_cat_id": 46,
        "meaning": "a glass that has a stem and in which wine is served",
        "synset": "wineglass.n.01",
    },
    "clock": {
        "coco_cat_id": 85,
        "meaning": "a timepiece that shows the time of day",
        "synset": "clock.n.01",
    },
    "bear": {
        "coco_cat_id": 23,
        "meaning": "large carnivorous or omnivorous mammals with shaggy coats and claws",
        "synset": "bear.n.01",
    },
    "vase": {
        "coco_cat_id": 86,
        "meaning": "an open jar of glass or porcelain used as an ornament or to hold flowers",
        "synset": "vase.n.01",
    },
    "microwave": {
        "coco_cat_id": 78,
        "meaning": "kitchen appliance that cooks food by passing an electromagnetic wave through it",
        "synset": "microwave.n.02",
    },
    "oven": {
        "coco_cat_id": 79,
        "meaning": "kitchen appliance used for baking or roasting",
        "synset": "oven.n.01",
    },
    "cake": {
        "coco_cat_id": 61,
        "meaning": "baked goods made from or based on a mixture of flour, sugar, eggs, and fat",
        "synset": "cake.n.03",
    },
    "apple": {
        "coco_cat_id": 53,
        "meaning": "fruit with red or yellow or green skin and sweet to tart crisp whitish flesh",
        "synset": "apple.n.01",
    },
    "bed": {
        "coco_cat_id": 65,
        "meaning": "a piece of furniture that provides a place to sleep",
        "synset": "bed.n.01",
    },
    "skis": {
        "coco_cat_id": 35,
        "meaning": "sports equipment for skiing on snow",
        "synset": "ski.n.01",
    },
    "dining table": {
        "coco_cat_id": 67,
        "meaning": "a table at which meals are served",
        "synset": "dining_table.n.01",
    },
    "remote": {
        "coco_cat_id": 75,
        "meaning": "a device that can be used to control a machine or apparatus from a distance",
        "synset": "remote_control.n.01",
    },
    "bird": {
        "coco_cat_id": 16,
        "meaning": "animal characterized by feathers and wings",
        "synset": "bird.n.01",
    },
    "laptop": {
        "coco_cat_id": 73,
        "meaning": "a portable computer small enough to use in your lap",
        "synset": "laptop.n.01",
    },
    "train": {
        "coco_cat_id": 7,
        "meaning": "public or private transport provided by a line of railway cars coupled together and drawn by a locomotive",
        "synset": "train.n.01",
    },
    "mouse": {
        "coco_cat_id": 74,
        "meaning": "a computer input device that controls an on-screen pointer",
        "synset": "mouse.n.04",
    },
    "pizza": {
        "coco_cat_id": 59,
        "meaning": "Italian open pie made of thin bread dough spread with a spiced mixture of e.g. tomato sauce and cheese",
        "synset": "pizza.n.01",
    },
    "toaster": {
        "coco_cat_id": 80,
        "meaning": "a kitchen appliance (usually electric) for toasting bread",
        "synset": "toaster.n.02",
    },
    "cell phone": {
        "coco_cat_id": 77,
        "meaning": "a hand-held mobile telephone",
        "synset": "cellular_telephone.n.01",
    },
    "person": {"coco_cat_id": 1, "meaning": "a human being", "synset": "person.n.01"},
    "sports ball": {
        "coco_cat_id": 37,
        "meaning": "a spherical object used as a plaything",
        "synset": "ball.n.06",
    },
    "fire hydrant": {
        "coco_cat_id": 11,
        "meaning": "an upright hydrant for drawing water to use in fighting a fire",
        "synset": "fireplug.n.01",
    },
    "umbrella": {
        "coco_cat_id": 28,
        "meaning": "a lightweight handheld collapsible canopy",
        "synset": "umbrella.n.01",
    },
    "truck": {
        "coco_cat_id": 8,
        "meaning": "an automotive vehicle suitable for hauling",
        "synset": "truck.n.01",
    },
    "knife": {
        "coco_cat_id": 49,
        "meaning": "tool with a blade and point used as a cutting instrument",
        "synset": "knife.n.01",
    },
    "baseball glove": {
        "coco_cat_id": 40,
        "meaning": "the handwear used by fielders in playing baseball",
        "synset": "baseball_glove.n.01",
    },
    "giraffe": {
        "coco_cat_id": 25,
        "meaning": "tall animal having a spotted coat and small horns and very long neck and legs",
        "synset": "giraffe.n.01",
    },
    "airplane": {
        "coco_cat_id": 5,
        "meaning": "an aircraft that has a fixed wing and is powered by propellers or jets",
        "synset": "airplane.n.01",
    },
    "parking meter": {
        "coco_cat_id": 14,
        "meaning": "a coin-operated timer located next to a parking space",
        "synset": "parking_meter.n.01",
    },
    "couch": {
        "coco_cat_id": 63,
        "meaning": "an upholstered seat for more than one person",
        "synset": "sofa.n.01",
    },
    "tennis racket": {
        "coco_cat_id": 43,
        "meaning": "a racket used to play tennis",
        "synset": "tennis_racket.n.01",
    },
    "backpack": {
        "coco_cat_id": 27,
        "meaning": "a bag carried by a strap on your back or shoulder",
        "synset": "backpack.n.01",
    },
    "hot dog": {
        "coco_cat_id": 58,
        "meaning": "a smooth-textured sausage, usually smoked, often served on a bread roll",
        "synset": "frank.n.02",
    },
    "banana": {
        "coco_cat_id": 52,
        "meaning": "elongated crescent-shaped yellow fruit with soft sweet flesh",
        "synset": "banana.n.02",
    },
    "bowl": {
        "coco_cat_id": 51,
        "meaning": "a dish that is round and open at the top for serving foods",
        "synset": "bowl.n.03",
    },
    "skateboard": {
        "coco_cat_id": 41,
        "meaning": "a board with wheels that is ridden in a standing or crouching position and propelled by foot",
        "synset": "skateboard.n.01",
    },
    "bottle": {
        "coco_cat_id": 44,
        "meaning": "a glass or plastic vessel used for storing drinks or other liquids",
        "synset": "bottle.n.01",
    },
    "dog": {
        "coco_cat_id": 18,
        "meaning": "a common domesticated dog",
        "synset": "dog.n.01",
    },
    "frisbee": {
        "coco_cat_id": 34,
        "meaning": "a light, plastic disk propelled with a flip of the wrist for recreation or competition",
        "synset": "frisbee.n.01",
    },
    "broccoli": {
        "coco_cat_id": 56,
        "meaning": "plant with dense clusters of tight green flower buds",
        "synset": "broccoli.n.01",
    },
    "elephant": {
        "coco_cat_id": 22,
        "meaning": "a common elephant",
        "synset": "elephant.n.01",
    },
    "car": {
        "coco_cat_id": 3,
        "meaning": "a motor vehicle with four wheels",
        "synset": "car.n.01",
    },
    "donut": {
        "coco_cat_id": 60,
        "meaning": "a small ring-shaped friedcake",
        "synset": "doughnut.n.02",
    },
    "suitcase": {
        "coco_cat_id": 33,
        "meaning": "cases used to carry belongings when traveling",
        "synset": "bag.n.06",
    },
    "cup": {
        "coco_cat_id": 47,
        "meaning": "a small open container usually used for drinking; usually has a handle",
        "synset": "cup.n.01",
    },
    "hair drier": {
        "coco_cat_id": 89,
        "meaning": "a hand-held electric blower that can blow warm air onto the hair",
        "synset": "hand_blower.n.01",
    },
    "surfboard": {
        "coco_cat_id": 42,
        "meaning": "a narrow buoyant board for riding surf",
        "synset": "surfboard.n.01",
    },
    "traffic light": {
        "coco_cat_id": 10,
        "meaning": "a device to control vehicle traffic often consisting of three or more lights",
        "synset": "traffic_light.n.01",
    },
    "tv": {
        "coco_cat_id": 72,
        "meaning": "an electronic device that receives television signals and displays them on a screen",
        "synset": "television_receiver.n.01",
    },
    "spoon": {
        "coco_cat_id": 50,
        "meaning": "a piece of cutlery with a shallow bowl-shaped container and a handle",
        "synset": "spoon.n.01",
    },
    "horse": {"coco_cat_id": 19, "meaning": "a common horse", "synset": "horse.n.01"},
    "motorcycle": {
        "coco_cat_id": 4,
        "meaning": "a motor vehicle with two wheels and a strong frame",
        "synset": "motorcycle.n.01",
    },
    "zebra": {
        "coco_cat_id": 24,
        "meaning": "any of several fleet black-and-white striped African equines",
        "synset": "zebra.n.01",
    },
    "cat": {"coco_cat_id": 17, "meaning": "a domestic house cat", "synset": "cat.n.01"},
    "teddy bear": {
        "coco_cat_id": 88,
        "meaning": "plaything consisting of a child's toy bear (usually plush and stuffed with soft materials)",
        "synset": "teddy.n.01",
    },
    "handbag": {
        "coco_cat_id": 31,
        "meaning": "a container used for carrying money and small personal items or accessories",
        "synset": "bag.n.04",
    },
    "sink": {
        "coco_cat_id": 81,
        "meaning": "plumbing fixture consisting of a water basin fixed to a wall or floor and having a drainpipe",
        "synset": "sink.n.01",
    },
    "keyboard": {
        "coco_cat_id": 76,
        "meaning": "a keyboard that is a data input device for computers",
        "synset": "computer_keyboard.n.01",
    },
    "bus": {
        "coco_cat_id": 6,
        "meaning": "a vehicle carrying many passengers; used for public transport",
        "synset": "bus.n.01",
    },
    "fork": {
        "coco_cat_id": 48,
        "meaning": "cutlery used for serving and eating food",
        "synset": "fork.n.01",
    },
    "chair": {
        "coco_cat_id": 62,
        "meaning": "a seat for one person, with a support for the back",
        "synset": "chair.n.01",
    },
    "refrigerator": {
        "coco_cat_id": 82,
        "meaning": "a refrigerator in which the coolant is pumped around by an electric motor",
        "synset": "electric_refrigerator.n.01",
    },
    "scissors": {
        "coco_cat_id": 87,
        "meaning": "a tool having two crossed pivoting blades with looped handles",
        "synset": "scissors.n.01",
    },
    "sheep": {
        "coco_cat_id": 20,
        "meaning": "woolly usually horned ruminant mammal related to the goat",
        "synset": "sheep.n.01",
    },
    "potted plant": {
        "coco_cat_id": 64,
        "meaning": "a container in which plants are cultivated",
        "synset": "pot.n.04",
    },
    "snowboard": {
        "coco_cat_id": 36,
        "meaning": "a board that resembles a broad ski or a small surfboard; used in a standing position to slide down snow-covered slopes",
        "synset": "snowboard.n.01",
    },
    "cow": {
        "coco_cat_id": 21,
        "meaning": "cattle that are reared for their meat",
        "synset": "beef.n.01",
    },
}
