from resources import *


class Or:
    __match_args__ = ("items",)

    items: list[tuple[int, str]]

    def __init__(self, items: list[tuple[int, str]]):
        self.items = items


class And:
    __match_args__ = ("items",)

    items: list[Or | tuple[int, str]]

    def __init__(self, items: list[Or | tuple[int, str]]):
        self.items = items


BUILDINGS_TO_RECIPES: dict[str, list[str | tuple[And | Or | tuple[int, str], str]]] = {
    # Buildings that don't need an entry:
      "Blight Post": [],
      "Bank": [], # What is this?
      "Farmfield": [],
      "Shelter": [],
      "Hydrant": [],
      "Path": [],
      "Storage (buildable)": [],
      "Barrels": [],
      "Temporary Hearth (buildable)": [],
      "Big Shelter": [],
      "Paved Road": [],
      "Reinforced Road": [],
      "Human House": [],
      "Trading Post": [],
      "Beaver House": [],
      "Fox House": [],
      "Lizard House": [],
      "Fence": [],
      "Harpy House": [],
      "CornerFence": [],
      "Comfort 2x2 - Park": [],
      "Pipe": [],
      "Pipe Valve": [],
      "Pipe End": [],
      "Tower": [],
      "Gate": [],
      "Lamp": [],
      "Road Sign": [],
      "Signboard": [],
      "Bush": [],
      "Flower Bed": [],
      "Nightfern": [],
      "Aestherics 2x2 - Garden": [],
      "Chest": [],
      "Cages": [],
      "Fire Shrine": [],
      "Lizard Post": [],
      "Water Extractor": [],
      "Sealed Biome Shrine": [],

    # Resource buildings have dummy recipes to show what they can take from the map:
    "Forager's Camp": [GRAIN, ROOT, VEGETABLE],
    "Primitive Forager's Camp": [GRAIN, ROOT, VEGETABLE],
    "Harvester Camp": [PLANT_FIBER, REED],
    "Herbalist's Camp": [BERRY, HERB, MUSHROOM],
    "Primitive Herbalist's Camp": [BERRY, HERB, MUSHROOM],
    "Rain Catcher": [CLEARANCE, DRIZZLE, STORM],
    "Stonecutter's Camp": [CLAY, SEA_MARROW, STONE],
    "Primitive Trapper's Camp": [MEAT, INSECT, EGG],
    "Trapper's Camp": [MEAT, INSECT, EGG],
    "Woodcutters Camp": [WOOD],

    "Bakery": [
        (And([(8, FLOUR), Or([(3, HERB), (3, BERRY), (3, ROOT)])]), (10, BISCUITS)),
        (And([(6, FLOUR), Or([(4, HERB), (4, MEAT), (4, INSECT), (4, EGG), (4, BERRY)])]), (10, PIPE)),
        (And([(3, CLAY), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (5, POTTERY)),
    ],
    "Beanery": [
        (And([Or([(3, HERB), (3, INSECT), (3, RESIN), (3, VEGETABLE)]), Or([(4, STONE), (4, CLAY)]), Or([(10, STORM), (14, CLEARANCE), (18, DRIZZLE)])]), (2, CRYSTALIZED_DEW)),
        (And([Or([(5, VEGETABLE), (5, MUSHROOM), (5, ROOT), (5, BERRY), (5, EGG)]), Or([(3, POTTERY), (3, BARREL), (2, WATERSKIN)])]), (10, PICKLED_GOOD)),
        (And([Or([(4, GRAIN), (4, VEGETABLE), (4, MUSHROOM), (4, HERB)]), Or([(6, DRIZZLE), (8, CLEARANCE), (10, STORM)])]), (10, PORRIDGE)),
    ],
    "Brick Oven": [
        ((15, WOOD), (3, COAL)),
        (And([Or([(6, HERB), (6, ROOT), (6, INSECT), (8, RESIN)]), Or([(6, WOOD), (3, OIL), (2, COAL), (2, SEA_MARROW)])]), (10, INSECT)),
        (And([(6, FLOUR), Or([(3, HERB), (3, MEAT), (3, INSECT), (3, EGG), (3, BERRY)])]), (10, PIPE)),
    ],
    "Butcher": [
        (And([Or([(4, INSECT), (4, MEAT), (4, MUSHROOM), (3, BERRY)]), Or([(4, VEGETABLE), (4, ROOT), (4, BERRY), (4, EGG)])]), (10, SKEWERS)),
        (And([Or([(5, INSECT), (5, MEAT)]), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (10, BERRY)),
        (Or([(3, GRAIN), (3, MEAT), (3, VEGETABLE), (3, PLANT_FIBER)]), (5, OIL)),
    ],
    "Cellar": [
        (And([Or([(6, VEGETABLE), (6, MUSHROOM), (6, ROOT), (6, BERRY), (6, EGG)]), Or([(3, POTTERY), (3, BARREL), (3, WATERSKIN)])]), (10, PICKLED_GOOD)),
        (And([Or([(6, INSECT), (6, MEAT)]), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (10, BERRY)),
        (And([Or([(2, BERRY), (2, MUSHROOM), (2, REED)]), Or([(2, POTTERY), (2, BARREL), (2, WATERSKIN)])]), (10, WINE)),
    ],
    "Cookhouse": [
        (And([Or([(4, INSECT), (4, MEAT), (4, MUSHROOM), (3, BERRY)]), Or([(4, VEGETABLE), (4, ROOT), (4, BERRY), (4, EGG)])]), (10, SKEWERS)),
        (And([(8, FLOUR), Or([(3, HERB), (3, BERRY), (3, ROOT)])]), (10, BISCUITS)),
        (Or([(4, INSECT), (4, BERRY), (4, COPPER_ORE), (3, COAL)]), (10, PIGMENT)),
    ],
    "Flawless Cellar": [
        (And([Or([(2, BERRY), (2, MUSHROOM), (2, REED)]), Or([(2, POTTERY), (2, BARREL), (2, WATERSKIN)])]), (10, WINE)),
        (And([Or([(4, VEGETABLE), (4, MUSHROOM), (4, ROOT), (4, BERRY), (4, EGG)]), Or([(3, POTTERY), (3, BARREL), (2, WATERSKIN)])]), (10, PICKLED_GOOD)),
        (And([Or([(4, INSECT), (4, MEAT)]), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (10, BERRY)),
    ],
    "Forester's Hut": [
        ((1, FARM_FIELD), (6, RESIN)),
        ((1, FARM_FIELD), (3, CRYSTALIZED_DEW)),
    ],
    "Granary": [
        (Or([(4, ROOT), (4, GRAIN), (4, VEGETABLE), (4, MUSHROOM)]), (2, PACK_OF_CROPS)),
        (And([Or([(5, VEGETABLE), (5, MUSHROOM), (5, ROOT), (5, BERRY), (5, EGG)]), Or([(3, POTTERY), (3, BARREL), (2, WATERSKIN)])]), (10, PICKLED_GOOD)),
        (Or([(3, PLANT_FIBER), (3, REED), (3, LEATHER)]), (2, FABRIC)),
    ],
    "Greenhouse": [
        ((4, DRIZZLE), (4, MUSHROOM)),
        ((4, DRIZZLE), (4, HERB)),
    ],
    "Grill": [
        (And([(6, COPPER_ORE), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (2, COPPER_BAR)),
        (And([Or([(6, GRAIN), (6, ROOT)]), Or([(3, POTTERY), (2, BARREL), (3, WATERSKIN)])]), (10, ALE)),
        (And([Or([(3, INSECT), (3, MEAT), (3, MUSHROOM), (2, BERRY)]), Or([(3, VEGETABLE), (3, ROOT), (3, BERRY), (3, EGG)])]), (10, SKEWERS)),
    ],
    "Hallowed Herb Garden": [
        ((1, FARM_FIELD), (9, ROOT)),
        ((1, FARM_FIELD), (9, HERB)),
    ],
    "Hallowed Small Farm": [
        ((1, FARM_FIELD), (9, VEGETABLE)),
        ((1, FARM_FIELD), (9, GRAIN)),
    ],
    "Herb Garden": [
        ((1, FARM_FIELD), (3, ROOT)),
        ((1, FARM_FIELD), (6, HERB)),
    ],
    "Homestead": [
        ((1, FARM_FIELD), (6, VEGETABLE)),
        ((1, FARM_FIELD), (6, MUSHROOM)),
        ((1, FARM_FIELD), (9, GRAIN)),
        ((1, FARM_FIELD), (9, PLANT_FIBER)),
    ],
    "Plantation": [
        ((1, FARM_FIELD), (6, BERRY)),
        ((1, FARM_FIELD), (6, PLANT_FIBER)),
    ],
    "Ranch": [
        (Or([(8, PLANT_FIBER), (8, REED), (8, GRAIN), (5, VEGETABLE)]), (10, MEAT)),
        (Or([(2, PLANT_FIBER), (2, REED), (2, GRAIN), (1, VEGETABLE)]), (4, LEATHER)),
        (Or([(3, GRAIN), (2, INSECT), (2, REED), (2, BERRY)]), (5, EGG)),
    ],
    "Small Farm": [
        ((1, FARM_FIELD), (3, VEGETABLE)),
        ((1, FARM_FIELD), (6, GRAIN)),
    ],
    "Smokehouse": [
        (And([(4, CLAY), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (5, POTTERY)),
        (And([Or([(6, HERB), (6, ROOT), (6, INSECT), (8, RESIN)]), Or([(6, WOOD), (3, OIL), (2, COAL), (2, SEA_MARROW)])]), (10, INSECT)),
        (And([Or([(4, INSECT), (4, MEAT)]), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (10, BERRY)),
    ],
    "Advanced Rain Collector": [
        DRIZZLE,
        CLEARANCE,
        STORM,
    ],
    "Alchemist's Hut": [
        (And([Or([(2, HERB), (2, INSECT), (2, RESIN), (2, VEGETABLE)]), Or([(3, STONE), (3, CLAY)]), Or([(8, STORM), (12, CLEARANCE), (16, DRIZZLE)])]), (2, CRYSTALIZED_DEW)),
        (And([Or([(3, HERB), (3, PIGMENT), (3, RESIN), (3, MUSHROOM), (3, ROOT)]), Or([(3, DRIZZLE), (4, CLEARANCE), (5, STORM)]), Or([(2, CRYSTALIZED_DEW), (2, COPPER_BAR)])]), (10, TEA)),
        (And([Or([(3, BERRY), (3, MUSHROOM), (3, REED)]), Or([(3, POTTERY), (3, BARREL), (3, WATERSKIN)])]), (10, WINE)),
    ],
    "Apothecary": [
        (And([Or([(3, HERB), (3, PIGMENT), (3, RESIN), (3, MUSHROOM), (3, ROOT)]), Or([(3, DRIZZLE), (4, CLEARANCE), (5, STORM)]), Or([(2, CRYSTALIZED_DEW), (2, COPPER_BAR)])]), (10, TEA)),
        (And([Or([(5, HERB), (5, ROOT), (5, INSECT), (7, RESIN)]), Or([(6, WOOD), (3, OIL), (2, COAL), (2, SEA_MARROW)])]), (10, INSECT)),
        (And([(8, FLOUR), Or([(3, HERB), (3, BERRY), (3, ROOT)])]), (10, BISCUITS)),
    ],
    "Artisan": [
        ((2, FABRIC), (10, COAL)),
        (And([Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
        (Or([(4, WINE), (4, TRAINING_GEAR), (4, INSECT), (4, SCROLL), (4, ALE), (4, TEA)]), (2, PACK_OF_LUXURY_GOODS)),
    ],
    "Brewery": [
        (And([Or([(6, VEGETABLE), (6, MUSHROOM), (6, ROOT), (6, BERRY), (6, EGG)]), Or([(3, POTTERY), (3, BARREL), (3, WATERSKIN)])]), (10, PICKLED_GOOD)),
        (Or([(5, ROOT), (5, GRAIN), (5, VEGETABLE), (5, MUSHROOM)]), (2, PACK_OF_CROPS)),
        (And([Or([(4, GRAIN), (4, ROOT)]), Or([(2, POTTERY), (1, BARREL), (2, WATERSKIN)])]), (10, ALE)),
    ],
    "Brickyard": [
        (And([Or([(3, HERB), (3, INSECT), (3, RESIN), (3, VEGETABLE)]), Or([(4, STONE), (4, CLAY)]), Or([(10, STORM), (14, CLEARANCE), (18, DRIZZLE)])]), (2, CRYSTALIZED_DEW)),
        (And([(3, CLAY), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (5, POTTERY)),
        (Or([(2, CLAY), (2, STONE)]), (2, BRICK)),
    ],
    "Carpenter": [
        ((5, WOOD), (2, PLANK)),
        (And([Or([(8, WOOD), (2, PLANK)]), Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)])]), (2, TOOL)),
        (Or([(4, WINE), (4, TRAINING_GEAR), (4, INSECT), (4, SCROLL), (4, ALE), (4, TEA)]), (2, PACK_OF_LUXURY_GOODS)),
    ],
    "Clothier": [
        (And([(6, LEATHER), Or([(4, OIL), (4, MEAT)])]), (10, WATERSKIN)),
        (And([Or([(4, LEATHER), (4, PLANT_FIBER), (10, WOOD)]), Or([(3, PIGMENT), (3, WINE)])]), (8, SCROLL)),
        ((1, FABRIC), (10, COAL)),
    ],
    "Cooperage": [
        (And([Or([(4, HERB), (4, PIGMENT), (4, RESIN), (4, MUSHROOM), (4, ROOT)]), Or([(4, DRIZZLE), (5, CLEARANCE), (6, STORM)]), Or([(2, CRYSTALIZED_DEW), (2, COPPER_BAR)])]), (10, TEA)),
        ((2, FABRIC), (10, COAL)),
        (And([Or([(1, COPPER_BAR), (1, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
    ],
    "Crude Workstation": [
        ((8, WOOD), (2, PLANK)),
        (Or([(6, PLANT_FIBER), (6, REED), (6, LEATHER)]), (2, FABRIC)),
        (Or([(6, CLAY), (6, STONE)]), (2, BRICK)),
        (Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)]), (2, PIPE)),
    ],
    "Distillery": [
        (And([Or([(3, BERRY), (3, MUSHROOM), (3, REED)]), Or([(3, POTTERY), (3, BARREL), (3, WATERSKIN)])]), (10, WINE)),
        (And([Or([(5, GRAIN), (5, VEGETABLE), (5, MUSHROOM), (5, HERB)]), Or([(7, DRIZZLE), (9, CLEARANCE), (11, STORM)])]), (10, PORRIDGE)),
        (And([Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
    ],
    "Druid's Hut": [
        (And([Or([(6, HERB), (6, ROOT), (6, INSECT), (8, RESIN)]), Or([(6, WOOD), (3, OIL), (2, COAL), (2, SEA_MARROW)])]), (10, INSECT)),
        ((3, FABRIC), (10, COAL)),
        (Or([(2, GRAIN), (2, MEAT), (2, VEGETABLE), (2, PLANT_FIBER)]), (5, OIL)),
    ],
    "Finesmith": [
        (And([(3, RESIN), Or([(10, CLEARANCE), (1, OIL)])]), (1, BERRY)),
        (And([Or([(6, WOOD), (1, PLANK)]), Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)])]), (2, TOOL)),
    ],
    "Flawless Brewery": [
        (And([Or([(4, GRAIN), (4, ROOT)]), Or([(2, POTTERY), (1, BARREL), (2, WATERSKIN)])]), (15, ALE)),
        (And([Or([(4, VEGETABLE), (4, MUSHROOM), (4, ROOT), (4, BERRY), (4, EGG)]), Or([(3, POTTERY), (3, BARREL), (2, WATERSKIN)])]), (15, PICKLED_GOOD)),
        (Or([(3, ROOT), (3, GRAIN), (3, VEGETABLE), (3, MUSHROOM)]), (5, PACK_OF_CROPS)),
    ],
    "Flawless Cooperage": [
        (And([Or([(1, COPPER_BAR), (1, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
        ((1, FABRIC), (10, COAL)),
        (And([Or([(2, HERB), (2, PIGMENT), (2, RESIN), (2, MUSHROOM), (2, ROOT)]), Or([(2, DRIZZLE), (3, CLEARANCE), (4, STORM)]), Or([(1, CRYSTALIZED_DEW), (1, COPPER_BAR)])]), (10, TEA)),
    ],
    "Flawless Druid's Hut": [
        (Or([(2, GRAIN), (2, MEAT), (2, VEGETABLE), (2, PLANT_FIBER)]), (5, OIL)),
        (And([Or([(4, HERB), (4, ROOT), (4, INSECT), (6, RESIN)]), Or([(6, WOOD), (3, OIL), (2, COAL), (2, SEA_MARROW)])]), (10, INSECT)),
        ((1, FABRIC), (10, COAL)),
    ],
    "Flawless Leatherworker": [
        (And([(4, LEATHER), Or([(2, OIL), (2, MEAT)])]), (10, WATERSKIN)),
        (Or([(2, PLANT_FIBER), (2, REED), (2, LEATHER)]), (2, FABRIC)),
        (Or([(3, INSECT), (3, BERRY), (3, COPPER_ORE), (2, COAL)]), (10, PIGMENT)),
    ],
    "Flawless Rain Mill": [
        (Or([(5, GRAIN), (5, MUSHROOM), (5, ROOT)]), (10, FLOUR)),
        (And([Or([(2, LEATHER), (2, PLANT_FIBER), (6, WOOD)]), Or([(1, PIGMENT), (1, WINE)])]), (8, SCROLL)),
        (Or([(6, PLANK), (3, FABRIC), (3, BRICK), (8, COPPER_ORE)]), (2, PACK_OF_BUILDING_MATERIALS)),
    ],
    "Flawless Smelter": [
        (And([(4, COPPER_ORE), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (2, COPPER_BAR)),
        (And([Or([(3, STONE), (1, COPPER_BAR), (1, CRYSTALIZED_DEW)]), Or([(2, PLANK), (2, REED)])]), (10, TRAINING_GEAR)),
        (And([(8, FLOUR), Or([(2, HERB), (2, BERRY), (2, ROOT)])]), (10, BISCUITS)),
    ],
    "Furnace": [
        (And([(5, COPPER_ORE), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (2, COPPER_BAR)),
        (Or([(3, CLAY), (3, STONE)]), (2, BRICK)),
        (And([(6, FLOUR), Or([(4, HERB), (4, MEAT), (4, INSECT), (4, EGG), (4, BERRY)])]), (10, PIPE)),
    ],
    "Kiln": [
        (Or([(4, CLAY), (4, STONE)]), (2, BRICK)),
        (And([Or([(6, INSECT), (6, MEAT)]), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (10, BERRY)),
        ((10, WOOD), (5, COAL)),
    ],
    "Leatherworker": [
        (Or([(3, PLANT_FIBER), (3, REED), (3, LEATHER)]), (2, FABRIC)),
        (Or([(4, INSECT), (4, BERRY), (4, COPPER_ORE), (3, COAL)]), (10, PIGMENT)),
        (And([(4, LEATHER), Or([(2, OIL), (2, MEAT)])]), (10, WATERSKIN)),
    ],
    "Lumber Mill": [
        (And([Or([(4, LEATHER), (4, PLANT_FIBER), (10, WOOD)]), Or([(3, PIGMENT), (3, WINE)])]), (8, SCROLL)),
        (Or([(8, PIGMENT), (8, OIL), (6, FLOUR), (6, POTTERY), (6, BARREL), (6, WATERSKIN)]), (2, PACK_OF_LUXURY_GOODS)),
        ((3, WOOD), (2, PLANK)),
    ],
    "Makeshift Post": [
        (Or([(6, ROOT), (6, GRAIN), (6, VEGETABLE), (6, MUSHROOM)]), (2, PACK_OF_CROPS)),
        (Or([(6, HERB), (6, BERRY), (6, INSECT), (6, MEAT), (6, EGG)]), (3, PACK_OF_PROVISIONS)),
        (Or([(10, PLANK), (6, FABRIC), (6, BRICK), (14, COPPER_ORE)]), (2, PACK_OF_BUILDING_MATERIALS)),
    ],
    "Manufactory": [
        (And([Or([(5, STONE), (2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), Or([(3, PLANK), (3, REED)])]), (10, TRAINING_GEAR)),
        (Or([(4, INSECT), (4, BERRY), (4, COPPER_ORE), (3, COAL)]), (10, PIGMENT)),
        (Or([(4, HERB), (4, BERRY), (4, INSECT), (4, MEAT), (4, EGG)]), (3, PACK_OF_PROVISIONS)),
    ],
    "Mine": [
        COAL,
        STONE,
        COPPER_ORE,
        CLAY,
    ],
    "Press": [
        (Or([(8, GRAIN), (8, MUSHROOM), (8, ROOT)]), (10, FLOUR)),
        (Or([(5, WINE), (5, TRAINING_GEAR), (5, INSECT), (5, SCROLL), (5, ALE), (5, TEA)]), (2, PACK_OF_LUXURY_GOODS)),
        (Or([(2, GRAIN), (2, MEAT), (2, VEGETABLE), (2, PLANT_FIBER)]), (5, OIL)),
    ],
    "Provisioner": [
        (Or([(7, GRAIN), (7, MUSHROOM), (7, ROOT)]), (10, FLOUR)),
        (And([Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
        (Or([(4, HERB), (4, BERRY), (4, INSECT), (4, MEAT), (4, EGG)]), (3, PACK_OF_PROVISIONS)),
    ],
    "Rain Collector": [
        DRIZZLE,
        CLEARANCE,
        STORM,
    ],
    "Rain Mill": [
        (And([Or([(4, LEATHER), (4, PLANT_FIBER), (10, WOOD)]), Or([(3, PIGMENT), (3, WINE)])]), (8, SCROLL)),
        (Or([(8, PLANK), (5, FABRIC), (5, BRICK), (12, COPPER_ORE)]), (2, PACK_OF_BUILDING_MATERIALS)),
        (Or([(5, GRAIN), (5, MUSHROOM), (5, ROOT)]), (10, FLOUR)),
    ],
    "Rainpunk Foundry": [
        (And([Or([(4, COPPER_BAR), (4, CRYSTALIZED_DEW), (15, STONE), (15, CLAY)]), Or([(1, COAL), (1, SEA_MARROW), (2, OIL), (5, WOOD)])]), (1, PARTS)),
        (And([(10, COAL), Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), Or([(10, STORM), (10, CLEARANCE)])]), (1, WILDFIRE_ESSENCE)),
    ],
    "Scribe": [
        (And([Or([(10, WOOD), (3, PLANK)]), Or([(4, COPPER_BAR), (4, CRYSTALIZED_DEW)])]), (2, TOOL)),
        (And([Or([(5, GRAIN), (5, ROOT)]), Or([(3, POTTERY), (2, BARREL), (3, WATERSKIN)])]), (10, ALE)),
        (And([Or([(2, LEATHER), (2, PLANT_FIBER), (6, WOOD)]), Or([(1, PIGMENT), (1, WINE)])]), (8, SCROLL)),
    ],
    "Smelter": [
        (And([(8, FLOUR), Or([(4, HERB), (4, BERRY), (4, ROOT)])]), (10, BISCUITS)),
        (And([Or([(5, STONE), (2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), Or([(3, PLANK), (3, REED)])]), (10, TRAINING_GEAR)),
        (And([(4, COPPER_ORE), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (2, COPPER_BAR)),
    ],
    "Smithy": [
        (And([Or([(8, WOOD), (2, PLANK)]), Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)])]), (2, TOOL)),
        (Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), (3, PIPE)),
        (Or([(6, PIGMENT), (6, OIL), (4, FLOUR), (4, POTTERY), (4, BARREL), (4, WATERSKIN)]), (2, PACK_OF_LUXURY_GOODS)),
    ],
    "Stamping Mill": [
        (And([(6, COPPER_ORE), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (2, COPPER_BAR)),
        (Or([(7, GRAIN), (7, MUSHROOM), (7, ROOT)]), (10, FLOUR)),
        (And([(2, CLAY), Or([(5, WOOD), (2, OIL), (1, COAL), (1, SEA_MARROW)])]), (5, POTTERY)),
    ],
    "Supplier": [
        (Or([(7, GRAIN), (7, MUSHROOM), (7, ROOT)]), (10, FLOUR)),
        ((5, WOOD), (2, PLANK)),
        (And([(5, LEATHER), Or([(3, OIL), (3, MEAT)])]), (10, WATERSKIN)),
    ],
    "Teahouse": [
        (And([(6, LEATHER), Or([(4, OIL), (4, MEAT)])]), (10, WATERSKIN)),
        (And([Or([(5, GRAIN), (5, VEGETABLE), (5, MUSHROOM), (5, HERB)]), Or([(7, DRIZZLE), (9, CLEARANCE), (11, STORM)])]), (10, PORRIDGE)),
        (And([Or([(2, HERB), (2, PIGMENT), (2, RESIN), (2, MUSHROOM), (2, ROOT)]), Or([(2, DRIZZLE), (3, CLEARANCE), (4, STORM)]), Or([(1, CRYSTALIZED_DEW), (1, COPPER_BAR)])]), (10, TEA)),
    ],
    "Tinctury": [
        (And([Or([(5, GRAIN), (5, ROOT)]), Or([(3, POTTERY), (2, BARREL), (3, WATERSKIN)])]), (10, ALE)),
        (And([Or([(3, BERRY), (3, MUSHROOM), (3, REED)]), Or([(3, POTTERY), (3, BARREL), (3, WATERSKIN)])]), (10, WINE)),
        (Or([(4, INSECT), (4, BERRY), (4, COPPER_ORE), (3, COAL)]), (10, PIGMENT)),
    ],
    "Tinkerer": [
        (And([Or([(8, WOOD), (2, PLANK)]), Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)])]), (2, TOOL)),
        (And([Or([(5, STONE), (2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), Or([(3, PLANK), (3, REED)])]), (10, TRAINING_GEAR)),
        (Or([(7, PLANK), (4, FABRIC), (4, BRICK), (10, COPPER_ORE)]), (2, PACK_OF_BUILDING_MATERIALS)),
    ],
    "Toolshop": [
        (And([Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)]), (2, PLANK)]), (10, BARREL)),
        (Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)]), (3, PIPE)),
        (And([Or([(6, WOOD), (1, PLANK)]), Or([(2, COPPER_BAR), (2, CRYSTALIZED_DEW)])]), (2, TOOL)),
    ],
    "Weaver": [
        (And([Or([(8, STONE), (3, COPPER_BAR), (3, CRYSTALIZED_DEW)]), Or([(3, PLANK), (3, REED)])]), (10, TRAINING_GEAR)),
        (Or([(8, PIGMENT), (8, OIL), (6, FLOUR), (6, POTTERY), (6, BARREL), (6, WATERSKIN)]), (2, PACK_OF_LUXURY_GOODS)),
        (Or([(2, PLANT_FIBER), (2, REED), (2, LEATHER)]), (2, FABRIC)),
    ],
    "Workshop": [
        (Or([(3, COPPER_BAR), (3, CRYSTALIZED_DEW)]), (2, PIPE)),
        ((5, WOOD), (2, PLANK)),
        (Or([(3, PLANT_FIBER), (3, REED), (3, LEATHER)]), (2, FABRIC)),
        (Or([(3, CLAY), (3, STONE)]), (2, BRICK)),
    ],

}
