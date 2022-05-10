from ast import Try
from cgitb import enable, text
import copy
from ctypes.wintypes import SIZE
import json
from multiprocessing.pool import ThreadPool
import os
from pprint import pprint
from re import I
import shutil
import sys
from tkinter import DISABLED, END, filedialog
from tkinter.font import NORMAL
from unittest import main
import random
import yaml
from concurrent.futures import ThreadPoolExecutor
import PySimpleGUI as sg
import configparser


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
 [111, 'BIG BAG OF CANDY', 5],
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
 

weaponlist = [[2, 'SHINY KNIFE', False],
 [3, 'KNIFE', False],
 [4, 'DULL KNIFE', False],
 [5, 'RUSTY KNIFE', False],
 [6, 'RED KNIFE', False],
 [8, 'FLY SWATTER', False],
 [9, 'HANDS', False],
 [10, 'VIOLIN', False],
 [11, 'VIOLIN', False],
 [12, 'VIOLIN', False],
 [14, 'STUFFED TOY', False],
 [15, 'COMET HAMMER', False],
 [16, 'BODY PILLOW', False],
 [17, 'POOL NOODLE', False],
 [18, 'COOL NOODLE', False],
 [19, "HERO'S TROPHY", False],
 [20, 'MAILBOX', False],
 [21, 'BAGUETTE', False],
 [22, 'BASEBALL BAT', False],
 [23, 'LOL SWORD', False],
 [25, 'NAIL BAT', False],
 [28, 'RUBBER BALL', False],
 [29, 'METEOR BALL', False],
 [30, 'BLOOD ORANGE', False],
 [31, 'JACK', False],
 [32, 'BEACH BALL', False],
 [33, 'COCONUT', False],
 [34, 'GLOBE', False],
 [35, 'CHICKEN BALL', False],
 [36, 'SNOWBALL', False],
 [37, 'BASKETBALL', False],
 [42, 'BASKETBALL', False],
 [45, 'SPATULA', False],
 [46, 'ROLLING PIN', False],
 [47, 'TEAPOT', False],
 [48, 'FRYING PAN', False],
 [49, 'BLENDER', False],
 [50, 'BAKING PAN', False],
 [51, 'TENDERIZER', False],
 [52, "OL' RELIABLE", False],
 [53, 'SHUCKER', False],
 [55, 'FIST', False],
 [61, 'STEAK KNIFE', False],
 [62, 'SWEETHEART BUST', False],
 [110, 'STEAK KNIFE', False],
 [112, 'SHINY KNIFE', False],
 [113, 'KNIFE', False],
 [114, 'DULL KNIFE', False]]

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

# TODO: Add in logic to iterate through Classes of ID 1-4 and randomize skills!
# TODO: Take into account skills obtained through means other than level up and randomize those too!
playerSkillList = [[25, 'OBSERVE', False],
[26, 'SAD POEM', False],
[27, 'STAB', False],
[28, 'HACK AWAY', False],
[30, 'BREAD SLICE', False],
[31, 'HIDE ', False],
[32, 'LUCKY SLICE', False],
[33, 'TRICK', False],
[34, 'SHUN', False],
[35, 'MOCK', False],
[36, 'EXPLOIT', False],
[37, 'FINAL STRIKE', False],
[38, 'RED HANDS', False],
[41, 'STARE', False],
[43, 'DEEP BREATH', False],
[44, 'PAINFUL TRUTH', False],
[68, 'PEP TALK', False],
[69, 'HEADBUTT', False],
[70, 'HOMERUN ', False],
[71, 'WIND-UP THROW', False],
[72, 'POWER HIT', False],
[73, 'LAST RESORT', False],
[74, 'COUNTER', False],
[75, 'MASH', False],
[76, 'TWIRL', False],
[77, 'MOOD WRECKER', False],
[78, 'BEATDOWN', False],
[84, 'TEAM SPIRIT', False],
[107, 'ANNOY', False],
[108, 'FLEX ', False],
[109, 'REBOUND', False],
[110, 'JUICE ME', False],
[111, 'RALLY', False],
[112, 'SNOWBALL', False],
[113, 'TICKLE', False],
[114, 'RICOCHET', False],
[115, "RUN 'N GUN", False],
[116, 'MEGAPHONE', False],
[117, "CAN'T CATCH ME", False],
[123, 'CURVEBALL', False],
[124, 'COMEBACK', False],
[147, 'COOK', False],
[148, 'MASSAGE', False],
[149, 'SMILE', False],
[150, 'REFRESH', False],
[151, 'SNACK TIME', False],
[152, 'TEA TIME ', False],
[153, 'CHARM', False],
[154, 'CAPTIVATE', False],
[155, 'MESMERIZE', False],
[156, 'SHARE FOOD', False],
[157, 'FAST FOOD', False],
[158, 'HOMEMADE JAM', False],
[159, 'TENDERIZE', False],
[160, 'ENCHANT', False],
[161, 'DAZZLE', False],
[162, 'SPICY FOOD', False],
[163, 'GATOR AID', False],
[185, 'FIRST AID', False]]

