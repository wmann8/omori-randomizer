from ast import Try
from cgitb import enable, text
import copy
from ctypes.wintypes import SIZE
import json
from multiprocessing.pool import ThreadPool
import os
from pprint import pprint
import shutil
import sys
from tkinter import DISABLED, END, filedialog
from tkinter.font import NORMAL
from unittest import main
import random
import yaml
from concurrent.futures import ThreadPoolExecutor
import PySimpleGUI as sg

# Okay, this shit is wack and needs to be organized first for me to have any chance of keeping all this shit straight:
# Shop Items: Item setting starts at eventCode 302/605 -> parameter[1] == itemType int, within event IDs 129, 265-270 in Map346.json
# Normal Pickups (Melons/NPCs): eventCode 122 -> parameter[0] == 830, parameter[4] == itemType int; eventCode 126 -> parameter[0] == itemID
# Weapon Pickups: eventCode 122 -> parameter[0] == 830, parameter[4] == itemType int; eventCode 127 -> parameter[0] == itemID
# Armor Pickups: eventCode 122 -> parameter[0] == 830, parameter[4] == itemType int; eventCode 128 -> parameter[0] == itemID

class PathStrings():
    
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'data')

        self.yamlpath = os.path.join(os.getcwd(), 'text')

        self.randopath = os.path.join(os.getcwd(), 'randomized_data')

        self.yamlrandopath = os.path.join(os.getcwd(), 'randomized_text')

itemlist = [[13, 'TOFU', 0],
 [14, 'CANDY', 0],
 [15, 'SMORES', 0],
 [16, 'GRANOLA BAR', 0],
 [17, 'BREAD', 0],
 [18, 'NACHOS', 0],
 [19, 'CHICKEN WING', 0],
 [20, 'HOT DOG', 0],
 [21, 'WAFFLE', 0],
 [22, 'PANCAKE', 0],
 [23, 'PIZZA SLICE', 0],
 [24, 'FISH TACO', 0],
 [25, 'CHEESEBURGER', 0],
 [26, 'CHOCOLATE', 0],
 [27, 'DONUT', 0],
 [28, 'RAMEN', 0],
 [29, 'SPAGHETTI', 0],
 [30, 'POPCORN', 0],
 [31, 'FRIES', 0],
 [32, 'CHEESE WHEEL', 0],
 [33, 'WHOLE CHICKEN', 0],
 [34, 'WHOLE PIZZA', 0],
 [35, 'SNO-CONE', 0],
 [36, 'TOMATO', 0],
 [37, 'COMBO MEAL', 0],
 [38, 'DINO CLUMPS', 0],
 [39, 'DINO PASTA', 0],
 [41, "MARI'S COOKIE", 0],
 [42, "MARI'S COOKIE", 1],
 [46, 'PLUM JUICE', 0],
 [47, 'APPLE JUICE', 0],
 [48, 'CHERRY SODA', 0],
 [49, 'STAR FRUIT SODA', 0],
 [50, 'BREADFRUIT JUICE', 0],
 [51, 'TASTY SODA', 0],
 [52, 'LEMONADE', 0],
 [53, 'PEACH SODA', 0],
 [54, 'BUTT PEACH SODA', 0],
 [55, 'ORANGE JUICE', 0],
 [56, 'PINEAPPLE JUICE', 0],
 [57, 'GRAPE SODA', 0],
 [58, 'BANANA SMOOTHIE', 0],
 [59, 'MANGO SMOOTHIE', 0],
 [60, 'BERRY SMOOTHIE', 0],
 [61, 'MELON SMOOTHIE', 0],
 [62, 'S.BERRY SMOOTHIE', 0],
 [63, 'WATERMELON JUICE', 0],
 [64, 'DINO MELON SODA', 0],
 [65, 'DINO SMOOTHIE', 0],
 [66, 'BOTTLED WATER', 0],
 [67, 'FRUIT JUICE?', 0],
 [68, 'PRUNE JUICE', 0],
 [69, 'ROTTEN MILK', 0],
 [70, 'MILK', 0],
 [73, 'CAN', 1],
 [74, 'GLASS BOTTLE', 1],
 [75, 'CARDBOARD', 1],
 [76, 'DEAD BATTERIES', 1],
 [77, 'COMPUTER PART', 1],
 [78, 'JACKS', 1],
 [79, 'RUBBER BAND', 1],
 [80, 'DYNAMITE', 1],
 [81, 'SPARKLER', 1],
 [82, 'CONFETTI', 1],
 [83, 'POETRY BOOK', 1],
 [84, 'RAIN CLOUD', 1],
 [85, 'PRESENT', 1],
 [86, 'AIR HORN', 1],
 [87, 'DANDELION', 1],
 [88, 'MUSH', 1],
 [89, 'LIFE JAM', 0],
 [91, 'COFFEE', 0],
 [92, 'DINO JAM', 0],
 [93, 'MYSTERY POTION', 1],
 [94, 'BIG RUBBER BAND', 1],
 [95, 'PEARL', 1],
 [96, 'JAM PACKETS', 0],
 [101, 'DONUT', 0],
 [102, 'CANDY', 0],
 [103, 'SALAD', 0],
 [104, 'BREAD', 0],
 [105, 'CHOCOLATE', 0],
 [106, 'PIZZA SLICE', 0],
 [107, 'HERO SANDWICH', 0],
 [108, 'CARAMEL APPLE', 0],
 [109, 'WHOLE PIZZA', 0],
 [110, 'PIE', 0],
 [111, 'BIG BAG OF CANDY', 0],
 [112, 'SLICE OF CAKE', 0],
 [113, 'BANDAGE', 1],
 [114, 'FIRST AID KIT', 1],
 [118, 'PEPPER SPRAY', 1],
 [120, 'TASTY SODA', 0],
 [121, 'ORANGE JOE', 0],
 [122, 'APPLE JUICE', 0],
 [123, 'ORANGE JUICE', 0],
 [124, 'COFFEE', 0]]

