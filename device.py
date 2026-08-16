# --- IMPORTS START --- #
from pyray import *
# MODULES ^^^ vvv FILES
import funvalues as fun
import gonermaker
# --- IMPORTS END --- #

# --- WINDOW START --- #
init_window(fun.windowWidth, fun.windowHeight, "CONNECTION ESTABLISHED .")
set_target_fps(60)
while not window_should_close():
    # --- MAIN LOOP START --- #
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        set_target_fps(10)
        fun.dialoguePartOne(fun.gasterMessages)

    # SCREEN 1 ; OTHER DIALOGUE
    if fun.currentScreen == 1:
        set_window_title(" ")
        set_target_fps(10)
        fun.dialoguePartOne(fun.otherMessages)

    # SCREEN 2 ; BINGO CARD
    if fun.currentScreen == 2:
        set_window_title("SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!")
        for cardCounter in range(25):
            for col in range(1, 6):
                for row in range(1, 6):
                    fun.makeCardPartOne(row, col, ((row-1)+(col-1)*5))

    # --- DRAWING START --- #
    begin_drawing()
    # SCREEN 0 ; GASTER DIALOGUE
    if fun.currentScreen == 0:
        clear_background(BLACK)
        fun.dialoguePartTwo(fun.gasterMessages, 100)

    # SCREEN 1 ; OTHER DIALOGUE
    elif fun.currentScreen == 1:
        fun.clearText(BLACK)
        fun.dialoguePartTwo(fun.otherMessages, 50)

    # SCREEN 2 ; BINGO CARD
    elif fun.currentScreen == 2:
        # buffer clearing... oh i sound so smart saying buffer.
        clear_background(WHITE)
        # drawing the cards. will likely change for aesthetic purposes.
        for col in range(1, 6):
            for row in range(1, 6):
                fun.makeCardPartTwo(row, col, ((row-1)+(col-1)*5))
        # this is the fun aesthetic stuff, really. i guess none of it is required, but it's nice.
        draw_rectangle(0, 810, fun.windowWidth, 200, BLACK)

    end_drawing()
    # --- DRAWING END --- #
    # --- MAIN LOOP END --- #
close_window()
# --- WINDOW END --- #