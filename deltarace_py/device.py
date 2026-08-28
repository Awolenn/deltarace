# --- IMPORTS START --- #
from pyray import *
# MODULES ^^^ vvv FILES
import funvalues as fun
import gonermaker
import ctypes as ct
# --- IMPORTS END --- #

# --- WINDOW START --- #
# initilizing everything
init_window(fun.windowWidth, fun.windowHeight, "CONNECTION ESTABLISHED .")
init_audio_device()
set_trace_log_level(4) # preventing log spam
# image loading
fun.loadEggRooms()
temp = load_image("DONOTENTERPLEASE/depthsPartOne.png")
depthsA = load_texture_from_image(temp)
temp = load_image("DONOTENTERPLEASE/depthsPartTwo.png")
depthsB = load_texture_from_image(temp)
temp = load_image("DONOTENTERPLEASE/credits.png")
creditsImage = load_texture_from_image(temp)
temp = load_image("DONOTENTERPLEASE/Egg_item.png")
eggImage = load_texture_from_image(temp)
# sound loading
man = load_sound("DONOTENTERPLEASE/man.ogg")
anotherhim = load_sound("DONOTENTERPLEASE/AUDIO_ANOTHERHIM.ogg")
w = load_sound("DONOTENTERPLEASE/w.ogg")
eggSound = load_sound("DONOTENTERPLEASE/snd_egg.wav")
clickSound = load_sound("DONOTENTERPLEASE/snd_noise.wav")
winSound = load_sound("DONOTENTERPLEASE/snd_won.wav")
# font loading
monoFont = load_font("DONOTENTERPLEASE/DTM-Mono.otf")
sansFont = load_font("DONOTENTERPLEASE/DTM-Sans.otf")
wingdingding = load_font("DONOTENTERPLEASE/Wingdings-Regular.ttf")

