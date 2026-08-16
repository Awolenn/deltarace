# --- IMPORTS START --- #
from pyray import *
import gonermaker as goner
# --- IMPORTS END --- #

# --- CONSTANTS START --- #
windowWidth = 1000
windowHeight = 1010
cardSize = 150
cardMargin = 10
fullCard = cardSize + cardMargin
# REGULAR ^^^ vvv DIALOGUE LISTS
gasterMessages = ["", "ARE YOU\n\nTHERE ?", "ARE WE\n\nCONNECTED ?", "EXCELLENT .", "TRULY\n\nEXCELLENT .", "NOW .", "ARE YOU\n\nEXCITED ?", "TO RACE\n\nIN MY\n\nDELTARUNE ?", "YOUR SKILLS .\n\nYOUR WONDERFUL\n\nPLANNED OUT\n\nSTRATEGY .", ""]
otherMessages = ["Will now be discarded.", "No one will just play Deltarune\nwithout a twist in this group chat.", "Your\n\n\nbingo card\n\n\n\nis", ""]
# DIALOGUE LISTS ^^^ vvv CARD-SPECIFIC LISTS
squaresMarked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
squareColor = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
cardText = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
# --- CONSTANTS END --- #

# --- INITIAL VARIABLES START --- #
currentScreen = 2 # RESET TO ZERO ONCE YOU'RE DONE TESTING!
framesCounter = 0
messageCount = 0
# DIALOGUE STUFF ^^^ vvv BINGO STUFF
cardPartOneCounter = 0
cardPartTwoCounter = 0
# --- INITIAL VARIABLES END --- #

# --- FUNCTIONS START --- #
def dialoguePartOne(dialogue):
    """Allows proceeding through dialogue.
    
    dialoguePartTwo should be included inside the "drawing" portion of the code of this is present to ensure full functionality, but I'm not your dad.

    Args:
        dialogue (str[]): The list containing strings to be used for dialogue.
    """
    global framesCounter
    global currentScreen
    global messageCount
    # vvv DEBUGGING FEATURES, PLEASE REMOVE vvv
    if is_key_down(KEY_SPACE):
        framesCounter += 8
    else: 
        framesCounter += 1
    if is_key_pressed(KEY_ENTER):
        framesCounter = 0
    # ^^^ DEBUGGING FEATURES, PLEASE REMOVE ^^^
    # when dialogue concludes, change to the next screen.
    if messageCount == len(dialogue)-1:
        messageCount = 0
        currentScreen += 1
    # when "Z" is pressed, continue to the next string in the list.
    # additionally, only allow continuing once the string is finished.
    if is_key_pressed(KEY_Z):
        if framesCounter >= len(dialogue[messageCount]):
            messageCount += 1
            framesCounter = 0

def dialoguePartTwo(dialogue, xPosition):
    """Form dialogue from a list.

    dialoguePartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.
    
    Args:
        dialogue (str[]): The list containing strings to be used for dialogue.
        xPosition (int): The X position of the text.
    """
    draw_text(text_subtext(dialogue[messageCount], 0, framesCounter), xPosition, 200, 40, WHITE)

def clearText(color):
    """Clear text from the screen.
    
    Args:
        color (raylib.color): The color you want the screen to be.
    """
    draw_rectangle(0, 0, windowWidth, windowHeight, color)

# DIALOGUE ^^^ vvv CARDS

def leftLimit(col):
    """Define the leftmost limit of the card.

    Args:
        col (int): The column the card is in.
    """
    return fullCard*(col-1)+200

def upLimit(row):
    """Define the upper limit of the card.

    Args:
        row (int): The row the card is in.
    
    Returns:
        int: The upper limit of the card.
    """
    return fullCard*(row-1)+10

def isClickingCard(leftLimit, upLimit, rightLimit, downLimit):
    """Checks if a card is being clicked.
    
    Args:
        leftLimit (int): The leftmost limit of the card.
        upLimit (int): The upper limit of the card.
        rightLimit (int): The rightmost limit of the card.
        downLimit (int): The lower limit of the card.

    Returns:
        bool: If the cursor is in the card or not.
    """
    return get_mouse_x() >= leftLimit and get_mouse_x() <= rightLimit and get_mouse_y() >= upLimit and get_mouse_y() <= downLimit and is_mouse_button_pressed(MOUSE_BUTTON_LEFT)

def allLimits(col, row):
    """Gets all of the limits of a card. Intended to be deconstructed.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
    
    Returns:
        tuple (int, int, int, int): The limits of the card in order of leftmost, upper, rightmost, and lower.
    """
    return (leftLimit(col), upLimit(row), cardSize+leftLimit(col), cardSize+upLimit(row))

def makeCardPartOne(col, row, card):
    """Makes the cards capable of being marked.

    makeCardPartTwo should be included inside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
        card (int): The unique number of the card.
    """
    # check if a card is being clicked to begin with, and if so, what card specficially. 
    # the card should be inside of the limits. if it isn't. that's bad.
    if isClickingCard(*allLimits(col, row)):
        # if square isn't marked, mark it.
        if not squaresMarked[card]:
            squareColor[card] = RED
            squaresMarked[card] = True
        # if square is marked, unmark it.
        elif squaresMarked[card]:
            squareColor[card] = BLACK
            squaresMarked[card] = False

def makeCardPartTwo(col, row, card):
    """Draws the cards to the screen.

    makeCardPartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
        card (int): The unique number of the card.
    """
    draw_rectangle(leftLimit(col), upLimit(row), cardSize, cardSize, squareColor[card]) # draw the card itself. the color is a variable so it can be modified when marked.
    draw_text(goner.mike[card], leftLimit(col)+10, upLimit(row)+10, 20, BLUE) # draw the text on top of the card.
# --- FUNCTIONS END --- #