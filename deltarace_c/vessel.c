const char* easyNames[] = {
  "No skipping the Light World segments", //0
  "For every chapter you beat, beat one area in Undertale", //1
  "For every chapter you beat, beat one area in Undertale Yellow", //2
  "Complete a new song in Friday Night Dustin' every time you die", //3
  "Find Starwalker in every chapter", //4
  "Get all the Eggs", //5
  "Eat the Moss in every chapter", //6
  "Get all Recruits", //7
  "Go out of your way to lose every recruit", //8
  "Do all the Dojo Fights", //9
  "Get every FRIEND encounter", //10
  "Beat Sans", //11
  "Install whatever mod is first on GameBanana before playing", //12
  "Beat one chapter twice", //13
  "Draw the Fun Gang", //14
  "Replace one chapter with DeltaChars' singleplayer campaign", //15
  "Complete one night of Five Nights at Freddy's after finishing a chapter", //16
  "Win a round of an asym of your choice every time you die", //17
  "Only use S-Action and R-Action", //18
  "Only use Pacify and Sleep Mist to spare enemies", //19
  "Get every weapon and armor", //20
  "Open every chest", //21
  "Choose one chapter and replace it with the entire TS!Underswap demo", //22
  "After beating a chapter, draw your favorite character from that chapter", //23
  "You may only mark this space if you marked the spaces above, below, left, and right of this one.", //24
  "You can't use completion data.", //25
  "You have to watch a UTDR Analog Horror video every time you die.", //26
  "Have you ever heard of Five Nights at Undertale's? No? Well, go beat it.", //27
  "Write a 5 paragraph essay about the themes of the Weird route", //28
  "Mute your audio.", //29
  "Misgender Kris every time you want to refer to them", //30
  "Beat Undyne the Undying", //31
  "Whenever you see the Knight, rant about how the Knight is very obviously Papyrus", //32
  "Give everyone else a 20 minute headstart", //33
  "Whenever someone mentions a party member, shout 'OH, THAT GUY?? I KNOW THAT GUY!!'", //34
  "Talk to Onion every time you can", //35
  "You have to dress like Kris, or as close to Kris as possible, during the entire race", //36
  "Every time you take a break, backtrack a certain amount", //37
  "Every time anyone else beats a chapter, reload immediately", //38
  "Use a [percentage] [color] mod with the settings set by someone else", //39
  "Once you finish, read a Deltarune fanfiction out loud", //40
  "Skip a chapter and be careful not to get caught! Or else...", //41
  "Say that Nico/Techni/Chiro was kinda cooking off rip and defend yourself for it", //42
  "Stick to the edges of the box during every enemy turn throughout your race", //43
  "Create a Dustrune take", //44
  "Solo call with a random person for a chapter", //45
  "You have to listen to The Sick Mind of EDP445 on loop during the whole race", //46
  "Purposefully trigger the dogcheck on every chapter", //47
  "Collect evidence for a non-popular Knight candidate", //48
  "Unironically say that you goon to Aqua", //49
  "You have to end every fight with a party member downed", //50
  "Any time you can't skip dialogue, you have to dub it in an annoying voice", //51
  "Play the whole game in Japanese",
  "When trying to use any action that costs TP, you MUST get your TP to 100 percent before usage",
  "Become linked to another person and have them control your puzzles and vice versa",
  "Choose the worst dialogue choice every chance you get", //55
  "Maximize Kris' kit for magic even though they don't have a use for it",
  "Even if you beat a secret boss, you can't use their reward items",
  "Exhaust every Talk option during full screen shops",
  "Use Check every time you encounter an enemy for the first time",
  "Collect every ReviveMint but don't use any of them", //60
  "If you die, you have to read an act of Homestuck",
  "Play with a friend", 
  "You have to watch 'If Deltarune was Realistic'",

  // CHAPTER ONE
  "Listen to Ralsei's tale in Chapter 1",
  "Do Ralsei's tutorial in Chapter 1", //65
  "Make your Thrash Machine full duck",
  "Buy one of everything in Seam's Seap",
  "Beat Jevil by FIGHTING, except you use Pirouette every turn you can",
  "Beat K. Round's rematch without Susie's Idea",
  "Fight all encounters in Chapter 1 and get the ending where Ralsei pacifies the King", //70
  "Talk to every Hometown NPC in Chapter 1",
  "Fix the TopCake",
  "Complete Chapter 1 on a SURVEY_PROGRAM build",
  "Beat Chapter 1 itemless",
  "Name yourself Gaster during the goner maker", //75
  "Don't equip any new weapons or armor during Chapter 1",
  "Defeat both Jevil and King by fighting, but you can only deal damage with Rude Buster",
  "Die to Lancer during the opeing ambush",
  "Every change you get during Chapter 1, use Pacify, even if you're totally wasting the TP",
  "Throw away the Manual", //80
  "Name your party the $!$? Squad",

  // CHAPTER TWO
  "Recruit Hacker", 
  "Recruit the Electro-Dashers", 
  "Get the Ragger2", 
  "Do the Weird Route", //85
  "Do the Weird Route and abort after getting the ThornRing", 
  "Do Spamton NEO on Hard Mode", 
  "Make sure Lancer is well fed", 
  "Enter a fight with a full inventory of S. Poison and then use every single one", 
  "Don't equip any new weapons or armor during Chapter 2", //90
  "Beat Chapter 2 Itemless", 
  "Beat Spamton NEO without firing a [[ BIG SHOT! ]]", 
  "Taunt Berdly with the appealing blue shape",
  "Give Noelle your best armor and let her take them with her",

  // CHAPTER THREE
  "Get an S Rank (any board)", //95
  "Get a Z Rank (any board)", 
  "Get all 5 keys in Board 1", 
  "Win a round of Susiezilla",
  "Get the 1225 secret in Chapter 3", 
  "Go to the Bonus Zone in Chapter 3", //100
  "Use the Dog button during the Rouxls Fight", 
  "Don't equip any new weapons or armor during Chapter 3", 
  "Beat Chapter 3 Itemless",
  "Name yourself ASS during Chapter 3",
  "You can only use ILoveTV during the Tenna fight", //105
  "You have to 100 percent every Quiz during Board 1",

  // CHAPTER FOUR 
  "Do the Weird Route and abort in Chapter 4", 
  "Always use Rude Buster against Gerson and never fumble the parry chain",
  "Do at least 5 Piano Secrets in Chapter 4", 
  "Fight the Mikes", //110
  "Listen to Kris' entire phone call as they drink the chocolate milk", 
  "Get the GoldWidow",
  "Get the DogDollar in Chapter 4", 
  "Beat Gerson and Sound of Justice while only pointing your shield up and down", 
  "Don't equip any new weapons or armor during Chapter 4", //115
  "Beat Chapter 4 Itemless",
  "Record yourself trying to open a Dark Fountain after Susie does it",

  // CHAPTER FIVE
  "Do the Weird Route and abort in Chapter 5", 
  "Make Susie's outfit full duck", 
  "Get at least 100 Flowery Dollars from the infinite chest", //120
  "Defeat Pink with meaner bombs", 
  "Get all the Pink Coins", 
  "Go take a picture of any water during the Light World lake scene in Chapter 5", 
  "Go outside and take a photo of the sun when the Sunset of Seven Suns beat drops", 
  "Do every Suselle interaction during the Festival", //125
  "Do every Krusie interaction during the Festival", 
  "Do every Kriselle interaction during the Festival", 
  "Do 4rd Sanctuary in Castle Town", 
  "Beat Pink while only using Kris' regular Doki act", 
  "If you die on Pink once, record a cover of chai's Cutie Mew Mew Magic with lyrics", //130
  "Talk to Pink about FRIEND",
  "Waste all your items on Flowery once he's in your party", 
  "Don't equip any new weapons or armor during Chapter 5", 
  "End every fight that you can with Scythemare",
  "Beat Chapter 5 Itemless", //135
  "Every time you see a flower's Omega, beat the Omega Flowey fight in Undertale",
  "Very annoyingly sing Flower Man's lyrics when you fight Flowery",
  "You can only speak in Flowery voice lines during Chapter 5"
};
const int easyNamesLen = sizeof easyNames / sizeof *easyNames;

