# --- IMPORTS START --- #
from pyray import *
import generation
import time
# --- IMPORTS START --- #

# --- CONSTANTS START --- #
windowSize = 800
gasterMessages = ["", "ARE YOU\n\nTHERE ?", " ARE WE\n\nCONNECTED ?", "EXCELLENT .", "TRULY\n\nEXCELLENT .", "NOW .", "ARE YOU\n\nEXCITED ?", "TO RACE\n\nIN MY\n\nDELTARUNE ?", "YOUR SKILLS .\n\nYOUR WONDERFUL\n\nPLANNED OUT\n\nSTRATEGY .", ""]
otherMessages = ["Will now be discarded.", "No one will just play Deltarune\nwithout a twist in this group chat.", "Your\n\n\nbingo card\n\n\nis"]
# --- CONSTANTS END --- #

# --- INITIAL VARIABLES START --- #
framesCounter = 0
messageCount = 0
otherMessageCount = 0
currentScreen = 0
# --- INITIAL VARIABLES START --- #

init_window(windowSize, windowSize, "HELLO.")
set_target_fps(10)
while not window_should_close():
    # --- THE STUPID FUCKING ZONE START --- #
    if currentScreen == 0:
        # REMOVE THE SKIP WHEN YOURE DONE DEBUGGING
        if is_key_down(KEY_SPACE) == True:
            framesCounter += 8
        else: 
            framesCounter += 1
        if is_key_pressed(KEY_ENTER) == True:
            framesCounter = 0
        if messageCount == 9:
            messageCount = 0
            currentScreen = 1
        if is_key_pressed(KEY_Z) == True:
            if framesCounter >= len(gasterMessages[messageCount]):
                messageCount += 1
                framesCounter = 0
    if currentScreen == 1:
        if is_key_down(KEY_SPACE) == True:
            framesCounter += 8
        else: 
            framesCounter += 1
        if is_key_pressed(KEY_ENTER) == True:
            framesCounter = 0
        if is_key_pressed(KEY_Z) == True:
            if otherMessageCount == 2:
                otherMessageCount = 0
            else:
                otherMessageCount += 1
            framesCounter = 0
    # --- THE STUPID FUCKING ZONE END --- #

    # --- DRAWING START --- #
    begin_drawing()
    if currentScreen == 0:
        clear_background(BLACK)
        draw_text(text_subtext(gasterMessages[messageCount], 0, framesCounter), 100, 200, 40, WHITE)
    elif currentScreen == 1:
        draw_rectangle(0, 0, windowSize, windowSize, WHITE)
        draw_text(text_subtext(otherMessages[otherMessageCount], 0, framesCounter), 50, 200, 40, BLACK)
        print(otherMessageCount)
    end_drawing()
    # --- DRAWING END --- #
close_window()