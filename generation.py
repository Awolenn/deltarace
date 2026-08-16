import random

# template:
# E E E E H
# E H E E E
# H E E E E
# E E E H E
# E E H E E

easy = [
    # GENERAL
    "No skipping the Light World segments", 
    "For every chapter you beat, beat one area in Undertale", 
    "For every chapter you beat, beat one area in Undertale Yellow", 
    "Complete a new song in Friday Night Dustin' every time you die", 
    "Find Starwalker in every chapter", 
    "Get all the Eggs", 
    "Eat the Moss in every chapter", 
    "Get all Recruits", 
    "Go out of your way to lose every recruit", 
    "Do all the Dojo Fights (includes Trashy Trio)", 
    "Get every FRIEND encounter", 
    "Beat Sans", 
    "Install whatever mod is first on GameBanana before playing", 
    "Beat one chapter twice", 
    "Draw the Fun Gang", 
    "Replace one chapter with DeltaChars' singleplayer campaign", 
    "Complete one night of Five Nights at Freddy's after finishing a chapter", 
    "If you die, you have to detour into an Asymmetrical of your choice and win one round", 
    "When you unlock it, use only S-Action and R-Action throughout the whole game unless it's necessary to do otherwise", 
    "Only use Pacify and Sleep Mist to spare enemies", 
    "Get every weapon and armor", 
    "Open every chest", 
    "Choose one chapter and replace it with the entire TS!Underswap demo", 
    "After beating a chapter, draw your favorite character from that chapter",
    "You may only mark this space if you marked the spaces above, below, and to the left and right of this space.", 
    "You can't use completion data.",
    "You have to watch a UTDR Analog Horror video every time you die.", 
    "Have you ever heard of Five Nights at Undertale's? No? Well, go beat it.",
    "Write a 5 paragraph essay about the themes of the Weird route and get a 50 percent approval rating from members of the VC. 5+ sentences per paragraph.",
    "Mute your audio.",
    "Misgender Kris every time you want to refer to them and don't tell the VC it's part of your bingo.",
    "Beat Undyne the Undying",
    "Every time you see the Knight, launch into a multiminute long rant about how the Knight is very obviously Papyrus",
    "Give everyone else a 20 minute headstart.",
    "Whenever someone mentions any character who's in your party at that moment, you have to shout 'OH, THAT GUY?? I KNOW THAT GUY!!'",
    "Talk to Onion every time you can.",
    "You have to dress like Kris, or as close to Kris as possible, during the entire race.",
    "Every time you take a break, a timer starts, and the timer determines how long you have to actively backtrack for when you get back (or until you hit a point you can't backtrack past)",
    "Every time anyone else beats a chapter, you have to reload immediately, regardless of how close you were to the next save",
    "Use a Deltarune but it's [percentage] [color] mod, and someone else has to set all the settings for you",
    "Once you finish, read a Deltarune fanfiction out loud. You can't mark this space and complete your bingo until the fanfiction is completely finished.",
    "Skip a chapter and see if anyone notices. If no one notices, you can get away with it! If they do, you have to play the chapter you skipped and the one before it.",
    "Say that Nico/Techni/Chiro was kinda cooking off rip and defend yourself for it. You are not allowed to take it back or reveal that this is on your bingo.",
    "Stick to the edges of the box during every enemy turn throughout your race.",
    "Create a Dustrune take, complete with character designs for main characters and chapter antagonists (Kris, Susie, Ralsei, Noelle, Berdly, King, Queen, Tenna, the Knight, Gerson, the Titan, and Flowery) and a basic outline of what chapters 1-5 would look like. You have to get a 50 percent approval rating from the VC to mark this space.",
    "You have to get in a DM call with someone completely random (spun by wheel), and can't rejoin the main VC until you both beat a chapter (you can't pick someone who's already beaten their race).",
    "You have to listen to The Sick Mind of EDP445 on loop during the whole race.",
    "Purposefully trigger the dogcheck on every chapter",
    "Throughout your playthrough, build evidence for a Knight identity case and make it at least mildly convincing. Popular Knight candidates are not allowed.",
    "Unironically say that you goon to Aqua. You can't take it back or explain that it's on your bingo.",
    "You have to end every fight with a party member downed (unless it's a solo fight)",
    "Any time you can't skip dialogue, you have to dub it in an annoying voice",
    "Play the whole game in Japanese",
    "When trying to use any action that costs TP, you MUST get your TP to 100 percent as if the action costs 100 TP",
    "Become linked to another person. When that person enters a puzzle, they can only do what you tell them to do, and vice versa.",
    "Choose the worst dialogue choice every chance you get",
    "Maximize Kris' kit for magic even though they don't have a use for it",
    "Even if you beat a secret boss, you can't use their reward items (normal equippables only)",
    "Use every Talk option during full screen shops",
    "Use Check every time you encounter an enemy for the first time",
    "No ReviveMints",

    # CHAPTER ONE
    "Listen to Ralsei's tale in Chapter 1", 
    "Do Ralsei's tutorial in Chapter 1", 
    "Make your Thrash Machine full duck", 
    "Buy one of everything in Seam's Seap",
    "Beat Jevil by FIGHTING, except you have to Pirouette with Kris on every turn they're up", 
    "Beat K. Round's rematch without Susie's Idea",
    "Fight all encounters in Chapter 1 and get the ending where Ralsei pacifies the King", 
    "Talk to every Hometown NPC in Chapter 1", 
    "Fix the TopCake",
    "Complete Chapter 1 on a SURVEY_PROGRAM build", 
    "Beat Chapter 1 itemless", 
    "Name yourself Gaster during the goner maker", 
    "Don't equip any new weapons or armor during Chapter 1", 
    "Defeat both Jevil and King by fighting, but you can only deal damage with Rude Buster",
    "Die to Lancer during the opeing ambush",
    "Every change you get during Chapter 1, use Pacify, even if you're totally wasting the TP",
    "Throw away the Manual",
    "Name your party the Fuck(?) Squad",

    # CHAPTER TWO
    "Recruit Hacker", 
    "Recruit Bumper Cars", 
    "Get the Ragger2", 
    "Do the Weird Route",
    "Do the Weird Route and abort after getting the ThornRing", 
    "Do Spamton NEO on Hard Mode", 
    "Make sure Lancer is well fed", 
    "Enter a fight with a full inventory of S. Poison and then use every single one", 
    "Don't equip any new weapons or armor during Chapter 2", 
    "Beat Chapter 2 Itemless", 
    "Beat Spamton NEO without firing a [[ BIG SHOT! ]] except for in the tutorial", 
    "Taunt Berdly with the appealing blue shape",
    "When Noelle is in your party, automatically give her the best armors you have and let her keep them the whole time, knowing full well she'll leave the party and take that shit with her",

    # CHAPTER THREE
    "Get an S Rank (any board)", 
    "Get a Z Rank (any board)", 
    "Get all 5 keys in Board 1", 
    "Win at least one round of Susiezilla", 
    "Get the Egg in Chapter 3", 
    "Get the 1225 secret in Chapter 3", 
    "Go to the Bonus Zone in Chapter 3", 
    "Use the Dog button during the Rouxls Fight", 
    "Don't equip any new weapons or armor during Chapter 3", 
    "Beat Chapter 3 Itemless",
    "Name yourself ASS",
    "You can only use ILoveTV during the Tenna fight",
    "You have to 100 percent every Quiz during Board 1. If you miss a question, reload",

    # CHAPTER FOUR 
    "Do the Weird Route and abort in Chapter 4", 
    "Beat Gerson while using Rude Buster every time you can, and if you mess up the parry chain you have to restart",
    "Do at least 5 Piano Secrets in Chapter 4", 
    "Fight the Mikes", 
    "Listen to Kris' entire phone call as they drink the chocolate milk", 
    "Get the GoldWidow",
    "Get the DogDollar in Chapter 4", 
    "Only use S-Action and R-Action unless it's necessary to do otherwise in Chapter 4",
    "Beat Gerson and Sound of Justice while only pointing your shield up and down", 
    "Don't equip any new weapons or armor during Chapter 4", 
    "Beat Chapter 4 Itemless",
    "Record yourself trying to open a Dark Fountain after Susie does it. Don't half ass it. Do the jump and everything. Cheesy dialogue too.",

    # CHAPTER FIVE
    "Do the Weird Route and abort in Chapter 5", 
    "Make Susie's outfit full duck", 
    "Get at least 100 Flowery Dollars from the infinite chest", 
    "Defeat Pink with meaner bombs (*Note: Girls like it when you are better at dodging danmaku.)", 
    "Get all the Pink Coins", 
    "Go take a picture of any water during the Light World lake scene in Chapter 5", 
    "Go outside and take a photo of the sun when the Sunset of Seven Suns beat drop happens for the first time", 
    "Do every Suselle interaction during the Festival",
    "Do every Krusie interaction during the Festival", 
    "Do every Kriselle interaction during the Festival", 
    "Do 4rd Sanctuary in Castle Town", 
    "Beat Pink while only using Kris' regular Doki act", 
    "If you die on Pink once, you have to record yourself covering the entirety of chai's Cutie Mew Mew Magic with lyrics", 
    "Talk to Pink about FRIEND",
    "Waste all your items on Flowery once he's in your party", 
    "Don't equip any new weapons or armor during Chapter 5", 
    "End every fight that you can with Scythemare",
    "Beat Chapter 5 Itemless", 
    "Beat Flowery without dashing", 
    "Force yourself to die to THAT attack (duck) during the Seth and Aqua fight.",
    "Every time you see a flower's Omega, you have to load into and beat the Omega Flowey fight in Undertale (Flowey's Time Machine permitted)",
    "Very annoyingly sing Flower Man's lyrics when you fight Flowery",
    "You can only speak in Flowery voice lines during Chapter 5"
]

