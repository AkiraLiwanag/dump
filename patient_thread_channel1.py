import threading
import random
import time
import datetime

def random_function():
    ct = datetime.datetime.now()
    print(ct)
    life = ["Live", "Not Operand"]
    operand = random.sample(life, 1)
    print(operand)
    localities = ["global", "local"]
    locality = random.sample(localities, 1)
    print(locality)
    cases = ["single case", "multiple case", "mass case"]
    case = random.sample(cases, 1)
    print(case)
    print()
    letters1 = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    letters2 = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    letters3 = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    letters4 = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    letters5 = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    letter1 = random.sample(letters1, 1)
    letter2 = random.sample(letters2, 1)
    letter3 = random.sample(letters3, 1)
    letter4 = random.sample(letters4, 1)
    letter5 = random.sample(letters5, 1)
    value = (round(random.random()*9999999999,10))
    values = "value:"
    print(values, letter1, letter2, letter3, letter4, letter5, value)
    print()
    time.sleep(0)
    nano  = ["Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen Of Hearts", "King of Hearts", "Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen Of Clubs", "King of Clubs", "Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen Of Diamonds", "King of Diamonds", "Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen Of Spades", "King of Spades", "Joker", "Joker", "empty bottle", "bottle of wine", "wine glass", "bottle of iced tea", "energy drink", "lemon juice", "pack of green peas", "shirt", "bed", "headphones", "earphones", "blanket", "tablet", "kindle", "pills", "pack of coffee beans", "cup of coffee", "junkfood", "medicine", "spoon", "fork", "Nintendo Switch", "laptop", "mobile phone", "electric fan", "chair", "guitar", "keyboard", "piano", "tv", "monitor", "oil", "hashish", "marijuana", "cigarette", "vape", "pillow", "dog food", "bike", "car", "scooter", "skateboard", "printer", "shards of glass", "garbage", "strips of sleather", "food", "bottle of water", "bible", "Dhammapada", "yoga mat", "helmet", "chewing gum", "vitamins", "shirt", "sweater", "pants", "working pants", "skirt", "underwear", "parachute", "gun", "knife", "sword", "katana", "oatmeal", "chain", "slippers", "shoes", "book", "wires", "credit card", "stove", "oven", "hat", "bucket hat", "baseball cap", "beanie", "hoodie", "necklace", "ring", "gold ring", "diamond ring", "diamond", "diamonds", "painting", "pencil", "ballpoint pen", "sketchpad", "crayon", "box of crayons", "paint", "spray paint", "fruit", "lettuce", "carrot", "watermelon", "orange", "apple", "banana", "pear", "gold", "gold bar", "pistol", "lantern", "lamp", "umbrella", "newspaper", "Sega", "ecstasy", "Nintendo 64", "calculator", "brownies", "pie", "loaf bread", "aviator shades", "shutter shades", "CD", "floppy disk", "mp3 player", "walkman", "cassette", "ticket", "food stub", "ski mask", "spear", "nunchucks", "frying pan", "beans", "charger", "guitar pick", "mic", "digicam", "GoPro", "night vision goggles", "sniper rifle", "DS4 Playstation controller", "CDJ", "Raybans", "smartwatch", "modem", "axe", "Canada", "Sweden", "China", "Beijing", "New York", "California", "L.A.", "San Francisco", "Detroit", "Colorado", "Newark", "New Jersey", "Australia", "Gold Coast", "Thailand", "North Korea", "Pyongyang", "Seoul", "Tokyo", "Osaka", "Japan", "Fujian", "Kyoto", "Manila", "Palawan", "Siargao", "Sultan Kudarat", "Davao", "Sydney", "Poland", "Uzbekistan", "Kyrgystan", "Turkey", "Iraq", "Iran", "Bolivia", "Iceland", "Lithuania", "Greenland", "UK", "France", "Spain", "Rome", "Greece", "Amsterdam", "Netherlands", "Boracay", "Indonesia", "Russia", "Ukraine", "Africa", "Antarctica", "Alaska", "South Carolina", "North Carolina", "Philadelphia", "Brooklyn", "Mexico", "Brazil", "Taiwan", "Burma", "Cambodia", "Vietnam", "India", "Bangladesh", "New Delhi", "Bombay", "Philippines", "Africa and African America", "Aikido", "Animal and Imitative Systems in Chinese Martial Arts", "Archery, Japanese", "Baguazhang (Pa Kua Ch' uan)", "Boxing, Chinese", "Boxing, Chinese Shaolin Styles", "Boxing, European", "Brazilian Jiu Jitsu", "Budo, Bujutsu, and Bugei", "Capoeira", "China", "Chivalry", "Combatives: Military and Police Martial Art Training", "Dueling", "Europe", "External vs. Internal Chinese Martial Arts", "Folklore in the Martial Arts", "Form/Xing/Kata/Pattern Practice", "Gladiators", "Gunfighters","Hapkido", "Heralds", "Iaido", "India", "Japan", "Japanese Martial Arts, Chinese Influences on", "Jeet Kune Do", "Judo", "Kajukenbo", "Kalarippayattu", "Karate, Japanese", "Karate, Okinawan", "Kendo", "Kenpo", "Ki/Qi", "Knights", "Kobudo, Okinawan", "Korea", "Korean Martial Arts, Chinese Influences On", "Koryu Bugei, Japanese", "Krav Maga", "Kung Fu/Gungfu/Gongfu", "Masters of Defense", "Medicine, Traditional Chinese", "Meditation", "Middle East", "Mongolia", "Muay Thai", "Ninjutsu", "Okinawa", "Orders of Knighthood, Secular", "Pacific Islands", "Pankration", "Performing Arts", "Philippines", "Political Conflict and the Martial Arts", "Rank", "Religion and Spiritual Development: Ancient Mediterranean and Medieval West", "Religion and Spiritual Development: China", "Religion and Spiritual Development: India", "Religion and Spiritual Development: Japan", "Sambo", "Samurai", "Savate", "Silat", "Social Uses of the Martial Arts", "Southeast Asia", "Stage Combat", "Stickfighting, Non-Asian", "Sword, Japanese", "Swordsmanship, European Medieval", "Swordsmanship, European Renaissance", "Swordsmanship, Japanese", "Swordsmanship, Korean/Hankuk Haedong Kumdo", "T'aek'kyon", "Taekwondo", "Taijiquan (Tai Chi Ch'uan)", "Thaing", "Thang-Ta", "Training Area", "Varma Ati", "Vovinam/Viet Vo Dao", "Warrior Monks, Japanese/Sohei", "Women in the Martial Arts", "Women in the Martial Arts: Britain and North America", "Women in the Martial Arts: China", "Women in the Martial Arts: Japan", "Wrestling and Grappling: China", "Wrestling and Grappling: Europe", "Wrestilng and Grappling: India", "Wrestling and Grappling: Japan", "Wrestling, Professional", "Written Texts: China", "Written Texts: India", "Written Texts: Japan", "Xingyiquan (Hsing I Ch'uan)", "Yongchun/Wing Chun", "Backside 180", "Backside 360", "Backside Caballerial", "Backside Half Cab", "Fakie Ollie", "Frontside 180", "Frontside 360", "Frontside Caballerial", "Frontside Half Cab", "Kickturn", "Nollie", "Nollie Backside 180", "Nollie Backside 360", "Nollie Frontside 180", "Nollie Frontside 360", "Ollie", "Ollie North", "Ollie South", "Switch Backside 180", "Switch Backside 360", "Switch Frontside 180", "Switch Frontside 360", "Switch Ollie", "Tic-Tac", "360 Flip", "360 Hardflip", "360 Ollie Heelflip", "360 Ollie Kickflip", "360 Pop Shove-it", "360 Shuvit", "540 Flip", "720 Flip", "Alpha Flip", "Anti Casper Flip", "Backside Bigspin", "Backside Flip", "Backside Half Cab Heelflip", "Backside Half Cab Kickflip", "Backside Heelflip", "Backside Kickflip", "Big Heelflip", "Bigflip", "Biggerflip", "Biggerspin", "Bigspin", "Bubble Flip", "Bullflip", "Caballerial Flip", "Camel Flip", "Casper Flip", "Daydream Flip", "De Comply", "Disco Flip", "Double Heelflip", "Double Kickflip", "Dragon Flip", "Fakie 360 Flip", "Fakie 360 Hardflip", "Fakie Backside Bigspin", "Fakie Backside Pop Shove-it", "Fakie Frontside Bigspin", "Fakie Frontside Pop Shove-it", "Fakie Hardflip", "Fakie Heelflip", "Fakie Inward Heelflip", "Fakie Kickflip", "Fakie Varial Heelflip", "Fakie Varial Kickflip", "Feather Flip", "Fingerflip", "Forward Flip", "Front Foot Impossible", "Frontside 360 Pop Shove it", "Frontside Bigspin", "Frontside Flip", "Frontside Half Cab Heelflip", "Frontside Half Cab Kickflip", "Frontside Heelflip", "Frontside Kickflip", "Frontside Pop Shove-it", "Gazelle Flip", "Gazelle Spin", "Ghetto Bird", "Gingersnap", "Grape Flip", "Half Cab", "Handstand Flip", "Hardflip", "Haslam Flip", "Heelflip", "Hospital Flip", "Illusion Flip", "Impossible", "Inward Heelflip", "Jesus Flip", "Kickback Flip", "Kickflip", "Kiwi Flip", "Laser Flip", "Late Kickflip", "Nerd Flip", "Nightmare Flip", "No Comply", "540", "720", "900", "Airwalk", "Benihana", "Cannonball", "Christ Air", "Crossbone", "Delmar Indy", "Indy", "Indy Grab", "Invert", "Japan Air", "Judo Air", "Madonna", "McTwist", "Melancholy Grab", "Melon", "Method Air", "Mute Air", "Nose Grab", "Rocket Air", "Sal Flip", "Seatbelt Grab", "Stiffy", "Superman Grab", "Varial", "Egg Plant", "Manual", "Nose Manual", "Varial Heelflip", "Varial Kickflip",\
                 "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "bail", "Abstract Art", "Abstract Expressionism", "Academicism", "Analytical Cubism", "Art Deco", "Art Nouveau", "Ashcan School", "Banksy", "Baroque", "Byzantine Art", "Classicism", "Cloisonnism", "Color Field", "Conceptual Art", "Constructivism", "Cubism", "Cubo-Futurism", "Dadaism", "Dutch Golden Age", "Early Netherlandish", "Early Renaissance", "Expressionism", "Fauvism", "Futurism", "Geometric Abstract Art", "Gothic Art", "High Renaissance", "Hudson River School", "Impressionism", "Italian Renaissance", "Kitsch", "Luminism", "Mannerism", "Metaphysical Art", "Minimalism", "Modernism", "Naive Art/ Primitivism", "Neo-Baroque", "Neo-Classicism", "Neo-Dada", "Neo Expressionism", "Neoplasticism", "New Realism", "Northern Renaissance", "Op-Art", "Orientalism", "Orphism", "Pointilism", "Pop Art", "Pop Surrealism", "Post-Imressionism", "Pre-Raphaelites", "Precisionism", "Proto Renaissance", "Purism", "Realism", "Regionalism", "Renaissance", "Rococo", "Romanticism", "Social Realism", "Socialist Realism", "Suprematism", "Surrealism", "Symbolism", "Synthetic Cubism", "Synthetism", "Tenebrism", "Tonalism", "Tubism", "Ukiyo-E", "Verism", "Alternative", "Anime", "Blues", "Classical", "Comedy", "Commercials", "Country", "Dance", "Easy Listening", "Electronic", "Enka", "French Pop", "Folk Music", "German Folk", "German Pop", "Fitness and Workout", "Hip-Hop/Rap", "Holiday Music", "Indie Pop", "Industrial", "Inspirational", "Instrumental", "Jazz", "K-Pop", "Karaoke", "Latin", "Metal", "New Age", "Opera", "Pop", "R&B/Soul", "Reggae", "Rock", "Soundtracks", "Spoken Word", "Tex-Mex/Tejano", "Vocal", "World", "You met", "You fought with", "You fought with", "You defeated", "You defeated","You defeated", "You were sent to the hospital by", "You were defeated by", "You healed", "You were healed by", "You jailed", "You pranked", "You were pranked by", "You were jailed by", "you were beat by", "you were K.Ode by", "a stranger", "a child", "an emo", "a doctor", "a soldier", "a police", "a homeless person", "a mom", "a gamer", "a dancer", "an artist", "a peasant", "a prince", "a princess", "a King", "a Queen", "a lawyer", "a vendor", "an alien", "a Mexican", "a nurse", "a lizard", "a woman", "a girl", "a boy", "Akira", "Pedro the dog", "an optometrist", "a physician", "a psychologist", "a psychiatrist", "a teacher", "White Tara", "Green Tara", "a ninja", "a gangster", "Dollars", "Rupies", "Yen", "Pesos", "Pounds", "Coins", "Arcade Coins", "Mickey Mouse Money", "Francs", "Shekels", "Tugriks", "Indian Rupees", "Singapore Dollars", "Rubles", "Dinars", "Yuans", "Bahts", "Afghanis", "Riyals", "Kronas", "Riels", "DDOS attacks", "Botnets", "Credit Card Numbers", "E-mail addresses", "Business Addresses", "Home Addresses", "Passwords", "Mobile Numbers", "Telephone Numbers", "STD", "spits", "garbage", "sickness", "nudes", "hate", "likes", "Canada", "Sweden", "China", "Beijing", "New York", "California", "L.A.", "San Francisco", "Detroit", "Colorado", "Newark", "New Jersey", "Australia", "Gold Coast", "Thailand", "North Korea", "Pyongyang", "Seoul", "Tokyo", "Osaka", "Japan", "Fujian", "Kyoto", "Manila", "Palawan", "Siargao", "Sultan Kudarat", "Davao", "Sydney", "Poland", "Uzbekistan", "Kyrgystan", "Turkey", "Iraq", "Iran", "Bolivia", "Iceland", "Lithuania", "Greenland", "UK", "France", "Spain", "Rome", "Greece", "Amsterdam", "Netherlands", "Boracay", "Indonesia", "Russia", "Ukraine", "Africa", "Antarctica", "Alaska", "South Carolina", "North Carolina", "Philadelphia", "Brooklyn", "Mexico", "Brazil", "Taiwan", "Burma", "Cambodia", "Vietnam", "India", "Bangladesh", "New Delhi", "Bombay", "Philippines", "Italy", "Belgium", "Denmark", "Colombia", "Argentina", "Albania", "Algeria", "Andora", "Angola", "Antigua and Barbuda", "Armenia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Belarus", "Belize", "Benin", "Bhutan", "Bosnia", "Botswana", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Chad", "Chile", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Congo", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Guinea", "Estonia", "Swaziland", "Ethiopia", "Fiji", "Gabon", "Gambia", "Ghana", "Guatemala", "Guyana", "Haiti", "Honduras", "Hungary", "Israel", "Italy", "Jamaica", "Kenya", "Jordan", "Laos", "Latvia", "Lebanon", "Liberia", "Liechtenstein", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritiana", "Mauritius", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Portugal", "Qatar", "Romania", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Slovakia", "Slovenia", "Solomon Islands", "South Africa", "South Korea", "South Sudan", "Sri Lanka", "Sudan", "Suriname", "Syria", "Tajikistan", "Tanzania", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Zambia", "Zimbabwe", "samurai helmet", "bike helmet", "motorcycle helmet", "astronaut helmet", "pilot helmet", "aviator hat", "baseball cap", "backwards baseball cap", "trucker cap", "backwards trucker cap", "construction helmet", "miner helmet", "skate helmet", "ski mask", "facemask", "beanie", "birthday party hat", "pantyhose", "f13th mask", "jabbawockee mask", "none", "poring hat", "beehive", "idea bubble", "speech bubble", "bucket hat", "black bucket hat", "beige bucket hat", "orange bucket hat", "blue bucket hat", "american football helmet", "rugby helmet", "emo hair", "mohawk", "blonded semi-balded", "skinhead", "tropika", "glasses", "raybans", "shades", "spectacles", "night-vision goggles", "pilot goggles", "black-rimmed glasses", "nostril piercing", "tibetan headgear", "sikh headgear", "muslim hat", "skullcap", "muslim skullhat", "long hair", "salt and pepper", "blonde", "headphones", "earphones", "visor hat", "headband", "cat headband", "rabbit headband", "afro", "curly curls", "facial mask", "face paint", "warpaint", "unipaint", "maked-up", "bush headgear", "soldier helmet", "buddhahead", "game-night drink", "cig", "tobacco", "spliff", "straw", "british army guard headgear", "police helmet", "police mask", "hanja mask", "java mask", "african continent mask", "feather", "chef hat", "indian chief headgear", "black paint", "hijab", "knight armor", "police armor", "samurai armor", "karate uniform", "police uniform", "soldier uniform", "korean robe", "japanese robe", "barong", "polo", "shirt", "black shirt", "sweater", "tanktop", "backpack", "slingbag", "none", "chest hair", "kevlar", "press vest", "bush gear", "hoodie", "white hoodie", "blue hoodie", "tight shirt", "nikes", "puma", "adidas", "coca-cola retro shirt", "rasta shirt", "sash", "soccer uniform", "american football armor", "football shirt", "soccer shirt", "referee shirt", "pacemaker", "bra", "bikini", "chest bag", "tuxedo", "suit", "bowtie", "tie", "apron", "chef uniform", "red paint", "black paint", "astronaut suit", "diving suit", "rashguard", "jersey", "bathrobe", "farmer gear", "lanyard", "muslim clothing", "sikh clothing", "tourguide uniform", "boyscout uniform", "girlscout uniform", "black sweater", "scarf", "shawl", "green hoodie", "pink hoodie", "jacket", "windbreaker", "varsity jacket", "jock jacket", "vest", "coat", "sword", "samurai", "club", "knife", "machete", "ice cream", "food", "coffee", "pizza", "camera", "gun", "staff", "ruler", "katana", "arnis", "nunchucks", "cat", "tablet", "phone", "iphone", "android", "fruitshake", "vape", "bong", "spliff", "joint", "beer", "champagne", "chainsaw", "folder", "testpaper", "pen", "macbook", "laptop", "linux computer", "pencil", "paintbrush", "tire pump", "fire extinguisher", "measuring device", "scalpel", "diamond cutter", "diamond", "diamonds", "trash", "water", "none", "empty-hand", "spraypaint", "smartwatch", "dynamite", "c4", "whisker", "whiskey", "liquor", "flask", "leaf", "feather", "book", "novel", "junkfood", "rifle", "sniper", "handgun", "laser", "keys", "guitar", "electric guitar", "classical guitar", "ukulele", "keyboard", "burger", "twig", "plank", "paddel", "coins", "money", "dollar bills", "fruit", "vegetable", "ps4 controller", "xbox controller", "ipod", "yarn", "spear", "bow", "tights", "shorts", "cycling shorts", "skirt", "bushwear", "pants", "leggings", "elephant pants", "skinny jeans", "jeans", "none", "trunks", "pants", "pants", "pants", "holster", "bruise", "slacks", "hiking pants", "karate pants", "taekwondo pants", "mma shorts", "briefs", "sleather pants", "slippers", "hotel slippers", "shoes", "shoes", "shoes", "shoes", "boots", "beige boots", "black army boots", "nikes", "adidas", "puma", "converse", "chucks", "none", "socks", "clogs", "leather shoes", "white shoes", "skateboard", "longboard", "sneakers", "new balance", "world balance", "fluffy shoes", "fluffy slippers", "sandals", "You walk in a field", "You encounter an animal", "You encounter a monster", "You encounter an enemy", "You encounter a friend", "You encounter an ally", "You enter an alley", "It is night time", "The sun just rised", "It is dawn", "It is dusk", "You enter the university", "You sit down on your computer", "You just chill", "You chill in a cafe", "You feel sleepy", "You are hungry", "You walk on", "You run straight", "You run in loops", "You are tired", "You are bullied", "You are sent to the hospital", "You go on a roadtrip", "You hike", "You mine", "You are out of money", "You just earned your salary", "You spend your time waiting", "You just nearly died", "You do your assignment", "You paint", "You hum", "You rap", "You sing", "You hear someone singing", "You compose rap", "You compose a classical track", "You feel lonely", "You feel happy", "You feel ecstatic", "You yearn for something", "You feel you should meditate", "You feel you should pray", "You walk in a church", "You walk in a temple", "You walk in a mosque", "You walk in a forest", "You walk in a jungle", "You walk along the road", "You're in the city", "You ride a bus", "You ride a cab", "You take out the trash", "You find a job", "Someone gave you work", "You worship", "You're in transit", "You surf the internet", "You got hacked", "You got scammed", "You exercise", "You were commissioned in the army", "You were commisioned in the police force", "You were commissioned in the airforce", "You were commissioned in the marines", "You have a mission", "You feel inspired", "You feel uninspired", "You feel creative block", "You feel like dancing", "You hear music", "You watch TV", "You hear the radio", "You are fatigued", "You enter war", "You meet someone", "You view film showing schedules", "You browse through courses", "You walk into a market", "You think of getting souvenirs", "You explore the place", "red", "crimson", "maroon", "scarlet", "orange", "amber", "rust", "salmon", "green", "emerald", "lime", "olive", "yellow", "gold", "lemon", "mustard", "blue", "azure", "indigo", "teal", "purple", "lavender", "magenta", "violet", "brown", "beige", "chocolate", "sienna", "gray", "charcoal", "silver", "slate", "black", "ebony", "jet", "onyx", "white", "alabaster", "ivory", "pearl", "pink", "sky blue", "neon green", "neon yellow", "neon orange", "neon blue", "touchdown", "touchdown", "touchdown", "first down", "first down", "first down", "first down", "second down", "second down", "second down", "third down", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "the path is clear", "there are 3 guards ahead of you", "there are 3 guards ahead of you", "there are 3 guards ahead of you", "there are 4 guards ahead of you", "there are 2 guards ahead of you", "there are 2 guards ahead of you", "there are 2 guards ahead of you", "there is 1 guard ahead of you", "there is 1 guard ahead of you"]
    result = random.sample(nano, 5)
    print(result)

    print()

def call_random_function():
    while True:
        time.sleep(random.randint(30, 360))
        random_function()

if __name__ == '__main__':
    threading.Thread(target=call_random_function).start()