const char* hardNames[] = {
  "Beat Undertale: Last Breath", //0
  "Don't equip any new armors or weapons. Ever.", 
  "Beat an FDY Fangame (no noob mode)", 
  "Beat Sans 5 times", 
  "Set up and run a solo Deltarune Archipelago for any 1 chapter", 
  "Someone else chooses your keybinds for 1 chapter", //5
  "No running. Ever.", 
  "Once you get to Chapter 5, switch chapters with the person who's in last", 
  "You can only save once per chapter", 
  " ",
  "Every time you encounter an enemy, draw them on one canvas", //10 
  "Mod yourself over a party member",
  "Set your monitor brightness to the lowest setting where you can still see",
  "Someone else in the VC gets to choose a challenge for this space",
  "Free space, but you give Sadie an I.O.U.",
  "Use the Custom Difficulty mod with the Hard Preset", //15
  "Use the Custom Difficulty mod with the Nightmare Preset",
  "Use the Custom Difficulty mod with the Nightmare-EX Preset",
  "Use the Custom Difficulty mod with the Nightmare-NEO Preset",
  "Use the No I-Frames mod",
  "Beat Mifune's Sans Hard Mode Fight", //20
  "1v1 the person who finishes after you in a game of their choice",
  "Get 5 killer wins in The Roaring - Deltarune (the asym)",
  "You can't move the soul during fights",
  "Get all 93 endings in Undertale",
  "You can only equip new armors and weapons on Ralsei", //25
  "Every single bingo space must be completed on its own save file",

  // CHAPTER ONE
  "You have to defeat both Jevil and King via violence with only Ralsei",
  "No-hit King", //28

  // CHAPTER THREE
  "Get a T Rank (any board)", 
  "Defeat the Knight mantleless", //30
  "Use Kaizo Knight", 
  "Full combo Lightners Live",
  
  // CHAPTER FOUR
  "Use the secret Ultimate Boss Rush Mod Mod and complete it during Chapter 4",
  
  // CHAPTER FIVE
  "Use Determination Flowery",
  "Beat Flowery without dashing", //35
  "Force yourself to die to THAT attack during the Seth and Aqua fight.",
};
const int hardNamesLen = sizeof hardNames / sizeof *hardNames;