keyitemlist = [[2, 'COLD STEAK', 5],
 [3, 'MICROWAVED STEAK', 5],
 [115, 'HAMBURGER', 5],
 [116, 'MEAT', 5],
 [117, 'FISH', 5],
 [125, 'SMALL SKETCH', 5],
 [128, 'FOE FACTS!', 5],
 [129, 'JUNKYARD KEY', 5],
 [130, 'SPECIAL MIXTAPE', 5],
 [131, 'SHOW TICKETS', 5],
 [132, 'COOL KEY CARD', 5],
 [133, 'V.I.P. KEY CARD', 5],
 [134, 'WOODEN TRACK', 5],
 [135, 'SLIMY KEY CARD', 5],
 [136, 'EMOTION CHART', 5],
 [138, 'COLD STEAK', 5],
 [139, 'LUKEWARM STEAK', 5],
 [140, 'HERO’S GIFT', 5],
 [141, '"PIZZA" ORDER', 5],
 [142, 'BAKERY ORDER', 5],
 [143, 'HOMECOOKED MEAL', 5],
 [144, 'MICROWAVED MEAL', 5],
 [146, 'TOY BOX KEY', 5],
 [151, 'LIGHT BULB', 5],
 [153, 'TOY BOX KEY', 5],
 [157, 'SHEET MUSIC', 5],
 [158, 'FLOWER CROWN', 5],
 [161, 'JOKE BOOK', 5],
 [162, 'BIG AIRHORN', 5],
 [163, 'B.E.D.', 5],
 [164, 'BLACKMAIL', 5],
 [165, 'STRANGE LIST', 5],
 [166, 'INTERESTING BOOK', 5],
 [167, 'THINGAMABOB', 5],
 [168, 'WHATCHAMACALLIT', 5],
 [169, 'DOOHICKEY', 5],
 [170, 'CARE PACKAGE', 5],
 [171, 'GIANT CHECK', 5],
 [172, 'SPOOKY MAP', 5],
 [173, 'BATTERIES', 5],
 [174, 'ORANGE CREST', 5],
 [176, 'TEDDY BEAR', 5],
 [177, 'RAT MEAT', 5],
 [178, 'SNOT', 5],
 [179, 'SCRAP METAL', 5],
 [180, 'THANK-YOU FOSSIL', 5],
 [181, "PESSI'S THING", 5],
 [185, 'POTATO SPOON', 5],
 [186, 'PLASTIC SPOON', 5],
 [187, 'WOODEN SPOON', 5],
 [188, 'SILVER SPOON', 5],
 [190, 'BUTT CERTIFICATE', 5],
 [191, 'FLOWER PUZZLE', 5],
 [192, 'ANCIENT CODE', 5],
 [195, 'SEASHELL', 5],
 [196, 'RARE CARD', 5],
 [197, 'SMALL SKETCH', 5],
 [198, 'NOSTALGIC CD', 5],
 [199, 'CELESTIAL CD', 5],
 [200, 'MERRY CD', 5],
 [201, 'DEVILISH CD', 5],
 [202, 'OTHERWORLDLY CD', 5],
 [203, 'LIVELY CD', 5],
 [204, 'BRUTAL CD', 5],
 [205, 'ETHEREAL CD', 5],
 [206, 'GHOULISH CD', 5],
 [207, 'TRANQUIL CD', 5],
 [208, 'CHILL CD', 5],
 [209, 'DYNAMIC CD', 5],
 [210, 'SECRET CD', 5],
 [211, 'TRASH', 5],
 [212, 'BUBBLE WRAP', 5],
 [213, 'ARCADE PIECE', 5],
 [214, 'FLOWER CLIP', 5],
 [215, 'PRESCRIPTION', 5],
 [216, 'ID CARD', 5],
 [217, 'LUNCHBOX', 5],
 [218, 'LETTER FOR DAD', 5],
 [219, 'GARDEN SHEARS', 5],
 [220, 'GREEN FLYER', 5],
 [221, 'BLUE FLYER', 5],
 [222, 'TV REMOTE', 5],
 [223, "GRANNY'S MEDICINE", 5],
 [224, 'FLOOR LAMP', 5],
 [225, 'FLOWERS', 5],
 [226, 'MISSING TEETH', 5],
 [227, 'COIN', 5],
 [241, 'SPROUT MOLE MASKS', 5],
 [242, 'MATCHBOX', 5],
 [243, 'BAD DRAWING', 5],
 [244, 'CLEMS', 5],
 [246, 'RECIPE 4 DISASTER', 5],
 [247, 'SHEET MUSIC', 5],
 [248, 'PYRAMID KEY', 5],
 [249, 'TREASURE MAP', 5],
 [250, 'TRAIN PASS', 5],
 [251, 'SNO-CONE TICKET', 5],
 [252, 'ACTUAL MOLE', 5],
 [254, 'SELF-HELP GUIDE', 5],
 [286, 'TOMATO (BACKUP)', 5],
 [287, 'COMBO MEAL (BACKUP)', 5],
 [401, 'MIXTAPE', 5],
 [410, 'SUGAR', 5],
 [411, 'ALL-PURPOSE FLOUR', 5],
 [412, 'GARDEN SOIL', 5],
 [413, 'STRAWBERRIES', 5],
 [414, 'PINEBERRIES', 5],
 [415, 'BOTTLES OF FRUIT JUICE', 5],
 [416, 'STICK OF BUTTER', 5],
 [417, 'JAR OF PICKLES', 5],
 [418, 'BLUE FISH', 5],
 [419, 'EGG', 5],
 [420, 'LEATHER SHOE', 5],
 [421, 'ROAST CHICKEN', 5],
 [422, '#0422', 5],
 [700, 'TWENTY DOLLARS', 5],
 [701, '☐☐☐', 5],
 [702, '☐☐ ☐☐', 5],
 [703, "'KEY' INGREDIENT", 5],
 [800, 'YELLOW KEYCHAIN', 5],
 [801, 'GREEN KEYCHAIN', 5],
 [802, 'PINK KEYCHAIN', 5],
 [803, 'AMAZING KEYCHAIN', 5],
 [804, 'PURPLE BALL', 5],
 [805, 'PINK BALL', 5],
 [806, 'GREEN BALL', 5],
 [807, 'RED HAND', 5],
 [808, 'GREEN HAND', 5],
 [809, 'PURPLE HAND', 5],
 [810, 'GREEN SLINKY', 5],
 [811, 'BLUE SLINKY', 5],
 [812, 'YELLOW SLINKY', 5],
 [850, 'Blackletter A', 5],
 [851, 'Blackletter B', 5],
 [852, 'Blackletter C', 5],
 [853, 'Blackletter D', 5],
 [854, 'Blackletter E', 5],
 [855, 'Blackletter F', 5],
 [856, 'Blackletter G', 5],
 [857, 'Blackletter H', 5],
 [858, 'Blackletter I', 5],
 [859, 'Blackletter J', 5],
 [860, 'Blackletter K', 5],
 [861, 'Blackletter L', 5],
 [862, 'Blackletter M', 5],
 [863, 'Blackletter N', 5],
 [864, 'Blackletter O', 5],
 [865, 'Blackletter P', 5],
 [866, 'Blackletter Q', 5],
 [867, 'Blackletter R', 5],
 [868, 'Blackletter S', 5],
 [869, 'Blackletter T', 5],
 [870, 'Blackletter U', 5],
 [871, 'Blackletter V', 5],
 [872, 'Blackletter W', 5],
 [873, 'Blackletter X', 5],
 [874, 'Blackletter Y', 5],
 [875, 'Blackletter Z', 5],
 [876, 'Dreamworld Album (Hidden)', 5],
 [877, 'DW Polaroid 1', 5],
 [878, 'DW Polaroid 2', 5],
 [879, 'DW Polaroid 3', 5],
 [880, 'DW Polaroid 4', 5],
 [881, 'DW Polaroid 5', 5],
 [882, 'DW Polaroid 6', 5],
 [883, 'DW Polaroid 7', 5],
 [884, 'DW Polaroid 8', 5],
 [885, 'DW Polaroid 9', 5],
 [886, 'DW Polaroid 10', 5],
 [887, 'DW Polaroid 11', 5],
 [888, 'DW Polaroid 12', 5],
 [889, 'BlackSpace Album (Hidden)', 5],
 [890, 'BS Polaroid 1', 5],
 [891, 'BS Polaroid 2', 5],
 [892, 'BS Polaroid 3', 5],
 [893, 'BS Polaroid 4', 5],
 [894, 'BS Polaroid 5', 5],
 [895, 'BS Polaroid 6', 5],
 [896, 'BS Polaroid 7', 5],
 [897, 'BS Polaroid 8', 5],
 [898, 'BS Polaroid 9', 5],
 [899, 'BS Polaroid 10', 5],
 [900, 'BS Polaroid 11', 5],
 [901, 'BS Polaroid 12', 5],
 [902, 'BS Polaroid 13', 5],
 [903, 'BS Polaroid 14', 5],
 [904, 'BS Polaroid 15', 5],
 [905, 'BS Polaroid 16', 5],
 [906, 'BS Polaroid 17', 5],
 [907, 'BS Polaroid 18', 5],
 [908, 'BS Polaroid 19', 5],
 [909, 'BS Polaroid 20', 5],
 [910, 'BS Polaroid 21', 5],
 [911, 'BS Polaroid 22', 5],
 [912, 'BS Polaroid 23', 5],
 [913, 'BS Polaroid 24', 5],
 [914, 'Faraway Album (Hidden)', 5],
 [915, 'FA Polaroid 1', 5],
 [916, 'FA Polaroid 2', 5],
 [917, 'FA Polaroid 3', 5],
 [918, 'FA Polaroid 4', 5],
 [919, 'FA Polaroid 5', 5],
 [920, 'FA Polaroid 6', 5],
 [921, 'FA Polaroid 7', 5],
 [922, 'FA Polaroid 8', 5],
 [923, 'FA Polaroid 9', 5],
 [924, 'FA Polaroid 10', 5],
 [925, 'FA Polaroid 11', 5],
 [926, 'FA Polaroid 12', 5],
 [927, 'FA Polaroid 13', 5],
 [928, 'FA Polaroid 14', 5],
 [929, 'FA Polaroid 15', 5],
 [930, 'FA Polaroid 16', 5],
 [931, 'FA Polaroid 17', 5],
 [932, 'FA Polaroid 18', 5],
 [933, 'FA Polaroid 19', 5],
 [934, 'FA Polaroid 20', 5],
 [935, 'FA Polaroid 21', 5],
 [936, 'FA Polaroid 22', 5],
 [937, 'FA Polaroid 23', 5],
 [938, 'FA Polaroid 24', 5],
 [939, 'FA Polaroid 25', 5],
 [940, 'FA Polaroid 26', 5],
 [941, 'FA Polaroid 27', 5],
 [942, 'FA Polaroid 28', 5],
 [943, 'FA Polaroid 29', 5],
 [944, 'FA Polaroid 30', 5],
 [945, 'FA Polaroid 31', 5],
 [946, 'FA Polaroid 32', 5],
 [947, 'FA Polaroid 33', 5],
 [948, 'FA Polaroid 34', 5],
 [949, 'FA Polaroid 35', 5],
 [950, 'FA Polaroid 36', 5],
 [951, 'FA Polaroid 37', 5],
 [952, 'FA Polaroid 38', 5],
 [953, 'FA Polaroid 39', 5],
 [954, 'FA Polaroid 40', 5],
 [955, 'FA Polaroid 41', 5],
 [956, 'FA Polaroid 42', 5],
 [957, 'FA Polaroid 43', 5],
 [958, 'FA Polaroid 44', 5],
 [959, 'FA Polaroid 45', 5],
 [960, 'FA Polaroid 46', 5],
 [961, 'FA Polaroid 47', 5],
 [962, 'FA Polaroid 48', 5],
 [963, 'DW Polaroid 13', 5],
 [964, 'BLURRY PHOTO', 5],
 [966, 'PHOTO ALBUM', 5],
 [967, 'PHOTO ALBUM', 5],
 [968, 'PHOTO ALBUM', 5],
 [970, 'FA Polaroid 1', 5],
 [971, 'FA Polaroid 4', 5],
 [972, 'FA Polaroid 5', 5],
 [973, 'FA Polaroid 8', 5],
 [974, 'FA Polaroid 9', 5],
 [975, 'FA Polaroid 10', 5],
 [976, 'FA Polaroid 11', 5],
 [977, 'FA Polaroid 12', 5],
 [978, 'FA Polaroid 16', 5],
 [979, 'FA Polaroid 18', 5],
 [980, 'FA Polaroid 19', 5],
 [981, 'FA Polaroid 20', 5],
 [982, 'FA Polaroid 21', 5],
 [983, 'FA Polaroid 22', 5],
 [984, 'FA Polaroid 25', 5],
 [985, 'FA Polaroid 26', 5],
 [986, 'FA Polaroid 27', 5],
 [987, 'FA Polaroid 31', 5],
 [988, 'FA Polaroid 32', 5],
 [989, 'FA Polaroid 33', 5],
 [990, 'FA Polaroid 34', 5],
 [991, 'FA Polaroid 35', 5],
 [992, 'FA Polaroid 38', 5],
 [993, 'FA Polaroid 43', 5],
 [994, 'FA Polaroid 44', 5]]
 

