'''
Program name: WhatToPlay.py
Programmer: Tyler Davies
Date: 10-13-21
Description: This program generates a random number which is used to print a video game with
             the console it is to be played on. "Do not waste time choosing, just play!"
	     Randomly choose a game to play based on console, game type, single/multiplayer,
	     not played yet/completed; create, upload, and save lists of games.
Additions/Notes: THIS IS A WORK IN PROGRESS...
		 List of Dictionaries (name, console, type, played-no, yes, finished-, rating)
                 Input File (require some sort of delimitor like /n)
                 Output File (usable as input again, but also in a nice printable format)
                 Add Functions (Sort, Search, Print, etc.)
                 Executable on Phone???
'''

import random

gameList = {
    1:'2048 Battles',
    2:'A Duel Hand Disaster: Trackher',
    3:'Aborigenus',
    4:'Adrenaline Rush: Miami Drive',
    5:'Almost There: The Platformer',
    6:'Among Us',
    7:'Archaica: The Path of Light',
    8:'Assassin’s Creed III Remastered',
    9:'Assassin’s Creed Black Flag (The Rebel Collection)',
    10:'Assassin’s Creed Rogue (The Rebel Collection)',
    11:'Atomic Heist',
    12:'Bastion',
    13:'Blades',
    14:'Blood Breed',
    15:'Bloodroots',
    16:'Bridge Strike',
    17:'Capcom Arcade Stadium',
    18:'Captain Toad Treasure Tracker',
    19:'Cat Quest',
    20:'Chess Ace',
    21:'Child of Light Ultimate Edition',
    22:'Clubhouse Games: 51 Worldwide Classics',
    23:'Colorgrid',
    24:'Cosmic Star Heroine',
    25:'Crash Bandicoot N’ Sane Trilogy',
    26:'Crash Team Racing',
    27:'Crypt of the Necrodancer',
    28:'Cuphead',
    29:'Dark Burial',
    30:'Dead Dungeon',
    31:'Deadly Fighter 2',
    32:'Debtor',
    33:'Defunct',
    34:'Deponia',
    35:'Diabolic',
    36:'Digimon Story Cyber Sleuth: Complete Edition',
    37:'Ding Dong XL',
    38:'Disc Jam',
    39:'Aladdin (Disney Classic Games)',
    40:'The Lion King (Disney Classic Games)',
    41:'Dragon Quest Triology (Dragon Quest, Luminaries or the Legendary Line, The Seeds of Salvation)',
    42:'Drawngeon: Dungeons of Ink and Paper',
    43:'Earthworms',
    44:'Elliott Quest',
    45:'Fantasy Strike',
    46:'Farabel',
    47:'Felix the Reaper',
    48:'Flashback',
    49:'Galaxy of Pen and Paper',
    50:'Genetic Disaster',
    51:'Ghostbusters: The Video Game Remastered',
    52:'GhoulBoy',
    53:'Girabox',
    54:'Green Game',
    55:'Gurgamoth',
    56:'Hades',
    57:'Hang the Kings',
    58:'Horace',
    59:'Island Maze',
    60:'Jenny LeClue—Detective',
    61:'Jeopardy!',
    62:'Jumping Joe! & Friends',
    63:'Kakuro Magic',
    64:'Killer Queen Black',
    65:'Knights of Pen & Paper Bundle',
    66:'Lego DC Super-Villains Deluxe Edition',
    67:'Ludo Mania',
    68:'Lumo',
    69:'Mad Carnage',
    70:'Mana Spark',
    71:'Mario & Rabbids Kingdom Battle Gold Edition',
    72:'Mario & Sonic Olympic Games Tokyo 2020',
    73:'Mario Kart 8 Deluxe',
    74:'Marooners',
    75:'Marvel Ultimate Alliance 3: The Black Order',
    76:'Mech Rage',
    77:'Mecho Tales',
    78:'Mecho Wars: Desert Ashes',
    79:'Membrane',
    80:'Monopoly for Nintendo Switch',
    81:'Moto Rush GT',
    82:'My Brother Rabbit',
    83:'Naruto Shippuden Ultimate Ninja Storm Trilogy (1-3)',
    84:'NecroWorm',
    85:'Odium to the Core',
    86:'Old Man’s Journey',
    87:'One Person Story',
    88:'One Piece: Pirate Warriors Deluxe Edition (3 & 4)',
    89:'One Piece Unlimited World Red Deluxe Edition',
    90:'Overlanders',
    91:'Overwatch',
    92:'Pan-Pan A tiny big adventure',
    93:'Peace. Death!',
    94:'Perseverance',
    95:'Plague Road',
    96:'Picross: Lord of the Nazarick',
    97:'Picross S, S2, S3, & S4',
    98:'Pinball FX 3',
    99:'Pokkén Tournament DX w/ Battle Pass',
    100:'Real Drift Racing',
    101:'Red Game Without a Great Name',
    102:'Revenge of the Bird King',
    103:'Runner 3',
    104:'Seeders Puzzle Reboot',
    105:'Shalnor Legends: Sacred Lands',
    106:'Skee-Ball',
    107:'Solitaire Deluxe Bundle 3 in 1',
    108:'Sonic Forces',
    109:'Space Pioneer',
    110:'Sparklite',
    111:'Spider Solitaire',
    112:'Spirit Roots',
    113:'Spyro Reignited Trilogy',
    114:'Squidlit',
    115:'Starman',
    116:'Star Wars Episode 1: Racer',
    117:'Star Wars Jedi Knight (Jedi Academy & Jedi Outcast)',
    118:'Star Wars Pinball',
    119:'State of Mind',
    120:'Street Basketball',
    121:'Super Battle Cards',
    122:'Super Kirby Clash',
    123:'Super Mario 3D All-Stars (3in1)',
    124:'Super Mario Bros 35',
    125:'Super Mario Odyssey',
    126:'Super Mario Party',
    127:'Super Monkey Ball: Banana Blitz HD',
    128:'Super Smash Bro’s Ultimate',
    129:'Swaps and Traps',
    130:'Swordbreaker The Game',
    131:'Tactical Mind (1 & 2)',
    132:'Tardy',
    133:'The Bridge',
    134:'The Escapists: Complete Edition',
    135:'The Legend of Zelda: Breath of the Wild (w/ Expansion Pass)',
    136:'The Outer Worlds',
    137:'The Rainsdowne Players',
    138:'The Warlock of Firetop Mountain',
    139:'The Way Remastered',
    140:'Thief Simulator',
    141:'Totes the Goat',
    142:'Trancelation',
    143:'Trine (1-4)',
    144:'Uno Ultimate Edition',
    145:'Valiant Hearts: The Great War',
    146:'Warframe',
    147:'Wheel of Fortune',
    148:'while True: learn()',
    149:'Windmill Kings',
    150:'Wreckin’ Ball Adventure',
    151:'NES - Nintendo Switch Online',
    152:'Pokemon Sword (w/ The Isle of Armor & The Crown Tundra)',
    153:'SNES - Nintendo Switch Online',
    154:'Just Glide',
    155:'Pokemon Unite',
    156:'Abzû',
    157:'Assassin’s Creed Odyssey',
    158:'AC Origins Deluxe Edition/Season Pass',
    159:'Astro Bot Rescue Mission',
    160:'Back to Bed',
    161:'Battlefield 1',
    162:'Call of Duty: Advanced Warfare',
    163:'Call of Duty: WW2',
    164:'Crash Bandicoot 4: It’s About Time',
    165:'Dragon Age: Inquisition',
    166:'Enter the Gungeon',
    167:'Fat Princess Adventures',
    168:'God of War (Omega)',
    169:'Horizon Zero Dawn: Complete Edition',
    170:'Injustice Gods Among Us Ultimate Edition',
    171:'Journey',
    172:'Kingdom Hearts HD 1.5 & 2.5 ReMix',
    173:'Life is Strange',
    174:'Moss',
    175:'NHL 18',
    176:'One Piece: World Seeker',
    177:'Paper Beast',
    178:'Psychonauts',
    179:'Pyre',
    180:'Q*bert Rebooted',
    181:'Ratchet & Clank',
    182:'Rez Infinite',
    183:'Shadow of War',
    184:'Star Trek: Bridge Crew',
    185:'Star Wars Battlefront II',
    186:'Stories: The Path of Destinies',
    187:'Subnautica',
    188:'Super Meat Boy',
    189:'Thumper',
    190:'Typoman',
    191:'The Unfinished Swan',
    192:'The Witcher 3: Wild Hunt Complete Edition',
    193:'The Witness',
    194:'Uncharted: The Nathan Drake Collection',
    195:'Whispering Willows',
    196:'Back to the Future (Episodes 1-5)',
    197:'Batman: Arkham City',
    198:'Sound Shapes (Best of PlayStation Network Vol. 1)',
    199:'Tokyo Jungle (Best of PlayStation Network Vol. 1)',
    200:'When Vikings Attack! (Best of PlayStation Network Vol. 1)',
    201:'Bomberman Ultra',
    202:'Castle Crashers',
    203:'Defiance',
    204:'Deadpool',
    205:'Destiny',
    206:'Diablo 3',
    207:'Dishonored',
    208:'God of War Saga (God of War, God of War II, God of War III, Chains of Olympus, and Ghost of Sparta)',
    209:'Hitman Absolution',
    210:'Infamous 2',
    211:'Jurassic Park The Game (Episodes 1-4)',
    212:'Lego: The Lord of the Rings',
    213:'Madden 09',
    214:'Middle Earth: Shadow of Mordor',
    215:'Mirror\'s Edge',
    216:'Need for Speed Hot Pursuit',
    217:'NBA Jam: on Fire Edition',
    218:'NFL Blitz',
    219:'Pac-Man: Championship Edition DX+',
    220:'Payday: The Heist',
    221:'Sour Calibur Lost Swords',
    222:'South Park: The Stick of Truth',
    223:'Star Wars: The Force Unleashed (1 & 2)',
    224:'The Last of Us',
    225:'The Wolf Among Us',
    226:'Thief',
    227:'Twisted Metal: Black',
    228:'Just Cause 2 (Ultimate Action Pack)',
    229:'Sleeping Dogs (Ultimate Action Pack)',
    230:'Tomb Raider (Ultimate Action Pack)',
    231:'Watchdogs'
}
#Switch (1-155)
#PlayStation 4 (156-195)
#PlayStation 3 (196-231)