const char* easyDesc[] = {
  "You're not allowed to skip any of the Light World sections by sleeping. If you don't want to stream this, make sure to record yourself not sleep skipping if you want to prove it!", //0
  "You can stream this... or you can just beat the area and then take a picture of your save file and send it if you want to prove it.", //1
  "You can stream this... or you can just beat the area and then take a picture of your save file and send it if you want to prove it.", //2
  "If you want to prove this one, stream it!", //3
  "Find him, and take pictures of him to prove it! Each one of him.", //4 
  "Find them, and take pictures of them to prove it! Don't forget a single one.", //5
  "Eat the Moss whenever you can and send screenshots of your changing titles.", //6
  "Take a picture of your recruits page to prove this one!",  //7
  "Take a picture of your recruits page to prove this one. Chapter 1 and forced recruits get a pass.", 
  "This includes the Trashy Trio. If you want to prove this one, take a picture of the Dojo in Chapter 4 and a screenshot after the Trashy Trio fight in Chapter 5.", 
  "People see pink and yellow and think, oh, a friend! Make sure to record every encounter!", 
  "Stream you beating Sans or take a picture of him asleep to prove it.", 
  "Take a screenshot of the mod on the first page and whatever it does in the game to prove this one. Or, uh, stream the game effects instead of taking a picture.", 
  "...you don't have to do anything beyond streaming.", 
  "Make sure to show us your art if you want to prove this one!", 
  "Send a picture of you beating Black Eggman (why the fuck is that his name [Eggman Nega!]) to prove this. Streaming it also works.", //15
  "Stream it or send a picture of your Five Nights at Freddy's main menu screen to prove this one.", 
  "This sounds like it'll suck. You have to do this every time you die. Make sure to send a picture of every result screen to prove it, or stream your gameplay. Both work.", 
  "If it's necessary to do something else, you get a pass, such as during Chapter 1. Make sure to take notes on what Susie and Ralsei do, you're gonna be quizzed on it!", 
  "You'll have to stream your game for this one to be proved...", 
  "If you wanna prove this one, take a picture of every weapon and armor in your possession by the end of the game.", //20
  "Make sure to take notes on what these chests contain and where, you're gonna be quizzed on it!", 
  "Make sure to take a picture of your save file once you're done, or stream the gameplay!", 
  "Make sure to send a picture of your lovely art!",
  "It's like the Game of Life or something...", 
  "Make sure to show off your starting inventory in every chapter.", //25
  "Send a picture of your watch history after the race to prove this one... maybe tell us some fun facts or something, too. You can stream it if you want a watch party.", 
  "Send a picture of you beating this. Cause I told you to go beat it. You could stream it, too.",
  "You gotta send a picture of the essay and get a 50 percent approval rating from the VC for this one to be marked! Five sentences per paragraph, at the very least.",
  "Only Deltarune has to be muted, you need to hear us after all! Make sure to take a picture of your audio settings and stream it so we can hear it! Or, uh, the lack of it...",
  "You are not allowed to tell the VC that this is on your bingo board, and... don't worry about proving this, it'll be... very obvious.", //30
  "Make sure to take a picture of her melty ass corpse! Or stream the fight!",
  "The rant has to be aggressively long and winding, lasting multiple minutes and disturbing any previous conversation or thoughts you were in the middle of. It'll be kinda obvious, so don't worry about proving it.",
  "Make sure to stream you dicking around and doing nothing for 20 minutes. If I see a damn hint of movement, I'll kick your ass.",
  "You only have to do this if the member is in your party. If they aren't, don't worry about this, unless you want to. ...you don't need to prove this one, it'll be glaringly obvious.",
  "Make sure to take pictures of your Onion encounters!", //35
  "Take a picture of yourself to prove this one! You can censor your face, don't worry.",
  "A timer starts once your break starts that determines how long you have to actively backtrack for when you get back. You can resume playing normally once the timer is up or if you encounter a part you can't backtrack past. Make sure you stream this so it can be verified that you are, in fact, backtracking.",
  "Regardless of how close you were to the next save, you'll have to reload!. Make sure you stream this so it can be verified that you are, in fact, reloading.",
  "Make sure to stream your colorful gameplay!",
  "you can't mark this space and complete your bingo until the fanfiction is completely finished. um. i think. it's pretty obvious. this one i mean. i think we'll know. when you. read it out loud. and stuff.", //40
  "You can skip a chapter and see if anyone notices. If no one notices, you can get away with it! If they do, you have to play the chapter you skipped and the one before it. You kinda have to try NOT to prove this one, hm? ",
  "You can't take this back or reveal that it was on your bingo board. We'll know if you do it.",
  "Make sure to stream this one to prove it.",
  "Make sure it has character designs for main characters and chapter antagonists (Kris, Susie, Ralsei, Noelle, Berdly, King, Queen, Tenna, the Knight, Gerson, the Titan, and Flowery) and a basic outline of what chapters 1-5 would look like. You have to get a 50 percent approval rating from the VC to mark this space.",
  "You have to get in a DM call with someone completely random (spun by wheel), and can't rejoin the main VC until you both beat a chapter. You can't pick someone who's already beaten their race. You have to take a picture of you and your new pal in the DM call to prove this one.", //45
  "You have to take a picture of your watch history to prove this one. A watch party works too.",
  "You have to record each Dogcheck to prove this one.",
  "Throughout your playthrough, build evidence for a Knight identity case and make it at least mildly convincing. Popular Knight candidates are not allowed. You kinda have to tell us the theory. I think. We might know.",
  "You can't take this back or say it was on your bingo board. It'll be pretty obvious if you do this, don't worry about proving it.",
  "Make sure to stream! Solo fights are excluded.",
  "it's pretty fucking obvious",
  "Send pictures of... your Japanese game... we'll know cause... it'll be in... Japanese...",
  "Make sure you stream this one!",
  "Become linked to another person. When that person enters a puzzle, they can only do what you tell them to do, and vice versa. Make sure to communicate in a way that others who aren't part of the link can see or hear.",
  "Make sure to take notes on these choices, you'll be quizzed!", //55
  "Make sure to show off Kris' amazing magic stat to prove this one.",
  "Show us the party's loadout going into Flowery.",
  "just send a image of you doing this like each time",
  "Make sure you remember these Checks! You're gonna be quizzed.",
  "Send us a picture of all those beauties in your storage before Flowery...", //60
  "You're gonna get quizzed on this. By 'act', it's just a section in the Adventure Map, so Intermissions and acts inside acts are included as their own acts. Ask that homestuck nerd if you're confused... you know the one. That homestuck nerd. So disgusting. Ugh, why do I have a throbbing boner?!",
  "You have to use the Deltarune Local Multiplayer Mod and play with a friend via Parsec or other means. The friend must complete their own bingo while you work on yours, and the two of you are now a pseudo-team, sharing the placement in the final ranking as well. If your partner does not complete their bingo by the time you're at the end of the game, even if you finished yours, both of you do not qualify for completion of the race. You can stream it for fun, I guess.",
  "You must watch both parts of 'If Deltarune was Realistic' by SmashBits and show evidence of it being in your watch history (or watch it with everyone in a fun watch party) to mark this space. You are not allowed to have it on in the background while you play. You must watch it and you will be quizzed.",

  // CHAPTER ONE
  "Make sure to record his tale. He'd appreciate it, I think. And you need to prove it.", 
  "Make sure to record it. To prove it.", //65
  "Make sure to record Ralsei's priceless reaction!", 
  "Make sure to take a picture of all their items in your inventory. Why is this game so woke? Always they/thems, where's the he/hims and the she/hers?",
  "Make sure to record this fight. It's probably really funny.", 
  "Make sure to record this fight. It's probably REALLY funny.",
  "Make sure you record the ending!", //70
  "Make sure to record you talking to everyone!", 
  "Make sure you take a picture! Lovely TopCake... fuck im such a hungry bitch im fuckign salivating on to my fucking keyboard",
  "Make sure you take a picture of the build in your favorite file manager. Like uh. File Explorer. And show off the wrist protector! If you were fast enough to get it, that is.", 
  "Stream this one... can't have you sneaking things behind our backs! Johnny johnny yes papa eating sugar no papa telling lies no papa open ur mouth ah ah ah", 
  "Record this one. Try not to let him fucking smite you or whatever irl feats be doing.",  //75
  "Take a picture of your loadout at the end to prove it!", 
  "Dealing damage with Kris, Ralsei, or Susie's normal attack is banned. You must record both fights for this to count.",
  "During Chapter 1, when Lancer ambushes you for the first time, you must die to his assault once before you can get past the encounter. Record yourself dying to him for this to count.",
  "During Chapter 1, you must immediately waste TP on Pacify if you can cast it, even if the enemy is not TIRED. Make sure to stream this!.",
  "When you receive it, throw away the Manual instantly, which will take a few tries due to Ralsei trying to give it back to you. Send a screenshot of the Manual not being in your inventory after you should have received it for this to count.", //80
  "When naming your party in Chapter 1, name yourself the $!$? Squad. Send a screenshot of you choosing this name to prove it!",

  // CHAPTER TWO
  "During the Cyber City, you can recruit the Hacker by collecting the checkmarks, and he'll show up in Castle Town. Send a screenshot of the Hacker in Castle Town for this to count!", 
  "During the Cyber City, you can recruit the Electro-Dasher by not hitting too many of them during the car segment, and they'll show up as in Castle Town. Send a screenshot of the miniature Electro-Dasher in front of Castle Town's Great Door for this to count!", 
  "During the Cyber Field, you can get the Ragger2 by collecting every purple orb leading up to the first Berdly encounter. You must get the Ragger2 and take a screenshot of it being in your inventory for it to count.", 
  "Your playthrough of Deltarune must be a Weird Route playthrough. The exception is Chapter 5, in which you must do a weird playthrough and then a normal playthrough in order to fight Pink, which is required to count as beating the game. In order for this space to count, you must record yourself doing the Chapter 5 lake scene.", //85
  "Your playthrough of Deltarune must be a Weird Route playthrough that gets aborted at the Berdly encounter, meaning he does not get frozen. In order to prove this space, take a screenshot of Noelle having the ThornRing after the Berdly encounter, as if you fail to abort the route here, Noelle will leave the party immediately after the Berdly encounter and you will be unable to get the screenshot.", 
  "When fighting Spamton NEO, you must trigger his hard mode by doing the big shot bug. Record yourself completing the fight this way for this space to count.", 
  "In Queen's Mansion, push the Lancer statue to the table to feed him. You must take a screenshot of him being well fed to prove this space.", 
  "Once you unlock Spamton's shop, you must fill your inventory with S. Poisons. You must then enter a fight and use every one in a single encounter. To prove this space, record yourself doing it.", 
  "During Chapter 2, you are not allowed to collect and use any armor or weapons from the chapter. To prove this, you must take a screenshot of your post-chapter inventory, showing that you have no Chapter 2 armors or weapons.", //90
  "Throughout Chapter 2, you are not allowed to pick up any Chapter 2 items or use any items from Chapters 1. You must take a screenshot of your post-Chapter 1 inventory and your post-Chapter 2 inventory, showing that they're identical, for this space to count.", 
  "When fighting Spamton NEO, you must avoid firing a big shot (except for in the tutorial). In order to prove this space, you must record yourself completing the entire fight without firing a big shot.", 
  "During Queen's Mansion, taunt Berdly with the 'appealing blue shape'. Take a screenshot of you doing this.",
  "When Noelle enters your party in Chapter 2, give her your best armors and don't take them off her. She will leave the party and take them with her. Take a screenshot of the armors you gave her to prove this space, along with the lack of them from your inventory after she leaves.",

  // CHAPTER THREE
  "During any board in Chapter 3, you must get an S-Rank as your final result. You must take a screenshot of your results screen to prove this one.", //95
  "During any board in Chapter 3, you must get a Z-Rank as your final result. You must take a screenshot of your results screen to prove this one.", 
  "During the Desert Board, you must collect all 5 keys. You must take a screenshot of all 5 keys being in your inventory, or getting the bonus for collecting both extra keys.", 
  "In Chapter 3, you must unlock Susiezilla and complete it all the way through at least once. You must take a screenshot of the results screen to prove this one.",
  "In the C-Rank room, trigger the 1225 secret in the Gacha machine. You must take a screenshot of the secret to prove this space.", 
  "During TV World, you must go to the Bonus Zone. You do not have to trigger the cutscene with Spamton. Take a screenshot of your party standing in the Bonus Zone for this space to count.", //100
  "During the Rouxls Kaard encounter in Chapter 3, you must at some point trigger the dog button to appear and use it at least once. You must take a screenshot of the dog button or the resulting cutscene to prove this space.", 
  "During Chapter 3, you are not allowed to collect and use any armor or weapons from the chapter. To prove this, you must take a screenshot of your post-chapter inventory, showing that you have no Chapter 3 armors or weapons.", 
  "Throughout Chapter 3, you are not allowed to pick up any Chapter 3 items or use any items from Chapters 1 and 2. You must take a screenshot of your post-Chapter 2 inventory and your post-Chapter 3 inventory, showing that they're identical, for this space to count.",
  "When naming your podium in Chapter 3, type in 'ASS'. You must take a screenshot of your podium to prove this one.",
  "When you fight Tenna, the only thing you are allowed to do to gain score is Kris' ILoveTV. No minigames are permitted, nor usage of Ralsei or Susie's acts.", //105
  "When in the Desert Board, every Quiz you must do must be 100%. If you miss a question, you have to reload the board and start over immediately. You must screenshot your results for each quiz to prove this space.",

  // CHAPTER FOUR 
  "Your playthrough of Deltarune must be a Weird Route that gets aborted during Chapter 4. You must record yourself aborting the route to prove it.", 
  "During the Gerson fight, whenever you have the TP for it, you must use Rude Buster and complete the full parry chain. You must record this fight fully to prove you did it.",
  "When you are at the big piano in Chapter 4, you must do at least five hidden melody secrets. You must record yourself doing this fully.", 
  "When you get the chance during Chapter 4, you must fight the Mikes. Send a screenshot of yourself at the end of the Mike fight to prove this space.", //110
  "During the Holiday manor segment in Chapter 4, you must record Kris' entire phone call as they pour themselves the chocolate milk. The recording will prove completion of the space.", 
  "You must donate to the fountain in Chapter 4 and receive the GoldWidow later on. You must send a screenshot of you having the GoldWidow to prove this one.",
  "You must do the dog race in Chapter 4 and receive the DogDollar. You must send a screenshot of you having the DogDollar in your inventory to prove this space.", 
  "During the Gerson and Sound of Justice fights, you are only allowed to point your shield up and down. To prove this, you must record both fights. In the Gerson fight, diagonals are not allowed.", 
  "During Chapter 4, you are not allowed to collect and use any armor or weapons from the chapter. To prove this, you must take a screenshot of your post-chapter inventory, showing that you have no Chapter 4 armors or weapons.", //115
  "During Chapter 4, you are not allowed to pick up any Chapter 4 items or use any items from Chapters 1-3. To prove this one, you must send a screenshot of your post-Chapter 3 inventory and post-Chapter 4 inventory, proving them to be identical.",
  "When Susie opens the Dark Fountain in Chapter 4, you must record yourself mimicking the animation in real life. You may censor your face. You must be all in, even doing a full jump and having a weapon. The video you take will prove this space.",

  // CHAPTER FIVE
  "Your playthrough of Deltarune must be a Weird Route playthrough that is aborted at Chapter 5. In order to prove this one, you must take a screenshot of the route abortion cutscene.", 
  "During Chapter 5's Castle Town segment, you must make Susie's outfit for the festival full duck. You must send a screenshot of Susie wearing the duck outfit to count this space. ", 
  "When Flowery gives you the chest with infinite currency, you must go out of your way to collect at least 100 F$. In order to prove this one, you must show that your inventory has 100 F$ after collecting them all from the infinite chest, as this is the first instance of you collecting Flowery dollars.", //120
  "During the Pink fight, you must die to her once to be able to change the bomb settings, and choose meaner bombs. You must record yourself doing the entire Pink fight like this to prove it.", 
  "Throughout your playthrough of Chapter 5, you must collect all the Pink Coins. In order to prove this one, you must show that you have one pink coin left over after buying the three flower items, or show that you used up the last pink coin.", 
  "During Chapter 5, when you do the scene at the lake (normal or weird), you must go find any form of water and take a photo of it. Water that comes in man-made forms, such as bottled water or sink water, is okay.", 
  "During Chapter 5, when you hear the beat drop during 'Sunset of Seven Suns', you must immediately leave and go take a picture of the sun. You do not have to do this multiple times. You must leave your house to do so - no window photos. Send the photo you took of the sun to prove it.", 
  "During the Festival, you must go to every attraction and pick Susie and Noelle to do them. You must record your festival segment to prove it.", //125
  "During the Festival, you must go to every attraction and pick Kris and Susie to do them. You must record your festival segment to prove it.", 
  "During the Festival, you must go to every attraction and pick Kris and Noelle to do them. You must record your festival segment to prove it.", 
  "During Chapter 5's Castle Town segment, you must go out of your way to do 4rd Sanctuary. You do not have to do a full combo. Send a recording of yourself doing 4rd Sanctuary to prove it.", 
  "You are only allowed to use Kris' regular Flirt act during the Pink fight. MegaFlirt, GigaFlirt, GigaFlirtX, as well as Susie and Ralsei's acts, are all banned. You must record yourself doing the whole fight like this to prove that you did it.", 
  "During Chapter 5, if you die to Pink at any point, you must immediately stop your playthrough and record yourself singing the entirety of chai's Cutie Mew Mew Magic with lyrics. You may mark this space if you first try Pink. You must prove this one by sending the audio recording OR do a full recording from the moment you use the MysteryKey to the end of the Pink fight to prove you did it deathless.", //130
  "After fighting Pink, you must trigger her shop dialogue where she warns you about cats and protein. To prove this one, you must take a screenshot of Pink's dialogue.",
  "During Chapter 5, when Flowery is briefly in your party, you must feed him all of your items. This does not include items in your storage, however you cannot tactically put items in your storage that you wish to preserve before doing this. You must send a screenshot of an empty inventory with Flowery in your party to prove this space.", 
  "During Chapter 5, you are limited to only use weapons and armor that you obtained during Chapter 4, and cannot pick up any Chapter 5 weapons or armor. You must screenshot your armors and weapons after Chapter 5 to prove that no Chapter 5 armors or weapons have entered your inventory.", 
  "During Chapter 5, you must end every encounter by tiring every enemy and using Susie's Scythemare spell. You should stream this!",
  "During Chapter 5, you must complete the entire chapter without picking up a single item or using any items from before Chapter 5. You must prove this one by taking a screenshot of your post-Chapter 4 inventory and then taking a screenshot of your post-Chapter 5 inventory, showing that they match.", //135
  "During Chapter 5, every time a flower says they're going to use their Omega, you must immediately boot up Undertale to fight Omega Flowey all the way through. This includes if you reload Chapter 5 and encounter the same Omega again. Make sure to stream this one! Flowey's Time Machine is permitted and encouraged.",
  "During the Flowery fight in Chapter 5, any time the lyrics come on for Flower Man, you must sing along, even if it disorients you from the fight. If you do the Weird Route, you cannot mark this space unless you do a normal playthrough of Chapter 5 and fight Flowery there. There is no need to provide evidence for this one, we'll hear you.",
  "Once you start Chapter 5, the only sentence you are permitted to say are ones that Flowery has voice lines for. This includes using text chats. If at any point you break this rule, you become illegible for the space. There is no need to provide evidence for this one, we'll hear you."
};
const int easyDescLen = sizeof easyDesc / sizeof *easyDesc;