while not window_should_close():
    # --- MAIN LOOP START --- #
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        set_target_fps(15)
        if is_sound_valid(anotherhim) and not is_sound_playing(anotherhim):
            play_sound(anotherhim)
        fun.dialoguePartOne(fun.gasterMessages)
        # part of the glowing text.
        if fun.opacity >= 1:
            fun.getBrighter = False

        elif fun.opacity <= 0:
            fun.getBrighter = True
        
        if fun.getBrighter:
            fun.opacity += .05

        elif not fun.getBrighter:
            fun.opacity -= .05
        
        # the depths effect... my attempt, at least.
        if fun.depthsOpacity >= 1:
            fun.depthsGetBrighter = False

        elif fun.depthsOpacity <= 0:
            fun.depthsGetBrighter = True
        
        if fun.depthsGetBrighter:
            fun.depthsOpacity += .01

        elif not fun.depthsGetBrighter:
            fun.depthsOpacity -= .01

        # when dialogue concludes, change to the next screen.
        if fun.messageCount == len(fun.gasterMessages)-1:
            fun.messageCount = 0
            fun.currentScreen = 1
            fun.opacity = 0

    # SCREEN 1 ; OTHER DIALOGUE
    if fun.currentScreen == 1:
        set_window_title(" ")
        set_target_fps(10)
        stop_sound(anotherhim)
        fun.dialoguePartOne(fun.otherMessages)
        # part of the fade to white.
        if fun.messageCount >= 2:
            if is_sound_valid(w) and not is_sound_playing(w):
                play_sound(w)
            fun.opacity += .02

        # when the fade to white completes, next screen.
        if fun.opacity >= 1:
            fun.messageCount = 0
            fun.opacity = 0
            fun.currentScreen = 2

    # SCREEN 2 ; BINGO CARD
    elif fun.currentScreen == 2:
        set_window_title("SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!")
        stop_sound(w)
        stop_sound(man)
        set_target_fps(60)
        for col in range(1, 6):
            for row in range(1, 6):
                fun.makeCardPartOne(row, col, clickSound, ((row-1)+(col-1)*5))
        fun.makeCreditsPartOne(clickSound, eggSound)
        fun.possibleBingoWinCheck(winSound)
    
    # SCREEN 3 ; CREDITS
    elif fun.currentScreen == 3:
        set_window_title("SADIE AND SAM'S SUPER SAUCY CREDITS!")
        set_target_fps(60)
        fun.makeCreditsPartOne(clickSound, eggSound)
    
    # SCREEN 66 ; THERE'S A ROOM INBETWEEN
    elif fun.currentScreen == 66:
        set_window_title(" ")
        set_target_fps(20)
        fun.dialoguePartOne(fun.forgottenMessages)
        if fun.messageCount == len(fun.forgottenMessages)-1:
            fun.messageCount = 0
            fun.currentScreen = 2

        if is_sound_valid(man) and not is_sound_playing(man):
            set_sound_volume(man, 1)
            play_sound(man)

    begin_drawing()
    # --- DRAWING START --- #
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        clear_background(BLACK)
        draw_texture_ex(depthsB, [-30, 0], 0, 3, GRAY)
        draw_texture_ex(depthsA, [-30, 0], 0, 3, fade(WHITE, fun.depthsOpacity))
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 200, 152, fun.windowWidth-300, fun.windowHeight-252, 3, 10, BLACK) # BELOW
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 200, 152, fun.windowWidth-300, fun.windowHeight-252, 3, 10, fade(WHITE, fun.opacity)) # BELOW PART 2
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 200, 148, fun.windowWidth-300, fun.windowHeight-248, 3, 10, BLACK) # ABOVE
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 200, 148, fun.windowWidth-300, fun.windowHeight-248, 3, 10, fade(WHITE, fun.opacity)) # ABOVE PART 2
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 198, 150, fun.windowWidth-298, fun.windowHeight-250, 3, 10, BLACK) # LEFT
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 198, 150, fun.windowWidth-298, fun.windowHeight-250, 3, 10, fade(WHITE, fun.opacity)) # LEFT PART 2
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 202, 150, fun.windowWidth-302, fun.windowHeight-250, 3, 10, BLACK) # RIGHT
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 202, 150, fun.windowWidth-302, fun.windowHeight-250, 3, 10, fade(WHITE, fun.opacity)) # RIGHT PART 2
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 200, 150, fun.windowWidth-300, fun.windowHeight-250, 3, 10, WHITE)

    # SCREEN 1 ; OTHER DIALOGUE
    elif fun.currentScreen == 1:
        fun.clearText(BLACK)
        fun.dialoguePartTwo(monoFont, fun.otherMessages, 200, 100, fun.windowWidth-300, fun.windowHeight-200, 3, 0, WHITE)
        if fun.messageCount == 2:
            fun.clearText(fade(WHITE, fun.opacity))

    # SCREEN 2 ; BINGO CARD
    elif fun.currentScreen == 2:
        # buffer clearing... oh i sound so smart saying buffer.
        clear_background(fun.deeperBlueGray)
        # this is the fun aesthetic stuff, really. i guess none of it is required, but it's nice. it gets rendered before the cards because. i said so.
        draw_rectangle(0, 600, fun.windowWidth, 100, fun.darkBlue)
        draw_text_ex(sansFont, "SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!", [290, 600], fun.standardFontSize*2, 1, BLUE)
        draw_text_ex(sansFont, "you only win the race if you beat all chapters and secret bosses\nAND fill outa bingo! for the easiest time verifying your bingo,\nstream your playthrough! hover over a card for details.", [290, 630], fun.standardFontSize*1, 0, BLUE)
        draw_rectangle(0, 0, 280, fun.windowHeight, WHITE)
        # drawing the cards. might change a little for aesthetic purposes but holy fuck i don't want to do that lol.
        for col in range(1, 6):
            for row in range(1, 6):
                fun.makeCardPartTwo(row, col, ((row-1)+(col-1)*5), sansFont, monoFont)
        fun.makeCreditsPartTwo(sansFont, eggImage)
    
    # SCREEN 3 ; CREDITS
    elif fun.currentScreen == 3:
        fun.clearText(RAYWHITE)
        draw_texture_ex(creditsImage, [110, 0], 0, .5, WHITE)
        draw_text_ex(sansFont, "also thanks to:\ndeltarune dev team (made this possible, music, sounds, assets, etc.)\nkolibri (helped me program and ported everything to C thanks dude ily)\nraylib dev team (i'm using it)\npython raylib bindings devs (i'm also using it)\n@JapanYoshi on behance.net (this awesome font)", [5, 0], fun.standardFontSize*1, 1, BLACK)
        if fun.isCursorInCard(150, 210, 150+260, 210+270):
            draw_text_ex(sansFont, "SAM", [240, 140], fun.standardFontSize*4, 1, BLACK)
            draw_text_ex(sansFont, "he/they/neos\nalso known as reaper or awolen\nguy who made this.\nprogrammer, gave some ideas for\nbingo cards but not a lot.", [150, 480], fun.standardFontSize*1, 1, BLACK)
        if fun.isCursorInCard(470, 240, 470+290, 240+300):
            draw_text_ex(sansFont, "SADIE", [550, 170], fun.standardFontSize*4, 1, BLACK)
            draw_text_ex(sansFont, "she/any\nalso known as amelia or talistelis\ngal who made this.\ngave most of the bingo card ideas, drew\nthis awesome art.", [470, 540], fun.standardFontSize*1, 1, BLACK)
        fun.makeCreditsPartTwo(sansFont, eggImage)
    
    # SCREEN 66 ; THERE'S A ROOM INBETWEEN
    elif fun.currentScreen == 66:
        fun.clearText(BLACK)
        fun.animateEggRoom()
        draw_rectangle(40, 490, 840, 190, WHITE)
        draw_rectangle(50, 500, 820, 170, BLACK)
        fun.dialoguePartThree(monoFont, fun.forgottenMessages, 70, 520, 2.5, 0, WHITE)
        fun.visitedEggRoom = True

    # --- DRAWING END --- #
    end_drawing()

# --- MAIN LOOP END --- #
# killing things and whatnot
close_window()
close_audio_device()
# --- WINDOW END --- #