hard = [
    # GENERAL
    "Beat Undertale: Last Breath", 
    "Don't equip any new armors or weapons. Ever.", 
    "Beat an FDY Fangame (no noob mode)", 
    "Beat Sans 5 times", 
    "Set up and run a solo Deltarune Archipelago for any 1 chapter", 
    "Someone else chooses your keybinds for 1 chapter", 
    "No running. Ever.", 
    "Once you get to Chapter 5, switch chapters with the person who's in last", 
    "You can only save once per chapter", 
    "That's weird... you could have sworn there was a bingo space here, but it's gone. Looks like you can't complete any bingos where this space would have been.",
    "Start with a blank canvas. Every time you encounter an enemy, you have to draw them on that canvas, throughout the entire race. Repeats included.", 
    "Mod yourself over a party member. You have to draw the overworld idle and walking sprites, dark world idle, walking, and battle sprites, and all the portraits.",
    "Set your monitor brightness to the lowest possible setting where you can still see.",
    "Someone else in the VC gets to choose a challenge for this space.",
    "Free space, but you give Sadie an I.O.U.",
        "Use the Custom Difficulty mod with the Hard Preset",
    "Use the Custom Difficulty mod with the Nightmare Preset",
    "Use the Custom Difficulty mod with the Nightmare-EX Preset",
    "Use the Custom Difficulty mod with the Nightmare-NEO Preset",
    "Use the No I-Frames mod",
    "Beat Mifune's Sans Hard Mode Fight",
    "If you're not last, 1v1 the person who finishes after you in a game of their choice. If they win, they steal your place from you and you automatically place after them.",
    "Get 5 killer wins in The Roaring - Deltarune (the asym)",
    "You can't move the soul during fights. Exception allowed if you die to the same encounter 3 times in a row",
    "Get all 93 endings in Undertale (please don't do this)",
    "You can only equip new armors and weapons on Ralsei",

    # CHAPTER ONE
    "You have to defeat both Jevil and King by fighting, but Ralsei is the only one allowed to attack",
    "No-hit King. If you take damage, reload",

    # CHAPTER THREE
    "Get a T Rank (any board)", 
    "Defeat the Knight mantleless", 
    "Use Kaizo Knight", 
    "Full combo Lightners Live",
    
    # CHAPTER FOUR
    "Use the secret Ultimate Boss Rush Mod Mod and complete it during Chapter 4",
    
    # CHAPTER FIVE
    "Use Determination Flowery"
]