enemySkillList = [
[207, '// RANDOM ENEMIES //', False],
[208, '// FOREST BUNNY //', False],
[209, 'ATTACK', False],
[210, 'DO NOTHING', False],
[211, 'BE CUTE', False],
[212, 'SAD EYES', False],
[217, '// FOREST BUNNY? //', False],
[218, 'ATTACK', False],
[219, 'DO NOTHING', False],
[220, 'BE CUTE?', False],
[221, 'SAD EYES?', False],
[226, '// LOST SPROUT MOLE //', False],
[227, 'ATTACK', False],
[228, 'DO NOTHING', False],
[229, 'RUN AROUND', False],
[234, '(Tutorial: Happy) RUN AROUND', False],
[235, '// SPACE BUNNY //', False],
[236, 'ATTACK', False],
[237, 'DO NOTHING', False],
[238, 'BUNNY BEAM', False],
[244, '// DUST BUNNY //', False],
[245, 'DO NOTHING', False],
[246, 'SCATTER', False],
[252, '// U.F.O. //', False],
[253, 'ATTACK', False],
[254, 'DO NOTHING', False],
[255, 'ORANGE BEAM', False],
[256, 'STRANGE BEAM', False],
[261, '// VENUS FLY TRAP //', False],
[262, 'ATTACK', False],
[263, 'DO NOTHING', False],
[264, 'CRUNCH', False],
[270, '// WORMHOLE //', False],
[271, 'ATTACK', False],
[272, 'DO NOTHING', False],
[273, 'OPEN WORMHOLE', False],
[279, '// MIX TAPE //', False],
[280, 'ATTACK', False],
[281, 'DO NOTHING', False],
[282, 'TANGLE', False],
[288, '// DIAL UP //', False],
[289, 'ATTACK', False],
[290, 'DO NOTHING', False],
[291, 'SLOW DOWN ALL', False],
[297, '// DOOM BOX //', False],
[298, 'ATTACK', False],
[299, 'DO NOTHING', False],
[300, 'BLAST MUSIC', False],
[306, '// SHARK PLANE //', False],
[307, 'ATTACK', False],
[308, 'DO NOTHING', False],
[309, 'OVERCLOCK ENGINES', False],
[310, 'CHOMP', False],
[316, '// SNOW BUNNY //', False],
[317, 'ATTACK', False],
[318, 'DO NOTHING', False],
[319, 'SMALL SNOW STORM', False],
[325, '// SNOW ANGEL //', False],
[326, 'ATTACK', False],
[327, 'UPLIFTING HYMN', False],
[328, 'PIERCE HEART', False],
[334, '// SNOW PILE //', False],
[335, 'ATTACK', False],
[336, 'DO NOTHING', False],
[337, 'ENGULF', False],
[338, 'MORE SNOW', False],
[343, '// BUN BUNNY //', False],
[344, 'ATTACK ', False],
[345, 'DO NOTHING', False],
[346, 'HIDE', False],
[352, '//TOASTY//', False],
[353, 'ATTACK', False],
[354, 'DO NOTHING', False],
[355, 'RILE', False],
[359, '//SOURDOUGH//', False],
[360, 'ATTACK', False],
[361, 'DO NOTHING', False],
[362, 'BAD WORD', False],
[366, '//SESAME//', False],
[367, 'ATTACK', False],
[368, 'DO NOTHING', False],
[369, 'BREAD ROLL', False],
[372, '// CREEPY PASTA //', False],
[373, 'ATTACK', False],
[374, 'DO NOTHING', False],
[375, 'SCARE', False],
[381, '// COPY PASTA //', False],
[382, 'ATTACK', False],
[383, 'DUPLICATE', False],
[389, '// HUSH PUPPY //', False],
[390, 'ATTACK', False],
[391, 'DO NOTHING', False],
[392, 'MUFFLED SCREAMS', False],
[398, '// LIVING BREAD //', False],
[399, 'ATTACK', False],
[400, 'DO NOTHING', False],
[401, 'BITE', False],
[402, 'BAD SMELL SETUP', False],
[403, 'BAD SMELL SKILL', False],
[408, '//GINGER DEAD MAN//', False],
[409, 'ATTACK', False],
[410, 'DO NOTHING', False],
[411, 'BITE ARM', False],
[416, '//PORCUPIE//', False],
[417, 'ATTACK', False],
[418, 'DO NOTHING', False],
[419, 'PIERCE ', False],
[420, 'COUNTER SETUP', False],
[421, 'COUNTER SPIKE', False],
[425, '// BUG BUNNY //', False],
[426, 'ATTACK', False],
[427, 'DO NOTHING', False],
[428, 'SUDDEN JUMP', False],
[429, 'SCUTTLE', False],
[434, '// RARE BEAR //', False],
[435, 'ATTACK', False],
[436, 'BEAR HUG', False],
[437, 'ROAR ', False],
[438, 'COUNTER SWIPE SETUP', False],
[439, 'COUNTER SWIPE SKILL', False],
[443, '// POTTED PLANT //', False],
[444, 'ATTACK', False],
[445, 'DO NOTHING', False],
[446, 'TRIP', False],
[447, 'EXPLODE', False],
[453, '// SPIDER CAT //', False],
[454, 'ATTACK', False],
[455, 'DO NOTHING', False],
[456, 'SPIN WEB', False],
[457, 'SCUTTLE', False],
[462, '// SPROUT MOLE? //', False],
[463, 'ATTACK', False],
[464, 'DO NOTHING', False],
[465, 'RUN AROUND', False],
[471, '// HAROLD //', False],
[472, 'ATTACK', False],
[473, 'DO NOTHING', False],
[474, 'PROTECT', False],
[475, 'WINK', False],
[481, '// MARSHA //', False],
[482, 'ATTACK', False],
[483, 'DO NOTHING', False],
[484, 'SPIN', False],
[485, 'CHOP', False],
[491, '// THERESE //', False],
[492, 'ATTACK', False],
[493, 'DO NOTHING', False],
[494, 'SNIPE', False],
[495, 'INSULT', False],
[496, 'DOUBLE SHOT', False],
[501, '// LUSCIOUS //', False],
[502, 'ATTACK', False],
[503, 'DO NOTHING', False],
[504, 'FIRE MAGIC', False],
[505, 'MISFIRE MAGIC', False],
[511, '// HORSE HEAD //', False],
[512, 'ATTACK', False],
[513, 'DO NOTHING', False],
[514, 'LICK', False],
[515, 'WHINNY', False],
[520, '// HORSE BUTT //', False],
[521, 'ATTACK', False],
[522, 'DO NOTHING', False],
[523, 'KICK', False],
[524, 'PRANCE', False],
[529, '// FISH BUNNY //', False],
[530, 'ATTACK', False],
[531, 'DO NOTHING', False],
[532, 'SCHOOLING', False],
[538, '// GATOR GUY //', False],
[539, 'ATTACK', False],
[540, 'DO NOTHING', False],
[541, 'ROUGH UP', False],
[547, '// SQUIZZARD //', False],
[548, 'ATTACK', False],
[549, 'DO NOTHING', False],
[550, 'SQUID WARD', False],
[551, 'SQUID MAGIC', False],
[557, '// MUSSEL //', False],
[558, 'ATTACK', False],
[559, 'FLEX', False],
[560, 'HIDE', False],
[566, '// REVERSE MERMAID //', False],
[567, 'ATTACK', False],
[568, 'DO NOTHING', False],
[569, 'RUN AROUND', False],
[575, '// SHARK FIN //', False],
[576, 'ATTACK', False],
[577, 'DO NOTHING', False],
[578, 'BITE', False],
[579, 'WORK UP', False],
[584, '//ANGI//', False],
[585, 'ATTACK', False],
[586, 'DO NOTHING', False],
[587, 'BRIGHT LIGHT', False],
[588, 'CRUNCH', False],
[589, 'LIGHTS OFF', False],
[595, '// SLIME BUNNY //', False],
[596, 'ATTACK', False],
[597, 'DO NOTHING', False],
[599, 'STICKY ', False],
[604, '// WATERMELON MIMIC //', False],
[605, 'RUBBER BAND', False],
[606, 'JACKS', False],
[607, 'DYNAMITE', False],
[608, 'TOMATO', False],
[609, 'GRAPES', False],
[610, 'FRENCH FRIES', False],
[611, 'CONFETTI', False],
[612, 'RAIN CLOUD', False],
[613, 'AIR HORN', False],
[619, '// WORM-BOT //', False],
[620, 'ATTACK', False],
[621, 'DO NOTHING', False],
[622, 'LASER', False],
[623, 'REPAIR', False],
[629, '// SNOT BUBBLE //', False],
[630, 'INFLATE', False],
[631, 'POP', False],
[632, 'POP (ON DEATH)', False],
[638, '//LAB RAT//', False],
[639, 'ATTACK', False],
[640, 'DO NOTHING', False],
[641, 'HAPPY GAS', False],
[642, 'SCURRY SETUP', False],
[643, 'SCURRY SKILL', False],
[648, '//SPROUT MOLE??//', False],
[649, 'ATTACK', False],
[650, 'DO NOTHING', False],
[651, 'EXPLODE', False],
[652, 'STRANGE LASER', False],
[653, 'JET PACK RUN AROUND', False],
[659, '//CHICKEN?//', False],
[660, 'RUN AWAY', False],
[661, 'DO NOTHING', False],
[667, '// SALLI //', False],
[668, 'ATTACK', False],
[669, 'DO NOTHING', False],
[670, 'SPEED UP', False],
[671, 'DODGE ANNOY SETUP', False],
[672, 'DODGE ANNOY SKILL', False],
[673, 'LIAR', False],
[677, '// CINDI //', False],
[678, 'ATTACK', False],
[679, 'DO NOTHING', False],
[680, 'SLAM', False],
[681, 'COUNTER ATTACK SET UP', False],
[682, 'COUNTER ATTACK SKILL', False],
[683, 'LIAR', False],
[687, '// DOROTHI //', False],
[688, 'ATTACK', False],
[689, 'DO NOTHING', False],
[690, 'ATTACK TWICE', False],
[691, 'ATTACK THRICE', False],
[692, 'SELF HAPPY', False],
[693, 'LIAR', False],
[699, '// NANCI //', False],
[700, 'ATTACK', False],
[701, 'DO NOTHING', False],
[702, 'SELF ANGRY', False],
[703, 'LIAR', False],
[708, '// MERCI //', False],
[709, 'ATTACK', False],
[710, 'DO NOTHING', False],
[711, 'MELODY', False],
[712, 'SCREAM', False],
[713, 'LIAR', False],
[718, '// LILI //', False],
[719, 'ATTACK', False],
[720, 'DO NOTHING', False],
[721, 'MULTIPY', False],
[722, 'CRY', False],
[723, 'SAD EYES', False],
[724, 'LIAR', False],
[729, '// HOUSEFLY //', False],
[730, 'ATTACK', False],
[731, 'DO NOTHING', False],
[732, 'ANNOY', False],
[738, '// RECYCLIST //', False],
[739, 'FLING TRASH', False],
[740, 'GATHER TRASH', False],
[747, '// STRAY DOG //', False],
[748, 'ATTACK', False],
[749, 'HOWL', False],
[755, '// CROW //', False],
[756, 'ATTACK', False],
[757, 'GRIN', False],
[758, 'STEAL', False],
[764, '// BOSSES //', False],
[765, '// KITE KID //', False],
[766, 'ATTACK', False],
[767, 'BRAG', False],
[768, 'REPAIR', False],
[774, "// KID'S KITE //", False],
[775, 'ATTACK', False],
[776, 'DO NOTHING', False],
[777, 'FLY', False],
[778, 'FLY 2', False],
[784, '// YE OLD SPROUT //', False],
[785, 'ROLL OVER', False],
[786, 'ROLL OVER (BOSS RUSH)', False],
[791, '//OMORI SOMETHING 1//', False],
[792, 'EMOTIONAL CONTROL', False],
[793, 'SOFT ATTACK', False],
[794, 'MEDIUM ATTACK', False],
[795, 'ENGULF', False],
[801, '// PLUTO //', False],
[802, 'DO NOTHING', False],
[803, 'HEADBUTT', False],
[804, 'BRAG', False],
[805, 'EXPAND', False],
[811, '// RIGHT ARM //', False],
[812, 'ATTACK', False],
[813, 'FLEX', False],
[814, 'GRAB', False],
[820, '// LEFT ARM //', False],
[821, 'ATTACK', False],
[822, 'FLEX', False],
[823, 'POKE', False],
[829, '// THE EARTH //', False],
[830, 'ATTACK', False],
[831, 'DO NOTHING', False],
[832, 'THE EARTH IS CRUEL', False],
[833, 'PROTECT THE WORLD', False],
[834, 'CRUEL (Epilouge)', False],
[835, 'PROTECT THE WORLD (Epilouge)', False],
[839, '// SPACE EX-BOYFRIEND //', False],
[840, 'ATTACK', False],
[841, 'DO NOTHING', False],
[842, 'ANGSTY SONG', False],
[843, 'ANGRY SONG', False],
[844, 'SPACE LASER', False],
[845, 'BULLET HELL', False],
[846, 'BULLET HELL (Epilouge)', False],
[851, '// DOWNLOAD WINDOW //', False],
[852, 'DO NOTHING', False],
[853, 'DO NOTHING 2', False],
[854, 'CRASH', False],
[860, '// Space Ex-Husband //', False],
[861, 'ATTACK', False],
[862, 'LASER', False],
[863, 'CALM DOWN', False],
[864, 'ANGRY SONG', False],
[865, 'ANGSTY SONG', False],
[866, 'JOYFUL SONG', False],
[867, 'SPINNING KICK', False],
[868, 'BULLET HELL', False],
[872, '// EVIL CHIP //', False],
[873, 'ATTACK', False],
[874, 'DO NOTHING', False],
[875, 'EVIL LAUGH', False],
[876, 'EVIL COOKIES', False],
[877, 'EVIL COOKIES HAPPY', False],
[882, '// UNBREAD TWINS //', False],
[883, 'ATTACK', False],
[884, 'DO NOTHING', False],
[885, 'STRESS EAT SETUP', False],
[886, 'BAKE BREAD', False],
[887, 'CHEER UP', False],
[888, 'STRESS EAT', False],
[889, 'COOK', False],
[890, 'BAKE BREAD (Epilouge)', False],
[893, '// KING CRAWLER //', False],
[894, 'ATTACK', False],
[895, 'DO NOTHING', False],
[896, 'CONSUME', False],
[897, 'CRUNCH', False],
[898, 'RAM', False],
[899, 'Consume Ally', False],
[900, 'Consume Recover', False],
[904, '// SPROUT MOLE LADDER //', False],
[905, 'DO NOTHING', False],
[906, 'SUMMON SPROUT MOLE', False],
[907, 'REPAIR', False],
[913, '// KING CARNIVORE //', False],
[914, 'ATTACK', False],
[915, 'DO NOTHING', False],
[916, 'SWEET GAS', False],
[922, '// ROOTS //', False],
[923, 'DO NOTHING', False],
[924, 'HEAL PLANT MONSTER', False],
[925, 'ATTACK', False],
[929, '// SHADY MOLE //', False],
[930, 'ATTACK', False],
[931, 'STEAL', False],
[932, 'B.E.D.', False],
[933, 'DYNAMITE', False],
[934, 'RUN AWAY', False],
[938, '// SIR MAXIMUS //', False],
[939, 'ATTACK', False],
[940, 'DO NOTHING', False],
[941, 'HIT TWICE', False],
[942, 'ULTIMATE ATTACK', False],
[943, 'ULTIMATE ATTACK x3 (Boss Rush)', False],
[944, 'ULTIMATE ATTACK x2 (Boss Rush)', False],
[945, 'ULTIMATE ATTACK x1 (Boss Rush)', False],
[948, '// SIR MAXIMUS II //', False],
[949, 'ATTACK', False],
[950, 'DO NOTHING', False],
[951, 'HIT TWICE', False],
[952, 'SPIN', False],
[953, 'ULTIMATE ATTACK', False],
[959, '// SIR MAXIMUS III //', False],
[960, 'ATTACK', False],
[961, 'DO NOTHING', False],
[962, 'HIT TWICE', False],
[963, 'SPIN', False],
[964, 'FLEX', False],
[965, 'ULTIMATE ATTACK', False],
[971, '// SWEET HEART //', False],
[972, 'ATTACK', False],
[973, 'SHARP INSULT', False],
[974, 'SWING MACE', False],
[975, 'BRAG', False],
[981, '// MR. JAWSUM //', False],
[982, 'SUMMON MINION', False],
[983, 'ATTACK ORDER', False],
[984, 'SUMMON MINION (BOSS RUSH)', False],
[989, '// PLUTO EXPANDED //', False],
[990, 'ATTACK', False],
[991, 'SUBMISSION HOLD', False],
[992, 'DO NOTHING', False],
[993, 'HEADBUTT', False],
[994, "EARTH'S FINALE", False],
[995, 'EXPAND FURTHER', False],
[996, 'EXPAND FURTHER FACE', False],
[997, 'EXPAND FURTHER CHEST', False],
[998, 'EXPAND FURTHER RIGHT', False],
[999, 'EXPAND FURTHER LEFT', False],
[1000, '// ABBI //', False],
[1001, 'ATTACK', False],
[1002, 'REVIVE TENTACLES', False],
[1004, 'ATTACK ORDER', False],
[1005, 'COUNTER TENTACLE SETUP', False],
[1012, '// ABBI TENTACLE //', False],
[1013, 'ATTACK', False],
[1014, 'WEAKEN', False],
[1015, 'GRAB', False],
[1016, 'GOOP', False],
[1022, '// ROBO HEART //', False],
[1023, 'ATTACK', False],
[1024, 'DO NOTHING', False],
[1025, 'LASER', False],
[1026, 'EXPLODE', False],
[1027, 'SNACK', False],
[1033, '// MUTANT HEART //', False],
[1034, 'ATTACK', False],
[1035, 'DO NOTHING', False],
[1036, 'HEAL', False],
[1037, 'WINK', False],
[1038, 'FLAIL ARMS', False],
[1039, 'CRY', False],
[1040, 'INSULT', False],
[1041, 'INSTAKILL', False],
[1043, '// PERFECT HEART //', False],
[1044, 'STEAL HEART', False],
[1045, 'STEAL BREATH', False],
[1046, 'ANGELIC WRATH', False],
[1047, 'EXPLOIT EMOTION', False],
[1048, 'SPARE', False],
[1049, 'ANGELIC VOICE', False],
[1058, '//SLIME GIRLS//', False],
[1059, 'COMBO ATTACK', False],
[1060, 'DO NOTHING', False],
[1061, 'STRANGE GAS', False],
[1062, 'DYNAMITE', False],
[1063, 'STING RAY', False],
[1064, 'SWAP ', False],
[1065, 'CHAIN SAW', False],
[1066, 'CHAIN SAW (BOSS RUSH)', False],
[1067, 'SLIME ULTIMATE ATTACK ', False],
[1070, '//HUMPHREY 1//', False],
[1071, 'ATTACK', False],
[1072, 'ATTACK x 2', False],
[1073, 'ATTACK x 3', False],
[1076, '//HUMPHREY 2//', False],
[1077, 'BASIC ATTACK', False],
[1078, 'CHOMP', False],
[1079, 'SWALLOW (BOSS RUSH)', False],
[1080, 'SWALLOW DAMAGE (BOSS RUSH)', False],
[1081, 'SWALLOW TRANSITION (BOSS RUSH)', False],
[1082, '//HUMPHREY 3//', False],
[1083, 'CHOMP', False],
[1084, 'DO NOTHING', False],
[1085, 'HEAL ', False],
[1086, 'POISON (LARGE)', False],
[1087, 'POISON (SMALL)', False],
[1088, 'SWALLOW', False],
[1089, 'SWALLOW DAMAGE', False],
[1090, 'SWALLOW TRANSITION', False],
[1091, '//HUMPHREY 4//', False],
[1092, 'DO NOTHING 1', False],
[1093, 'DO NOTHING 2', False],
[1094, 'DO NOTHING 3', False],
[1095, 'DO NOTHING 4', False],
[1096, 'DO NOTHING 5', False],
[1100, '//SOMETHING IN THE DARK//', False],
[1101, 'DO NOTHING 1', False],
[1102, 'DO NOTHING 2', False],
[1103, 'Dark Attack', False],
[1104, 'Final Attack', False],
[1107, '//SOMETHING IN THE WALLS //', False],
[1108, 'ATTACK', False],
[1109, 'DO NOTHING', False],
[1110, 'SUMMON BABY SPIDER', False],
[1111, 'SPIDER WEBS', False],
[1112, 'FINISH FIGHT', False],
[1117, '//BABY SPIDER//', False],
[1118, 'ATTACK', False],
[1119, 'DO NOTHING', False],
[1121, '//SOMETHING IN THE WATER//', False],
[1122, 'ATTACK', False],
[1123, 'DO NOTHING', False],
[1124, 'DRAG DOWN', False],
[1127, "// OMORI'S SOMETHING //", False],
[1128, 'ATTACK', False],
[1129, 'DO NOTHING', False],
[1130, 'ENGULF (Block)', False],
[1131, 'ENGULF (True)', False],
[1132, '//HANGING BODY//', False],
[1133, 'NOTHING 1', False],
[1134, 'NOTHING 2', False],
[1135, 'NOTHING 3', False],
[1136, 'NOTHING 4', False],
[1137, 'NOTHING 5', False],
[1138, 'NOTHING 6', False],
[1139, 'NOTHING 7', False],
[1140, 'NOTHING 8', False],
[1141, 'NOTHING 9', False],
[1142, 'NOTHING 10', False],
[1143, 'NOTHING 11', False],
[1144, 'NOTHING 12', False],
[1145, 'BLURRY NOTHING', False],
[1146, 'NOTHING WARNING', False],
[1147, '??? ATTACK', False],
[1148, '// OMORI //', False],
[1149, 'ATTACK', False],
[1150, 'OBSERVE', False],
[1151, 'SAD POEM', False],
[1152, 'HACK AWAY', False],
[1153, 'EXPLOIT ', False],
[1154, 'STAB', False],
[1155, 'TRIP', False],
[1156, 'FINAL STRIKE', False],
[1157, 'RED HANDS', False],
[1158, 'HIDE HUB', False],
[1160, '// AUBREY //', False],
[1161, 'ATTACK', False],
[1162, 'DO NOTHING', False],
[1163, 'HEADBUTT', False],
[1164, 'COUNTER ATTACK SETUP', False],
[1165, 'TAUNT', False],
[1166, 'COUNTER ATTACK SKILL', False],
[1171, '// THE HOOLIGANS //', False],
[1172, 'CHARLIE ATTACK', False],
[1173, 'ANGEL ATTACK', False],
[1174, 'MAVERICK CHARM', False],
[1175, 'KIM HEADBUTT', False],
[1176, 'VANCE CANDY', False],
[1177, 'GROUP ATTACK', False],
[1182, '// BASIL //', False],
[1183, 'ATTACK', False],
[1184, 'DO NOTHING', False],
[1185, 'PREMPTIVE STRIKE', False],
[1191, '// CHARLIE //', False],
[1192, 'RELUCTANT ATTACK', False],
[1193, 'DO NOTHING', False],
[1194, 'LEAVE', False],
[1200, '// ANGEL //', False],
[1201, 'ATTACK', False],
[1202, 'DO NOTHING', False],
[1203, 'QUICK ATTACK', False],
[1204, 'TEASE', False],
[1210, '// THE MAVERICK //', False],
[1211, 'ATTACK', False],
[1212, 'DO NOTHING', False],
[1213, 'SMILE', False],
[1214, 'TAUNT', False],
[1220, '// KIM //', False],
[1221, 'ATTACK', False],
[1222, 'DO NOTHING', False],
[1223, 'SMASH', False],
[1224, 'TAUNT', False],
[1230, '// VANCE //', False],
[1231, 'ATTACK', False],
[1232, 'DO NOTHING', False],
[1233, 'CANDY', False],
[1234, 'TEASE', False],
[1240, '// JACKSON //', False],
[1241, 'WALK SLOWLY', False],
[1242, 'AUTO KILL', False],
[1249, '// RECYCLEPATH //', False],
[1250, 'ATTACK', False],
[1251, 'SUMMON MINION', False],
[1252, 'FLING TRASH', False],
[1253, 'GATHER TRASH', False],
[1259, '//CLOSET SOMETHING//', False],
[1260, 'CLOSET ATTACK', False],
[1261, 'DO NOTHING', False],
[1262, 'MAKE AFRAID', False],
[1263, 'MAKE WEAK', False],
[1269, '//BACKGROUND ACTORS//', False],
[1270, '//BERLY//', False],
[1271, 'BERLY ATTACK', False],
[1272, 'BERLY NOTHING 1', False],
[1273, 'BERLY NOTHING 2', False],
[1279, "// BASIL'S SOMETHING //", False],
[1280, 'SOMETHING SET UP PLAYER', False],
[1281, 'BASIL ATTACK PLAYER', False],
[1282, 'BASIL ATTACK BASIL', False],
[1287, 'SHADOW BASIL ATTACK', False],
[1288, '//PLAYER SOMETHING// ', False],
[1289, 'INCREASE STRESS', False],
[1297, '//RABBIT//', False],
[1298, 'ATTACK', False],
[1299, 'DO NOTHING', False],
[1300, 'BE CUTE', False],
[1301, 'SAD EYES', False],
[1306, '//CUP CAKE BUNNY//', False],
[1307, 'ATTACK', False],
[1308, 'DO NOTHING', False],
[1309, 'SPRINKLES', False],
[1313, '//MILKSHAKE BUNNY//', False],
[1314, 'ATTACK', False],
[1315, 'DO NOTHING', False],
[1316, 'SHAKE', False],
[1320, '//PANCAKE BUNNY//', False],
[1321, 'ATTACK', False],
[1322, 'DO NOTHING', False],
[1326, '//STRAWBERRY SHORT SNAKE//', False],
[1327, 'ATTACK', False],
[1328, 'DO NOTHING', False],
[1329, 'SLITHER', False],
[1333, '//GHOST BUNNY//', False],
[1334, 'ATTACK', False],
[1335, 'DO NOTHING', False],
[1339, '//TOAST GHOST//', False],
[1340, 'ATTACK ', False],
[1341, 'DO NOTHING', False],
[1345, '//SPROUT BUNNY//', False],
[1346, 'ATTACK', False],
[1347, 'DO NOTHING', False],
[1348, 'FEED', False],
[1351, '//CELERY//', False],
[1352, 'ATTACK', False],
[1353, 'DO NOTHING', False],
[1357, '//CILANTRO//', False],
[1358, 'ATTACK', False],
[1359, 'DO NOTHING', False],
[1360, 'GARNISH', False],
[1364, '//GINGER//', False],
[1365, 'ATTACK', False],
[1366, 'DO NOTHING', False],
[1367, 'SOOTHE', False],
[1371, '//BIG STRONG TREE//', False],
[1372, 'DO NOTHING', False],
[1373, 'DO NOTHING', False],
[1377, '//BEE//', False],
[1378, 'ATTACK', False],
[1379, 'DO NOTHING', False],
[1380, 'STING', False],
[1384, '//SINGLE HUMPHREY// ', False],
[1385, 'ATTACK', False],
[1386, 'BITE', False],
[1390, '// BOSS //', False],
[1391, 'ATTACK', False],
[1392, 'ATTACK TWICE', False],
[1393, 'DO NOTHING', False],
[1395, 'ATTACK ALL', False],
[1397, '// LIFE JAM GUY //', False],
[1398, 'DEATH JAM', False],
[1399, 'DO NOTHING', False],
[1413, '//Fear extra battles//', False],
[1414, '// HEIGHTS //', False],
[1415, 'ATTACK ', False],
[1416, 'DO NOTHING', False],
[1417, 'REDUCE ATTACK ALL', False],
[1418, 'DEFENCE UP', False],
[1419, 'SHOVE', False],
[1422, '// SPIDERS //', False],
[1423, 'ATTACK', False],
[1424, 'DO NOTHING', False],
[1425, 'SPIN WEB', False],
[1426, 'ATTACK ALL', False],
[1430, '// DROWNING //', False],
[1431, 'ATTACK', False],
[1432, 'DO NOTHING', False],
[1433, 'DRAG DOWN', False],
[1434, 'WHIRLPOOL', False],
[1435, 'DROWNING SMALL', False],
[1436, 'DROWNING MEDIUM', False],
[1437, 'DROWNING BIG', False],
[1440, '//REFIGHT REWARD SKILLS//', False],
[1441, 'VERTIGO', False],
[1442, 'CRIPPLE', False],
[1443, 'SUFFOCATE', False],
[1444, '//BROKEN FEAR SKILLS//', False],
[1445, 'CALM DOWN', False],
[1446, 'FOCUS', False],
[1447, 'PERSIST', False],
[1448, 'RED HAND ATTACK', False],
[1449, 'HAIR ATTACK', False],
[1450, 'MARI ATTACK', False],
[1451, 'FINAL ATTACK', False],
[1459, '//FINAL BATTLE//', False],
[1460, 'ALLEGRO', False],
[1461, 'CHERISH', False],
[1462, 'ENCORE', False],
[1470, '//EPILOUGE EXTRA SKILLS//', False],
[1471, 'PLUTO METEOR', False]]