weaponlist = [[2, 'SHINY KNIFE'],
 [3, 'KNIFE'],
 [4, 'DULL KNIFE'],
 [5, 'RUSTY KNIFE'],
 [6, 'RED KNIFE'],
 [8, 'FLY SWATTER'],
 [9, 'HANDS'],
 [10, 'VIOLIN'],
 [11, 'VIOLIN'],
 [12, 'VIOLIN'],
 [14, 'STUFFED TOY'],
 [15, 'COMET HAMMER'],
 [16, 'BODY PILLOW'],
 [17, 'POOL NOODLE'],
 [18, 'COOL NOODLE'],
 [19, "HERO'S TROPHY"],
 [20, 'MAILBOX'],
 [21, 'BAGUETTE'],
 [22, 'BASEBALL BAT'],
 [23, 'LOL SWORD'],
 [25, 'NAIL BAT'],
 [28, 'RUBBER BALL'],
 [29, 'METEOR BALL'],
 [30, 'BLOOD ORANGE'],
 [31, 'JACK'],
 [32, 'BEACH BALL'],
 [33, 'COCONUT'],
 [34, 'GLOBE'],
 [35, 'CHICKEN BALL'],
 [36, 'SNOWBALL'],
 [37, 'BASKETBALL'],
 [42, 'BASKETBALL'],
 [45, 'SPATULA'],
 [46, 'ROLLING PIN'],
 [47, 'TEAPOT'],
 [48, 'FRYING PAN'],
 [49, 'BLENDER'],
 [50, 'BAKING PAN'],
 [51, 'TENDERIZER'],
 [52, "OL' RELIABLE"],
 [53, 'SHUCKER'],
 [55, 'FIST'],
 [61, 'STEAK KNIFE'],
 [62, 'SWEETHEART BUST'],
 [110, 'STEAK KNIFE'],
 [112, 'SHINY KNIFE'],
 [113, 'KNIFE'],
 [114, 'DULL KNIFE']]