const char* hardDesc[] = {
  "Beat Undertale: Last Breath at some point during the race and take a screenshot of you in the Last Corridor after killing Sans if you want to prove it... or stream it.", //0
  "You have to keep the same stupid loadout from the start of the first Chapter. Stream your playthrough if you want to prove it so we can watch you get knocked down by a random gust of wind... or take a picture before Flowery. That works too.", 
  "You have to complete an FDY fangame fully. Noob Mode is not allowed. Record yourself doing the fight for this to count, or stream it!", 
  "Stream you beating Sans or take a recording of the whole damn thing to prove it. This has to be in a row.", 
  "Archipelago works on a randomizer on its own. If you want to prove it, send a picture of the multiworld server log, or stream it!", 
  "Make sure to stream your gameplay with one of those little on-screen key showing programs on the screen.", //5
  "You'll have to stream your game for this one to be proved... get ready for a speedwalk! (heh, get it? like... like speedrun... eheh...)", 
  "This will hurt. Make sure the person you switched with says something so you can prove you did it! And... uh... streaming probably works too, huh?", 
  "Take a picture of your save after completion to prove this one.", 
  "That's weird... you could have sworn there was a bingo space here, but it's gone. Looks like you can't complete any bingos where this space would have been.",
  "Start on a blank canvas and draw the enemies on that canvas. Repeats are included. Make sure to show us your incredible art every time you draw another one!", //10
  "You have to draw the overworld idle and walking sprites, dark world idle, walking, and battle sprites, and all the portraits. ...I think proving this is pretty easy, just show us. It'll come up naturally in your other screenshots too, I think.",
  "Make sure to take a picture of your brightness settings! Like, with your phone or something if you can't turn it down through software... if you can mess with your monitor like that...",
  "What? You want me to read their mind and tell you how to prove it? Man, ask them!",
  "this is gonna fuck you over later lol",
  "Make sure to stream this!", //15
  "Make sure to stream this!",
  "Make sure to stream this!",
  "Make sure to stream this!",
  "Make sure you stream getting cracked Toriel-style because of this fuckass mod.",
  "Make sure you take a picture of the end, you don't want this to be unproveable! Or stream it.", //20
  "If they win, they steal your place from you and you automatically place after them. Make sure to record this awesome fight.",
  "Take pictures of all the killer result screens here to prove it! You can stream it, too.",
  "Make sure to stream your game if you're doing this! You can move your soul if you end up dying to the same encounter three times in a row. You can still shoot and dash and such, though!",
  "you will literally lose the race if you do this so there's not really a point in proving this one",
  "Make sure to take a picture of your loadout before Flowery!", //25
  "Every single bingo space on this bingo (except this one) must be completed on its own save file. You may use one save file for two spaces. You must send a screenshot of each one of your save files for this space to count.",

  // CHAPTER ONE
  "Attacking with Susie and Kris is completely banned. You must record both fights for this to count.",
  "You must no-hit the King fight, and if you take damage, you must reload immediately. You must record the King fight for this to count.", //28

  // CHAPTER THREE
  "During any board in Chapter 3, you must get a T-Rank as your final result. You must take a screenshot of your results screen to prove this one.", 
  "In Chapter 3, you must defeat the Knight without using the ShadowMantle. To prove this one, record yourself before the battle showing having no mantle equipped before going into the fight and completing it. you still need it in your inventory though, lol", //30
  "In Chapter 3, you must patch the Kaizo Knight mod into your game and complete it. You must take a screenshot of the Kaizo Knight battle to prove this one.", 
  "When doing the physical challenge of Board 2, you must full combo the whole thing. If you miss a single note, you must immediately reset and try again. In order to prove completion of this space, you must record yourself doing the full combo.",
  
  // CHAPTER FOUR
  "Once you complete Chapter 4, you must install the Ultimate Boss Rush mod and complete Super Mega Ultimate Boss Rush, which is a gauntlet consisting of every miniboss, main boss, and secret boss. You must screenshot yourself being at the end of the boss rush for this space to count.",
  
  // CHAPTER FIVE
  "You must install and use Determination Flowery during the Flowery fight. If you do the Weird Route, you are illegible for this space as you do not fight Flowery, unless you go out of your way to do a normal Chapter 5 completion as well. Take a screenshot of Determination Flowery to prove",
  "During Chapter 5, you must complete the entire Flowery fight without charging up the soul to do a dash. This includes the tutorial, where you will have to tank four of the blue bamboo sticks. You must prove this one by recording your fight.", //35
  "During Chapter 5, when Seth and Aqua use the duck attack, you must purposefully go out of your way to die to it, even though it only deals 1 DMG at a time. You may purposefully enter the fight with low HP intending to die to it. Take a screenshot of the duck closing in on you once you have 1 HP left to prove you completed this space."
};
const int hardDescLen = sizeof hardDesc / sizeof *hardDesc;