msg_dict = {}

def randomSelect():

    try:
        while True:
            randSelectList = random.randint(0, 2)
            if randSelectList == 0:
                randList = itemlist
            elif randSelectList == 1:
                randList = weaponlist
            elif randSelectList == 2:
                randList = armorlist

            randSelectInner = random.randint(0, len(randList) - 1)
            if randSelectList == 1:
                if randList[randSelectInner][2] == False:
                    randList[randSelectInner][2] = True
                    break
            else:
                break

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

    return (randList[randSelectInner][0], randList[randSelectInner][1] ,randSelectList)

    

def randomizePrice(jsonFile, randopath):

    try:
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

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

def closeWindow():
    window.destroy()

def randoButton_Click(itemrando, skillrando, inventoryrando, learnedrando):

    try:

        config = configparser.ConfigParser()
        config['rando'] = {}

        if learnedrando:
            config['rando']['learnedrando'] = 'true'
        else:
            config['rando']['learnedrando'] = 'false'
        if inventoryrando:
            config['rando']['inventoryrando'] = 'true'
        else:
            config['rando']['inventoryrando'] = 'false'

        if values['folderinput'] != "":
            fileTuple = Main()
            file_list = fileTuple[0]
            yaml_list = fileTuple[1]
            randoBool = False
            melonSkillList = []

            with open(os.path.join(paths.randopath, "Map002.json"), encoding='utf-8') as file:
                data = json.load(file)
                for event in data['events']:
                    if event != None:
                        if event['id'] in [88, 90, 91, 92, 93, 94]:
                            del event['pages'][0]['list'][-6:-1]

            with open(os.path.join(paths.randopath, "Map002.json"), mode='w', encoding='utf-8') as updatedFile:
                json.dump(data, updatedFile)

            if itemrando:
                randomizeItems(file_list)
                if not randoBool:
                    randoBool = True
            if skillrando:
                skillTuple = randomizePlayerSkills(config)
                melonSkillList = skillTuple[0]
                config = skillTuple[1]
                randomizeWepSkillLoc(melonSkillList)
            else:
                randomizeWepSkillLoc()
            if randoBool:
                updateYamlMsgs(yaml_list)

            with open('randoConfig.ini', 'w') as configFile:
                config.write(configFile)

            progress_text.update('Randomization Complete!')
            close_button(disabled=False)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')