# [ YES, HE SCRAWLS HIS NAME IN THE MARGINS OF HIS NOTES. HE NAMES PROGRAMMING VARIABLES AFTER HIM. ]
def easyChoice():
    easyNumber = random.randint(0, len(easy)-1)
    malachy = easy[easyNumber]
    easy.pop(easyNumber)
    return malachy

def hardChoice():
    hardNumber = random.randint(0, len(hard)-1)
    malachy2 = hard[hardNumber]
    hard.pop(hardNumber)
    return malachy2

def finalChoice():
    print(easyChoice(), "|", easyChoice(), "|", easyChoice(), "|", easyChoice(), "|", hardChoice())
    print(easyChoice(), "|", hardChoice(), "|", easyChoice(), "|", easyChoice(), "|", easyChoice())
    print(hardChoice(), "|", easyChoice(), "|", easyChoice(), "|", easyChoice(), "|", easyChoice())
    print(easyChoice(), "|", easyChoice(), "|", easyChoice(), "|", hardChoice(), "|", easyChoice())
    print(easyChoice(), "|", easyChoice(), "|", hardChoice(), "|", easyChoice(), "|", easyChoice())

print("HEY GUYS ITS ME THE BINGO MAKER!!!!")
print("HERE'S YOUR BOARD!!!!")
finalChoice()