armorlist = [[2, '"GOLD" WATCH'],
 [4, '3D GLASSES'],
 [5, '3-LEAF CLOVER'],
 [6, '4-LEAF CLOVER'],
 [7, '5-LEAF CLOVER'],
 [8, 'APPENDIX'],
 [9, 'BABY CHICKEN'],
 [10, 'BACKPACK'],
 [11, 'BASEBALL CAP'],
 [12, 'BINOCULARS'],
 [13, 'BLANKET'],
 [14, 'BOOK'],
 [15, 'BOW-TIE'],
 [16, 'BRACELET'],
 [17, 'BREADPHONES'],
 [18, 'BUBBLE WRAP'],
 [19, 'BUNNY EARS'],
 [20, 'CACTUS'],
 [21, 'CAT EARS'],
 [22, 'CELLPHONE'],
 [23, 'CLAM COIN'],
 [24, 'COOL GLASSES'],
 [25, 'BOTTLE CAP'],
 [26, 'COUGH MASK'],
 [27, 'DAISY'],
 [28, 'EYE PATCH'],
 [29, 'FAUX TAIL'],
 [30, 'FEDORA'],
 [31, 'FINGER'],
 [32, 'FLOWER CLIP'],
 [33, 'FOX TAIL'],
 [34, 'FRIENDSHIP BRACELET'],
 [35, 'NERDY GLASSES'],
 [36, 'GOLD WATCH'],
 [37, 'HARD HAT'],
 [38, 'HEADBAND'],
 [39, 'HEART STRING'],
 [40, 'HIGH HEELS'],
 [41, 'HOMEWORK'],
 [42, 'INNER TUBE'],
 [43, 'LUCKY TOKEN'],
 [44, 'MAGICAL BEAN'],
 [45, 'MONOCLE'],
 [46, 'MUSTACHE'],
 [47, 'ONION RING'],
 [48, 'OVEN MITTS'],
 [49, 'PAPER BAG'],
 [50, 'HECTOR'],
 [51, 'PRETTY BOW'],
 [52, 'PUNCHING BAG'],
 [53, 'RABBIT FOOT'],
 [54, 'RED RIBBON'],
 [55, 'DEEP POETRY BOOK'],
 [56, 'RUBBER DUCK'],
 [57, 'SALES TAG'],
 [58, 'SEASHELL NECKLACE'],
 [59, 'SEER GOGGLES'],
 [60, 'TOP HAT'],
 [61, 'PET ROCK'],
 [62, 'HECTOR JR'],
 [63, 'WEDDING RING'],
 [64, 'WISHBONE'],
 [65, 'VEGGIE KID'],
 [66, 'WATERING PAIL'],
 [67, 'RAKE'],
 [68, 'SCARF'],
 [69, 'TEDDY BEAR'],
 [70, 'COTTON BALL'],
 [71, 'FLASHLIGHT'],
 [72, 'UNIVERSAL REMOTE'],
 [73, "CHEF'S HAT"],
 [74, 'TV REMOTE'],
 [75, 'SUNSCREEN'],
 [76, 'CONTRACT'],
 [77, 'FLOWER CROWN'],
 [78, "ABBI'S EYE"],
 [81, 'RED HAND'],
 [82, 'GREEN HAND'],
 [83, 'PURPLE HAND'],
 [84, 'PURPLE BALL'],
 [85, 'PINK BALL'],
 [86, 'GREEN BALL'],
 [87, 'GREEN SLINKY'],
 [88, 'BLUE SLINKY'],
 [89, 'YELLOW SLINKY'],
 [90, 'YELLOW KEYCHAIN'],
 [91, 'GREEN KEYCHAIN'],
 [92, 'PINK KEYCHAIN'],
 [93, 'CHIMERA KEYCHAIN'],
 [94, 'PET ROCK'],
 [95, 'FLOWER CLIP'],
 [96, 'RED HEADBAND'],
 [97, 'ORANGE HEADBAND'],
 [98, 'COOL GLASSES'],
 [99, 'SEASHELL NECKLACE'],
 [100, 'GOLD WATCH'],
 [101, '"GOLD" WATCH'],
 [102, 'FEDORA'],
 [103, 'RABBIT FOOT'],
 [104, 'TEDDY BEAR'],
 [105, '"YOU ROCK" CAP'],
 [106, 'PINWHEEL'],
 [107, 'PAINT BRUSH'],
 [108, 'COOL BOTTLECAP'],
 [109, "KEL'S PET ROCK"],
 [120, 'TULIP HAIRSTICK'],
 [121, 'GLADIOLUS HAIRBAND'],
 [122, 'CACTUS HAIRCLIP'],
 [123, 'ROSE HAIRCLIP']]

