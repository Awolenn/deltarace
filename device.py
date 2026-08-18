# --- IMPORTS START --- #
from pyray import *
# MODULES ^^^ vvv FILES
import funvalues as fun
import gonermaker
# --- IMPORTS END --- #

# --- WINDOW START --- #
init_window(fun.windowWidth, fun.windowHeight, "CONNECTION ESTABLISHED .")
set_trace_log_level(4)
monoFont = load_font("DTM-Mono.otf")
sansFont = load_font("DTM-Sans.otf")
while not window_should_close():
    # --- MAIN LOOP START --- #
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        set_target_fps(15) 
        fun.dialoguePartOne(fun.gasterMessages)
        # when dialogue concludes, change to the next screen.
        if fun.messageCount == len(fun.gasterMessages)-1:
            fun.messageCount = 0
            fun.currentScreen = 1

    # SCREEN 1 ; OTHER DIALOGUE
    if fun.currentScreen == 1:
        set_window_title(" ")
        set_target_fps(10)
        fun.dialoguePartOne(fun.otherMessages)
        # part of the fade to white.
        if fun.messageCount >= 2:
            print(fun.opacity)
            fun.opacity += .028

        # when the fade to white completes, next screen.
        if fun.opacity >= 1:
            fun.messageCount = 0
            fun.opacity = 0
            fun.currentScreen = 2

    # SCREEN 2 ; BINGO CARD
    if fun.currentScreen == 2:
        set_window_title("SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!")
        set_target_fps(60)
        for cardCounter in range(25):
            for col in range(1, 6):
                for row in range(1, 6):
                    fun.makeCardPartOne(row, col, ((row-1)+(col-1)*5))
        fun.makeCreditsPartOne()
    
    # SCREEN 3 ; CREDITS
    elif fun.currentScreen == 3:
        fun.makeCreditsPartOne()
    
    # SCREEN 4 ; THERE'S A ROOM INBETWEEN
    elif fun.currentScreen == 4:
        set_window_title(" ")
        set_target_fps(20)
        fun.dialoguePartOne(fun.forgottenMessages)
        if fun.messageCount == len(fun.gasterMessages)-1:
            fun.messageCount = 0
            fun.currentScreen = 2

    # --- DRAWING START --- #
    begin_drawing()
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        clear_background(BLACK)
        fun.dialoguePartTwo(monoFont, fun.gasterMessages, 0, 0, fun.windowWidth, fun.windowHeight, 3, 10, WHITE)

    # SCREEN 1 ; OTHER DIALOGUE
    elif fun.currentScreen == 1:
        fun.clearText(BLACK)
        fun.dialoguePartTwo(monoFont, fun.otherMessages, 0, 0, fun.windowWidth, fun.windowHeight, 2, 0, WHITE)
        if fun.messageCount == 2:
            fun.clearText(fade(WHITE, fun.opacity))

    # SCREEN 2 ; BINGO CARD
    elif fun.currentScreen == 2:
        # buffer clearing... oh i sound so smart saying buffer.
        clear_background(RAYWHITE)
        # this is the fun aesthetic stuff, really. i guess none of it is required, but it's nice. it gets rendered before the cards because. i said so.
        draw_rectangle(0, 600, fun.windowWidth, 100, GRAY)
        draw_text_ex(sansFont, "SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!", [290, 600], fun.standardFontSize*2, 1, GREEN)
        draw_text_ex(sansFont, "you only win the race if you beat all chapters and secret bosses\nAND fill outa bingo! for the easiest time verifying your bingo,\nstream your playthrough! hover over a card for details.", [290, 630], fun.standardFontSize*1, 0, GREEN)
        draw_rectangle(0, 0, 280, fun.windowHeight, BLACK)
        if fun.visitedEggRoom:
            draw_circle(70, 70, 5, MAROON)
        # drawing the cards. might change a little for aesthetic purposes but holy fuck i don't want to do that lol.
        for col in range(1, 6):
            for row in range(1, 6):
                fun.makeCardPartTwo(row, col, ((row-1)+(col-1)*5), sansFont, monoFont)
        fun.makeCreditsPartTwo(sansFont)
    
    # SCREEN 3 ; CREDITS
    elif fun.currentScreen == 3:
        fun.clearText(RAYWHITE)
        draw_rectangle(0, 530, fun.windowWidth, 170, BLACK)
        fun.makeCreditsPartTwo(sansFont)
    
    # SCREEN 4 ; THERE'S A ROOM INBETWEEN
    elif fun.currentScreen == 4:
        fun.clearText(RED)
        draw_rectangle(30, 490, 840, 200, WHITE)
        draw_rectangle(40, 500, 820, 180, BLACK)
        fun.dialoguePartThree(monoFont, fun.forgottenMessages, 50, 520, 1, 0, WHITE)
        fun.visitedEggRoom = True

    end_drawing()
    # --- DRAWING END --- #
    # --- MAIN LOOP END --- #
close_window()
# --- WINDOW END --- #