choice = random.randint(1, 231)
print(gameList[choice], end = ' ')

if choice >= 1 and choice <= 155:
    print('(Switch)')
elif choice >= 156 and choice <= 195:
    print('(PlayStation 4)')
elif choice >= 196 and choice <= 231:
    print('(PlayStation 3)')
else:
    print('Error!')

'''
Omitted Games:
Switch
#Completed
    Borderlands: Game of the Year Edition
    Borderlands 2: Game of the Year Edition
    Borderlands: The Pre-Sequel Ultimate Edition
    Mushroom Quest
    Zombie Army Trilogy
#Multiplayer
    Drawful 2
    Rocket League
    Watermelon Party
#Ehh...
    Breakfast Bar Tycoon
    Bubble Cats Rescue
    Burger Chef Tycoon
    Classic Games Collection Vol. 1
    Conduct Together!
    Cooking Tycoons 3 in 1 Bundle
    Flowlines VS
    Food Truck Tycoon
    Funbox Party
    Funny Bunny Adventures
    Go! Fish Go!
    Jump Rope Challenge
    Pet Shop Snacks
    Pizza Bar Tycoon
    Quest for the Golden Duck

Playstation 4:
#Duplicate
    Crash Bandicoot N-Sane Trilogy
    Rocket League Collector’s Edition
    Warframe
#Completed
    King’s Quest
#Multiplayer
    Fluster Cluck
    Jack-box Party Pack 3

Playstation 3:
#Duplicate
    Injustice: Gods Among Us (Ultimate Edition)
    The Unfinished Swan
    Uncharted 3: Drake's Deception
#Completed
    Marvel Ultimate Alliance
    NHL 14
#Multiplayer
    Fat Princess
    Jackbox Party Pack
    Jackbox Party Pack 2
    PlayStation All-Stars Battle Royale
'''