def edit_yaml_value(y, splitList, itemName):

    try:

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
    
    except Exception:
        valueType, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {valueType}, {value}, {traceback.tb_lineno}')

def edit_yaml(y):

    try:

        for msg, itemName in msg_dict.items():
            splitList = msg.split(".")
            yam = f'{splitList[0]}.yaml'
            if y == yam:
                data = edit_yaml_value(y, splitList, itemName)
                if data != None:
                    with open(os.path.join(paths.yamlrandopath, y), 'w', encoding='utf-8') as updatedYaml:
                        yaml.dump(data, updatedYaml)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

    return f'{y} updated!'

def randomize_map_data(file):

    try:

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
                                                nextLastMsg = lastMsg
                                                lastMsg = item['parameters'][0].split(" ")[1]
                                                if (toYamlCounter <= 2 and lastItemName != ""):
                                                    if lastMsg not in msg_dict.keys():
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
                                                    if (lastMsg != "" and lastMsg not in msg_dict.keys() and toYamlCounter <= 2):
                                                        msg_dict[lastMsg] = lastItemName                                                                                                                                                                        
                                        elif item['code'] == 127:
                                            if item['parameters'][1] == 0:
                                                if item['parameters'][0] not in [2, 10, 11, 12, 14, 61, 110, 113]:
                                                    itemID, itemName, listType = randomSelect()
                                                    if listType == 0:
                                                        item['code'] = 126
                                                    elif listType == 2:
                                                        item['code'] = 128
                                                    item['parameters'][0] = itemID
                                                    lastItemName = itemName
                                                    toYamlCounter += 1
                                                    if (lastMsg != "" and lastMsg not in msg_dict.keys() and toYamlCounter <= 2):
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
                                                if (lastMsg != "" and lastMsg not in msg_dict.keys() and toYamlCounter <= 2):                                                    
                                                    msg_dict[lastMsg] = lastItemName
                                                elif lastMsg == "sidequest_dreamworld_rabbitkiller.message_16":
                                                        msg_dict[nextLastMsg] = lastItemName
                                        elif item['code'] in [302, 605]:
                                            if event['id'] == 71:
                                                if item['code'] == 302:
                                                    continue
                                            if not any(item['parameters'][1] in i for i in keyitemlist):
                                                itemID, itemName, listType = randomSelect()
                                                if listType == 1:
                                                    item['parameters'][0] = 1
                                                elif listType == 2:
                                                    item['parameters'][0] = 2
                                                item['parameters'][1] = itemID
                                                item['parameters'][2] = 0
                                                toYamlCounter += 1

                with open(os.path.join(paths.randopath, file), mode="w", encoding="utf-8") as updatedFile:
                    json.dump(data, updatedFile)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')
    
    return f'{file} randomized!'

