# Use singular for consistency.  Important each variable is the lowercase version of its name
ALE = "ale"
BARREL = "barrel"
BERRY = "berry"
BISCUITS = "biscuits"
BRICK = "brick"
CLAY = "clay"
CLEARANCE = "clearance"
COAL = "coal"
COPPER_ORE = "copper_ore"
COPPER_BAR = "copper_bar"
CRYSTALIZED_DEW ="crystalized_dew"
DRIZZLE = "drizzle"
EGG = "egg"
FABRIC = "fabric"
FLOUR = "flour"
GRAIN = "grain"
HERB = "herb"
INCENSE = "incense"
INSECT = "insect"
LEATHER = "leather"
MEAT = "meat"
MUSHROOM = "mushroom"
OIL = "oil"
PACK_OF_BUILDING_MATERIALS = "pack_of_building_materials"
PACK_OF_CROPS = "pack_of_crops"
PACK_OF_LUXURY_GOODS = "pack_of_luxury_goods"
PACK_OF_PROVISIONS = "pack_of_provisions"
PARTS = "parts"
PICKLED_GOOD = "pickled_good"
PIGMENT = "pigment"
PIPE = "pipe"
PLANK = "plank"
PLANT_FIBER = "plant_fiber"
PORRIDGE = "porridge"
POTTERY = "pottery"
REED = "reed"
RESIN = "resin"
ROOT = "root"
SCROLL = "scroll"
SEA_MARROW = "sea_marrow"
SKEWERS = "skewers"
STONE = "stone"
STORM = "storm"
TEA = "tea"
TRAINING_GEAR = "training_gear"
VEGETABLE = "vegetable"
TOOL = "tool"
WATERSKIN = "waterskin"
WILDFIRE_ESSENCE = "wildfire_essence"
WINE = "wine"
WOOD = "wood"
#Pseudo-resource:
FARM_FIELD = "farm_field"
BRAWLING = "brawling"
CLEANLINESS = "cleanliness"
EDUCATION = "education"
LEISURE = "leisure"
LUXURY = "luxury"
RELIGION = "religion"



# Hack!
ALL_RESOURCES = [item for item in dir() if not item.startswith("__")]

RESOURCE_NODE_TO_NAME = {
    "Node Clay Deposit": CLAY,
    "Node Dewberries": BERRY,
    "Node Insect Nest": INSECT,
    "Node Mushroom Deposit": MUSHROOM,
    "Node Reed Deposit": REED,
    "Node Root Deposit": ROOT,
    "Node Sea Marrow Deposit": SEA_MARROW,
    "Node Snail Broodmother": MEAT,
}