(function() {//causes this function to run immediately

    
    Scene_OmoriFile.prototype.loadGame = function() {
        if (DataManager.loadGame(this.savefileId())) {//loads save into memory so u can edit it
        
            //put randomization code here
            console.log('lol');
            $gameParty.changeWorldItemContainer(1);

            const itemlist = [[13, 'TOFU', 0],
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

            const keyitemlist = [[2, 'COLD STEAK', 5],
            [3, 'MICROWAVED STEAK', 5],
            [111, 'BIG BAG OF CANDY', 0],
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

            const weaponlist = [[2, 'SHINY KNIFE'],
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

            const armorlist = [[2, '"GOLD" WATCH'],
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

            function getRandom() {
                return Math.floor(Math.random() * 3);
            }

            function getRandomInt(max) {
                min = Math.ceil(0);
                max = Math.floor(max);
                return Math.floor(Math.random() * (max - min) + min);
            }

            function parseINIString(data){
                var regex = {
                    section: /^\s*\[\s*([^\]]*)\s*\]\s*$/,
                    param: /^\s*([^=]+?)\s*=\s*(.*?)\s*$/,
                    comment: /^\s*;.*$/
                };
                var value = {};
                var lines = data.split(/[\r\n]+/);
                var section = null;
                lines.forEach(function(line){
                    if(regex.comment.test(line)){
                        return;
                    }else if(regex.param.test(line)){
                        var match = line.match(regex.param);
                        if(section){
                            value[section][match[1]] = match[2];
                        }else{
                            value[match[1]] = match[2];
                        }
                    }else if(regex.section.test(line)){
                        var match = line.match(regex.section);
                        value[match[1]] = {};
                        section = match[1];
                    }else if(line.length == 0 && section){
                        section = null;
                    };
                });
                return value;
            }

            var fs = require("fs");

            const path = require("path");
            const base = path.dirname(process.mainModule.filename);
            var config = base.concat("/mods/randomizeralpha/randoConfig.ini");

            var data = fs.readFileSync(config, 'utf8');

            var configFile = parseINIString(data)

            if(!$gameSystem.randomized) {
                if(configFile['rando']['inventoryrando'] == 'true'){
                    $gameParty.initAllItems();
                    $gameParty.loseItem($dataWeapons[28], 1, true);
                    $gameParty.loseItem($dataWeapons[45], 1, true);
                    $gameParty.loseItem($dataArmors[50], 1, true);

                    randList = [];

                    for(let i = 0; i < 3; i++){
                        listType = getRandom();
                        if(listType == 0){
                            randList = itemlist;
                        }
                        else if(listType == 1){
                            randList = weaponlist;
                        }
                        else{
                            randList = armorlist;
                        }
                        randSelect = getRandomInt(randList.length);
                        randSelectInner = randList[randSelect][0]

                        if(listType == 0){
                            $gameParty.gainItem($dataItems[randSelectInner], 1);
                        }
                        else if(listType == 1){
                            $gameParty.gainItem($dataWeapons[randSelectInner], 1);
                        }
                        else{
                            $gameParty.gainItem($dataArmors[randSelectInner], 1);
                        }
                    }
                }

                if(configFile['rando']['learnedrando'] == 'true'){
                    $gameActors.actor(1).unequipSkill(0)
                    $gameActors.actor(1).unequipSkill(2)
                    $gameActors.actor(1).forgetSkill(26)
                    $gameActors.actor(1).forgetSkill(27)

                    $gameActors.actor(2).unequipSkill(0)
                    $gameActors.actor(2).forgetSkill(68)

                    $gameActors.actor(3).unequipSkill(0)
                    $gameActors.actor(3).forgetSkill(107)
                    
                    $gameActors.actor(4).unequipSkill(0)
                    $gameActors.actor(4).unequipSkill(2)
                    $gameActors.actor(4).forgetSkill(147)
                    $gameActors.actor(4).forgetSkill(148)


                    for (const [key, value] of Object.entries(configFile['OMORI'])){
                        $gameActors.actor(1).learnSkill(value)
                    }
                    for (const [key, value] of Object.entries(configFile['AUBREY'])){
                        $gameActors.actor(2).learnSkill(value)
                    }
                    for (const [key, value] of Object.entries(configFile['KEL'])){
                        $gameActors.actor(3).learnSkill(value)
                    }
                    for (const [key, value] of Object.entries(configFile['HERO'])){
                        $gameActors.actor(4).learnSkill(value)
                    }
                }

                $gameSystem.randomized = true;
            }

            

            SoundManager.playLoad();
            this.fadeOutAll();
            // Reload Map if Updated
            if ($gameSystem.versionId() !== $dataSystem.versionId) {
                $gamePlayer.reserveTransfer($gameMap.mapId(), $gamePlayer.x, $gamePlayer.y);
                $gamePlayer.requestMapReload();
            };
            SceneManager.goto(Scene_Map);
            var info = DataManager.loadSavefileInfo(this.savefileId());
            $gameSystem.saveName = info.saveName;
            this._loadSuccess = true;
            // Close Prompt Window
            this._promptWindow.close();
            this._promptWindow.deactivate();
        } else {
            // Play Buzzer
            SoundManager.playBuzzer();
            // Close Prompt Window
            this._promptWindow.close();
            this._promptWindow.deactivate();
            // Set Can select Flag to true
            this._canSelect = true;
        }
    };

})();//causes this function to run immediately