def browse_files():

    try:

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

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

def Main():

    try:

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
            
    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

    return (file_list, yaml_list)

def randomizeItems(file_list):

    try:

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
                    toYamlCounter = 0
                    lastItemName = ""
                    lastMsg = ""
                    for item in event['list']:
                        if item['code'] == 356:
                            if item['parameters'][0].startswith("ShowMessage "):
                                nextLastMsg = lastMsg
                                lastMsg = item['parameters'][0].split(" ")[1]
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
                                    if (lastMsg != "" and lastMsg not in msg_dict.keys()):
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
                                    if (lastMsg != "" and lastMsg not in msg_dict.keys()):
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
                                if (lastMsg != "" and lastMsg not in msg_dict.keys()):
                                    msg_dict[lastMsg] = lastItemName 
                        elif item['code'] in [302, 605]:
                            itemID, itemName, listType = randomSelect()
                            if listType == 1:
                                item['parameters'][0] = 1
                            elif listType == 2:
                                item['parameters'][0] = 2
                            item['parameters'][1] = itemID
                            item['parameters'][2] = 0

        with open(os.path.join(paths.randopath, 'CommonEvents.json'), mode='w', encoding='utf-8') as updatedEventFile:
            json.dump(data, updatedEventFile)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

def updateYamlMsgs(yaml_list):

    try:

        executor = ThreadPoolExecutor()
        results = executor.map(edit_yaml, yaml_list)

        for result in results:
            print(result)        

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

    return (yaml_list)