msg_dict = {}

def randomSelect():

    randSelectList = random.randint(0, 2)
    if randSelectList == 0:
        randList = itemlist
    elif randSelectList == 1:
        randList = weaponlist
    elif randSelectList == 2:
        randList = armorlist
    
    randSelectInner = random.randint(0, len(randList) - 1)

    return (randList[randSelectInner][0], randList[randSelectInner][1] ,randSelectList)

def randomizePrice(jsonFile, randopath):

    with open(os.path.join(randopath, jsonFile), encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if item != None:
                if jsonFile == 'Items.json':
                    if any(item['id'] in i for i in keyitemlist):
                        continue
                item['price'] = random.randint(1, 5000)
    
    with open(os.path.join(randopath, jsonFile), mode='w', encoding='utf-8') as updatedFile:
        json.dump(data, updatedFile)

def closeWindow():
    window.destroy()

def randoButton_Click():
    if values['folderinput'] != "":        
        Main()

def edit_yaml_value(y, splitList, itemName):
    with open(os.path.join(paths.yamlrandopath, y), encoding='utf-8') as file:
                    data = yaml.safe_load(file)                    
                    if data != None:
                        for k, v in data.items():
                            if isinstance(v, dict):
                                if k == splitList[1]:
                                    print(splitList[1])
                                    for key, value in v.items():
                                        if key == "text":
                                            if (value != None and type(value) == str):
                                                for list in [itemlist, weaponlist, armorlist]:
                                                    for sublist in list:
                                                        if sublist[1] in value:
                                                            v['text'] = value.replace(sublist[1], itemName, 1)
                                                            return data

def edit_yaml(y):
    for msg, itemName in msg_dict.items():
            splitList = msg.split(".")
            yam = f'{splitList[0]}.yaml'
            if y == yam:
                data = edit_yaml_value(y, splitList, itemName)
                if data != None:
                    with open(os.path.join(paths.yamlrandopath, y), 'w', encoding='utf-8') as updatedYaml:
                        yaml.dump(data, updatedYaml)
                        return f'{y} updated!'
    return ' '

def randomize_map_data(file):
    if file.startswith("Map"):
            if file != 'MapInfos.json':
                with open(os.path.join(paths.randopath, file), encoding='utf-8') as data_file:
                    print(f"{file}")
                    data = json.load(data_file)
                    events = data['events']
                    for event in events:
                        if event != None:
                            if event['id']:
                                if (file == 'Map346.json' and event['id'] == 264):
                                    continue
                                for page in event['pages']:
                                    toYamlCounter = 0
                                    lastItemName = ""
                                    lastMsg = ""
                                    for item in page['list']:                                        
                                        if item['code'] == 356:
                                            if item['parameters'][0].startswith("ShowMessage "):
                                                lastMsg = item['parameters'][0].split(" ")[1]
                                                if (toYamlCounter <= 2 and lastItemName != ""):
                                                    if not lastMsg in msg_dict.keys():
                                                        msg_dict[lastMsg] = lastItemName
                                                        toYamlCounter = 0
                                        if item['code'] == 126:
                                            if item['parameters'][1] == 0:
                                                if not any(item['parameters'][0] in i for i in keyitemlist):
                                                    itemID, itemName, listType = randomSelect()
                                                    if listType == 1:
                                                        item['code'] = 127
                                                    elif listType == 2:
                                                        item['code'] = 128
                                                    item['parameters'][0] = itemID
                                                    lastItemName = itemName
                                                    toYamlCounter += 1
                                                    if (lastMsg != "" and not lastMsg in msg_dict.keys() and toYamlCounter <= 2):
                                                        msg_dict[lastMsg] = lastItemName                                                                                                                                                                        
                                        elif item['code'] == 127:
                                            if item['parameters'][1] == 0:
                                                if item['parameters'][0] not in [2, 10, 11, 12, 14, 61, 110]:
                                                    itemID, itemName, listType = randomSelect()
                                                    if listType == 0:
                                                        item['code'] = 126
                                                    elif listType == 2:
                                                        item['code'] = 128
                                                    item['parameters'][0] = itemID
                                                    lastItemName = itemName
                                                    toYamlCounter += 1
                                                    if (lastMsg != "" and not lastMsg in msg_dict.keys() and toYamlCounter <= 2):
                                                        msg_dict[lastMsg] = lastItemName   
                                        elif item['code'] == 128:
                                            if item['parameters'][1] == 0:
                                                itemID, itemName, listType = randomSelect()
                                                if listType == 0:
                                                    item['code'] = 126
                                                elif listType == 1:
                                                    item['code'] = 127
                                                item['parameters'][0] = itemID
                                                lastItemName = itemName
                                                toYamlCounter += 1
                                                if (lastMsg != "" and not lastMsg in msg_dict.keys() and toYamlCounter <= 2):
                                                    msg_dict[lastMsg] = lastItemName
                                        elif item['code'] in [302, 605]:
                                            if event['id'] == 71:
                                                if item['code'] == 302:
                                                    continue
                                            itemID, itemName, listType = randomSelect()
                                            if listType == 1:
                                                item['parameters'][0] = 1
                                            elif listType == 2:
                                                item['parameters'][0] = 2
                                            item['parameters'][1] = itemID
                                            item['parameters'][2] = 0
                                            # item['parameters'][3] = random.randint(1, 1000)
                                            toYamlCounter += 1

                with open(os.path.join(paths.randopath, file), mode="w", encoding="utf-8") as updatedFile:
                    json.dump(data, updatedFile)
    
    return f'{file} randomized!'

def browse_files():

    folder = filedialog.askdirectory(initialdir=os.getcwd(), title="Select randomizeralpha folder")

    paths.path = None

    paths.yamlpath = None

    paths.randopath = None

    paths.yamlrandopath = None

    paths.path = os.path.join(folder, 'data')

    paths.yamlpath = os.path.join(folder, 'text')

    paths.randopath = os.path.join(folder, 'randomized_data')

    paths.yamlrandopath = os.path.join(folder, 'randomized_text')

    folder_field.update(folder)
    folder_field.Widget.xview_moveto(1)

def Main():

    randomize_button(disabled=True)
    close_button(disabled=True)

    for f in os.listdir(paths.randopath):
        os.remove(os.path.join(paths.randopath, f))

    for f in os.listdir(paths.yamlrandopath):
        os.remove(os.path.join(paths.yamlrandopath, f))

    file_list = []
    yaml_list = []

    

    for file in os.listdir(paths.path):
        shutil.copy(os.path.join(paths.path, file), os.path.join(paths.randopath, file))

    for file in os.listdir(paths.yamlpath):
        shutil.copy(os.path.join(paths.yamlpath, file), os.path.join(paths.yamlrandopath, file))

    for file in os.listdir(paths.randopath):
        newfile = copy.deepcopy(file)
        file_list.append(newfile)

    for file in os.listdir(paths.yamlrandopath):
        newYaml = copy.deepcopy(file)
        yaml_list.append(newYaml)

    executor = ThreadPoolExecutor()
    results = executor.map(randomize_map_data, file_list)

    for result in results:
        print(result)
    
    for file in ['Items.json', 'Weapons.json', 'Armors.json']:
        randomizePrice(file, paths.randopath)
    
    with open(os.path.join(paths.randopath, 'Enemies.json'), encoding='utf-8') as enemyFile:
        data = json.load(enemyFile)
        for enemy in data:
            if enemy != None:
                for item in enemy['dropItems']:
                    if item['kind'] != 0:
                        itemID, itemName, itemType = randomSelect()
                        item['kind'] = itemType + 1
                        item['dataId'] = itemID
    
    with open(os.path.join(paths.randopath, 'Enemies.json'), mode='w', encoding='utf-8') as updatedEnemyFile:
        json.dump(data, updatedEnemyFile)

    with open(os.path.join(paths.randopath, 'CommonEvents.json'), encoding='utf-8') as eventFile:
        data = json.load(eventFile)
        for event in data:
            if event != None:
                for item in event['list']:
                    if item['code'] == 126:
                        if item['parameters'][1] == 0:
                            if not any(item['parameters'][0] in i for i in keyitemlist):
                                itemID, itemName, listType = randomSelect()
                                if listType == 1:
                                    item['code'] = 127
                                elif listType == 2:
                                    item['code'] = 128
                                item['parameters'][0] = itemID
                    elif item['code'] == 127:
                        if item['parameters'][1] == 0:
                            if item['parameters'][0] not in [2, 10, 11, 12, 14, 61, 110]:
                                itemID, itemName, listType = randomSelect()
                                if listType == 0:
                                    item['code'] = 126
                                elif listType == 2:
                                    item['code'] = 128
                                item['parameters'][0] = itemID
                    elif item['code'] == 128:
                        if item['parameters'][1] == 0:
                            itemID, itemName, listType = randomSelect()
                            if listType == 0:
                                item['code'] = 126
                            elif listType == 1:
                                item['code'] = 127
                            item['parameters'][0] = itemID
                    elif item['code'] in [302, 605]:
                        itemID, itemName, listType = randomSelect()
                        if listType == 1:
                            item['parameters'][0] = 1
                        elif listType == 2:
                            item['parameters'][0] = 2
                        item['parameters'][1] = itemID
                        item['parameters'][2] = 0
                        # item['parameters'][3] = random.randint(1, 1000)

    with open(os.path.join(paths.randopath, 'CommonEvents.json'), mode='w', encoding='utf-8') as updatedEventFile:
        json.dump(data, updatedEventFile)

    executor = ThreadPoolExecutor()
    results = executor.map(edit_yaml, yaml_list)

    for result in results:
        print(result)

    progress_text.update('Randomization Complete!')
    close_button(disabled=False)



if __name__ == '__main__':

    try:
        paths = PathStrings()

        sg.theme('DarkPurple')   # Add a touch of color
        
        sg.theme_input_background_color('Black')
        sg.theme_input_text_color('Tan')
        sg.theme_text_color('Tan')
        

        # All the stuff inside your window.
        layout = [  [sg.InputText(default_text=os.getcwd(), key='folderinput'), sg.Button('Browse')],
                    [sg.Button('Randomize!', key='randobutton')],
                    [sg.Text('', key='progtext')],
                    [sg.Button('Close', key='closebutton')] ]

        # Create the Window
        window = sg.Window('OMORI Randomizer v0.13.1a', layout, finalize=True)
        progress_text = window['progtext']
        folder_field = window['folderinput']
        randomize_button = window['randobutton']
        close_button = window['closebutton']

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'closebutton': # if user closes window or clicks close
                break
            if event == 'Browse':
                browse_files()
            if event == 'randobutton':
                progress_text.update("Randomizing data. Please wait...")
                window.Refresh()
                randoButton_Click()
            

        window.close()

    except Exception:
            type, value, traceback = sys.exc_info()
            print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')
    
    