def randomizePlayerSkills(config):

    try:

        melonSkillList = [[180, "ShowMessage XX_OCEAN.message_531"],
        [181, "ShowMessage XX_OCEAN.message_532"],
        [182, "ShowMessage XX_OCEAN.message_533"],
        [183, "ShowMessage XX_OCEAN.message_534"],
        [184, "ShowMessage XX_OCEAN.message_535"],
        [185, "ShowMessage XX_OCEAN.message_536"]]

        quickActorDict = {1: "OMORI", 2: "AUBREY", 3: "KEL", 4: "HERO"}

        with open(os.path.join(paths.yamlrandopath, "XX_OCEAN.yaml"), encoding='utf-8') as yamlFile:
            data = yaml.safe_load(yamlFile)
            for x in range(6):
                randActor = random.randint(1, 4)

                while True:
                    randSelectInner = random.randint(0, len(playerSkillList) - 1)
                    randSkillId = playerSkillList[randSelectInner][0]
                    
                    if playerSkillList[randSelectInner][2] == False:
                        playerSkillList[randSelectInner][2] = True
                        break

                melonSkillList[x].append(randActor)
                melonSkillList[x].append(randSkillId)
                
                forbiddenSkillList = [2, 46, 49, 52, 86, 89, 92, 126, 129, 132, 168, 171, 174]

                splitList = melonSkillList[x][1].split(".")
                data[splitList[1]]['text'] = f"{quickActorDict[randActor]} learned \c[1]{playerSkillList[randSelectInner][1]}\c[0]!"
        
        with open(os.path.join(paths.yamlrandopath, "XX_OCEAN.yaml"), mode='w', encoding='utf-8') as updatedYaml:
            yaml.dump(data, updatedYaml)

        #TODO: Pluto(Map124), Man on Fire(Map332), Gator Guy sculptor(Map197), Berly(Map92), Shawn(Map490), Fears(Maps 440, 441, 443), Red Hand(Map87) skill rando logic here!

        characterSkillList = [["Map124.json", 12, "pluto.yaml", "message_142"], ["Map332.json", 3, "dreamworld_npc_dialogue_orangeoasis.yaml", "message_12"],
        ["Map197.json", 43, "art_sculpture.yaml", "message_112"], ["Map092.json", 25, "dreamworld_npc_dialogue_playground.yaml", "message_86"],
        ["Map490.json", 2, "dreamworld_npc_dialogue_playground.yaml", "message_21"], ["Map440.json", 8, "XX_MELON.yaml", "message_815"],
        ["Map441.json", 51, "XX_MELON.yaml", "message_814"], ["Map443.json", 4, "XX_MELON.yaml", "message_816"], ["Map087.json", 14, "01_map_whitespace.yaml", "message_125"]]

        for l in characterSkillList:
            l = randomizeCharacterSkills(l, quickActorDict)

            with open(os.path.join(paths.yamlrandopath, l[2]), encoding='utf-8') as yamlFile:
                data = yaml.safe_load(yamlFile)
                data[l[3]]['text'] = f"{l[4]} learned \c[1]{l[5]}\c[0]!"

            with open(os.path.join(paths.yamlrandopath, l[2]), mode='w', encoding='utf-8') as updatedYaml:
                yaml.dump(data, updatedYaml)

        with open(os.path.join(paths.randopath, "Classes.json"), encoding='utf-8') as file:
            data = json.load(file)
            for cls in data:
                if cls != None:
                    if cls['id'] in (1, 2, 3, 4):
                        config[quickActorDict[cls['id']]] = {}
                        for skill in cls['learnings']:
                            if skill['skillId'] not in forbiddenSkillList:
                                while True:
                                    randSelectInner = random.randint(0, len(playerSkillList) - 1)
                                    randSkillId = playerSkillList[randSelectInner][0]
                                    
                                    if playerSkillList[randSelectInner][2] == False:
                                        playerSkillList[randSelectInner][2] = True
                                        break
                                
                                skill['skillId'] = randSkillId
                                if skill['level'] in [1, 2, 3]:
                                    skillstr = f"skill{skill['skillId']}"
                                    config[quickActorDict[cls['id']]][skillstr] = str(skill['skillId'])

        with open(os.path.join(paths.randopath, "Classes.json"), mode='w', encoding='utf-8') as updatedFile:
            json.dump(data, updatedFile)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

    return (melonSkillList, config)

def randomizeCharacterSkills(l, quickActorDict):
    with open(os.path.join(paths.randopath, l[0]), encoding='utf-8') as file:
                data = json.load(file)
                for event in data['events']:
                    if event != None:
                        if event['id'] == l[1]:
                            for page in event['pages']:
                                for item in page['list']:
                                    if item['code'] == 318:
                                        randActor = random.randint(1, 4)

                                        while True:
                                            randSelectInner = random.randint(0, len(playerSkillList) - 1)
                                            randSkillId = playerSkillList[randSelectInner][0]
                                            
                                            if playerSkillList[randSelectInner][2] == False:
                                                playerSkillList[randSelectInner][2] = True
                                                break

                                        item['parameters'][1] = randActor
                                        item['parameters'][3] = randSkillId

                                        l.append(quickActorDict[randActor])
                                        l.append(playerSkillList[randSelectInner][1])

                                        with open(os.path.join(paths.randopath, l[0]), mode='w', encoding='utf-8') as updatedFile:
                                            json.dump(data, updatedFile)

                                        return l

def randomizeWepSkillLoc(melonSkillList = []):

    try:
        # randoSkillBool variables are 180-185
        # Possible melon IDs are 1-115
        ifLogicProperty = {"code": 111, "indent": 0, "parameters": [1, 180, 0, 0, 0]}
        itemGetProperty = {"code": 122, "indent": 1, "parameters": [830, 830, 0, 0, 0]}
        frameWaitProperty = {"code": 230, "indent": 1, "parameters": [20]}
        yamlMsgProperty = {"code": 356, "indent": 1, "parameters": ["ShowMessage XX_OCEAN.message_536"]}
        skillGetCEProperty = {"code": 117, "indent": 1, "parameters": [304]}
        skillProperty = {"code": 318, "indent": 1, "parameters": [0, 3, 0, 112]}
        boolSetProperty = {"code": 122, "indent": 0, "parameters": [180, 180, 0, 0, 1]}
        emptyEventProperty = {"code": 0, "indent": 0, "parameters": []}

        idList = randSelectMelons()

        if not melonSkillList:
            melonSkillList = [[180, "ShowMessage XX_OCEAN.message_531", 4, 152, idList[0]],
            [181, "ShowMessage XX_OCEAN.message_532", 4, 150, idList[1]],
            [182, "ShowMessage XX_OCEAN.message_533", 4, 151, idList[2]],
            [183, "ShowMessage XX_OCEAN.message_534", 4, 159, idList[3]],
            [184, "ShowMessage XX_OCEAN.message_535", 3, 110, idList[4]],
            [185, "ShowMessage XX_OCEAN.message_536", 3, 112, idList[5]]]
        else:
            for x in range(6):
                melonSkillList[x].append(idList[x])

        with open(os.path.join(paths.randopath, "Map002.json"), encoding='utf-8') as file:
            data = json.load(file)
            for event in data['events']:
                if event != None:
                    if event['id'] in idList:
                        for l in melonSkillList:
                            if event['id'] == l[4]:
                                ifLogicCopy = copy.deepcopy(ifLogicProperty)
                                yamlMsgCopy = copy.deepcopy(yamlMsgProperty)
                                skillCopy = copy.deepcopy(skillProperty)
                                boolSetCopy = copy.deepcopy(boolSetProperty)
                                ifLogicCopy['parameters'][1] = l[0]
                                yamlMsgCopy['parameters'][0] = l[1]
                                skillCopy['parameters'][1] = l[2]
                                skillCopy['parameters'][3] = l[3]
                                boolSetCopy['parameters'][0] = l[0]
                                boolSetCopy['parameters'][1] = l[0]
                                event['pages'][0]['list'].append(ifLogicCopy)
                                event['pages'][0]['list'].append(itemGetProperty)
                                event['pages'][0]['list'].append(frameWaitProperty)
                                event['pages'][0]['list'].append(yamlMsgCopy)
                                event['pages'][0]['list'].append(skillGetCEProperty) 
                                event['pages'][0]['list'].append(skillCopy)
                                event['pages'][0]['list'].append(boolSetCopy)
                                event['pages'][0]['list'].append(emptyEventProperty)

        with open(os.path.join(paths.randopath, "Map002.json"), mode='w', encoding='utf-8') as updatedFile:
            json.dump(data, updatedFile)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')

def randSelectMelons():

    try:
        idList = []
        
        for x in range(6):
            id = random.randint(1, 115)
            idList.append(id)

    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')
    
    return idList

if __name__ == '__main__':

    try:
        paths = PathStrings()

        sg.theme('DarkPurple')

        layout = [  [sg.InputText(default_text=os.getcwd(), key='folderinput'), sg.Button('Browse')],
                    [sg.Button('Randomize!', key='randobutton'), sg.Checkbox('Randomize Items/Weapons/Charms', key='itemrando', default=True),
                    sg.Checkbox('Randomize Party Skills', key='skillrando', enable_events=True)],
                    [sg.Checkbox('Randomize Inventory on Load*', key='inventoryrando'),
                    sg.Checkbox('Randomize Already Learned Skills on Load*', key='learnedrando', disabled=True)],
                    [sg.Text('', key='progtext')],
                    [sg.Button('Close', key='closebutton'), sg.Text('*Only happens on first load')] ]
        
        window = sg.Window('OMORI Randomizer v0.15.3a', layout, finalize=True)
        progress_text = window['progtext']
        folder_field = window['folderinput']
        randomize_button = window['randobutton']
        close_button = window['closebutton']
        learned_checkbox = window['learnedrando']

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'closebutton':
                break
            if event == 'Browse':
                browse_files()
            if event == 'skillrando':
                if values['skillrando'] == True:
                    learned_checkbox(disabled=False)
                else:
                    learned_checkbox(disabled=True)
                    window['learnedrando'].update(False)
            if event == 'randobutton':
                itemrando = values['itemrando']
                skillrando = values['skillrando']
                inventoryrando = values['inventoryrando']
                learnedrando = values['learnedrando']
                progress_text.update("Randomizing data. Please wait...")
                window.Refresh()
                randoButton_Click(itemrando, skillrando, inventoryrando, learnedrando)
            

        window.close()

    except Exception:
            type, value, traceback = sys.exc_info()
            print(f'This error occurred during randomization, {type}, {value}, {traceback.tb_lineno}')
    
    