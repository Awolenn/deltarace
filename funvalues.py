# --- IMPORTS START --- #
from pyray import *
import random
import gonermaker as goner
import vessel
# --- IMPORTS END --- #

# --- CONSTANTS START --- #
windowWidth = 900
windowHeight = 700
# WINDOW SIZES ^^^ vvv CARD SIZES
cardSize = 100
cardMargin = 5
fullCard = cardSize + cardMargin
# CARD SIZES ^^^ vvv CREDIT SIZES
creditsLeft = 15
creditsUp = 470
creditsWidth = 195
creditsHeight = 50
standardFontSize = 16
# CREDIT SIZES ^^^ vvv DIALOGUE LISTS
gasterMessages = ["", "ARE YOU\n\nTHERE?", "ARE WE\n\nCONNECTED?", "EXCELLENT.", "TRULY\n\nEXCELLENT.", "NOW.", "ARE YOU\n\nEXCITED?", "TO RACE\n\nIN MY\n\nDELTARUNE?", "YOUR SKILLS.\n\nYOUR WONDERFUL\n\nPLANNED OUT\n\nSTRATEGY.", ""]
otherMessages = ["Will now be discarded.", "No one will just play Deltarune\nwithout a twist in this group chat.", "   Your\n\n\nbingo card\n\n\n\n    is", "", "", "", "", "stop spamming you piece of shit"]
forgottenMessages = ["* (Well, there is a man here.)", "* (Well, he seems to be a little lost.)", "* (He seemed like he wanted to speak, but...)", "* (Well, the man smiled when he saw you.)", "* (And there was nothing in his hands.)", "* (But there was this... lingering weight on your\n  shoulder.)", "* (It carried far, far, into the distance.)", "* (...)", '* (You received the "Egg".)', ""]
# DIALOGUE LISTS ^^^ vvv CARD-SPECIFIC LISTS
squaresMarked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
squaresHovered = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
squareColor = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
cardText = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
# --- CONSTANTS END --- #

# --- INITIAL VARIABLES START --- #
currentScreen = 1 # RESET TO ZERO ONCE YOU'RE DONE TESTING!
framesCounter = 0
messageCount = 0
opacity = 0
# DIALOGUE STUFF ^^^ vvv BINGO STUFF
cardPartOneCounter = 0
cardPartTwoCounter = 0
# BINGO STUFF ^^^ vvv CREDITS STUFF
inCredits = False
visitedEggRoom = False # RESET TO FALSE ONCE YOU'RE DONE TESTING!
# --- INITIAL VARIABLES END --- #

# --- FUNCTIONS START --- #
def dialoguePartOne(dialogue):
    """Allows proceeding through dialogue.
    
    dialoguePartTwo should be included inside the "drawing" portion of the code of this is present to ensure full functionality, but I'm not your dad.

    Args:
        dialogue (str[]): The list containing strings to be used for dialogue.
    """
    global framesCounter
    global messageCount
    # vvv DEBUGGING FEATURES, PLEASE REMOVE vvv
    if is_key_down(KEY_SPACE):
        framesCounter += 8
    else: 
        framesCounter += 1
    if is_key_pressed(KEY_ENTER):
        framesCounter = 0
    # ^^^ DEBUGGING FEATURES, PLEASE REMOVE ^^^
    # when "Z" is pressed, continue to the next string in the list.
    # additionally, only allow continuing once the string is finished.
    if is_key_pressed(KEY_Z):
        if framesCounter >= len(dialogue[messageCount]):
            messageCount += 1
            framesCounter = 0

def dialoguePartTwo(font, dialogue, x, y, width, height, size, spacing, color):
    """Form dialogue from a list. Center-aligned.

    dialoguePartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad. Also, I don't actually know if it's raylib.font.
    
    Args:
        font (raylib.font): The font you want the text to be displayed as.
        dialogue (str[]): The list containing strings to be used for dialogue.
        x (int): The X position of the text.
        y (int): The Y position of the text.
        width (int): The width of the text. It makes sense when it gets centered, okay..?
        height (int): The height of the text. It makes sense when it gets centered, okay..?
        size (int): The font size for the text. Gets multiplied by 16.
        spacing (int): The spacing between the letters.
        color (raylib.color): The color you want the text to be.
    """
    textSize = measure_text_ex(font, dialogue[messageCount], standardFontSize*size, spacing)
    textPos = [
        x + lerp(0, width - textSize.x, .5),
        y + lerp(0, height - textSize.y, .5)
    ]
    draw_text_ex(font, text_subtext(dialogue[messageCount], 0, framesCounter), textPos, standardFontSize*size, spacing, color)

def dialoguePartThree(font, dialogue, x, y, size, spacing, color):
    """Form dialogue from a list. Left-aligned.

    dialoguePartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad. Also, I don't actually know if it's raylib.font.
    
    Args:
        font (raylib.font): The font you want the text to be displayed as.
        dialogue (str[]): The list containing strings to be used for dialogue.
        x (int): The X position of the text.
        y (int): The Y position of the text.
        size (int): The font size for the text. Gets multiplied by 16.
        spacing (int): The spacing between the letters.
        color (raylib.color): The color you want the text to be.
    """
    draw_text_ex(font, text_subtext(dialogue[messageCount], 0, framesCounter), [x, y], standardFontSize*size, spacing, color)


def clearText(color):
    """Clear text from the screen.
    
    Args:
        color (raylib.color): The color you want the screen to be.
    """
    draw_rectangle(0, 0, windowWidth, windowHeight, color)

# DIALOGUE ^^^ vvv CARD LIMIT CHECKS

def leftLimit(col):
    """Define the leftmost limit of the card.

    Args:
        col (int): The column the card is in.
    """
    return fullCard*(col-1)+320

def upLimit(row):
    """Define the upper limit of the card.

    Args:
        row (int): The row the card is in.
    
    Returns:
        int: The upper limit of the card.
    """
    return fullCard*(row-1)+5

def allLimits(col, row):
    """Gets all of the limits of a card. Intended to be deconstructed.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
    
    Returns:
        tuple (int, int, int, int): The limits of the card in order of leftmost, upper, rightmost, and lower.
    """
    return (leftLimit(col), upLimit(row), cardSize+leftLimit(col), cardSize+upLimit(row))

# CARD LIMIT CHECKS ^^^ vvv CARD INTERACTION CHECKS

def isClickingCard(leftLimit, upLimit, rightLimit, downLimit):
    """Checks if a card is being clicked.
    
    Args:
        leftLimit (int): The leftmost limit of the card.
        upLimit (int): The upper limit of the card.
        rightLimit (int): The rightmost limit of the card.
        downLimit (int): The lower limit of the card.

    Returns:
        bool: If a card is being clicked or not.
    """
    return get_mouse_x() >= leftLimit and get_mouse_x() <= rightLimit and get_mouse_y() >= upLimit and get_mouse_y() <= downLimit and is_mouse_button_pressed(MOUSE_BUTTON_LEFT)

def isCursorInCard(leftLimit, upLimit, rightLimit, downLimit):
    """Checks if the cursor is in the card.
    
    Args:
        leftLimit (int): The leftmost limit of the card.
        upLimit (int): The upper limit of the card.
        rightLimit (int): The rightmost limit of the card.
        downLimit (int): The lower limit of the card.

    Returns:
        bool: If the cursor is in the card or not.
    """
    return get_mouse_x() >= leftLimit and get_mouse_x() <= rightLimit and get_mouse_y() >= upLimit and get_mouse_y() <= downLimit

# CARD INTERACTION CHECKS ^^^ vvv CARD CREATION

def makeCardPartOne(col, row, card):
    """Makes the cards capable of being marked and showing tooltips when hovered over.

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

    # if cursor is in card, you're hovering over it.
    if isCursorInCard(*allLimits(col, row)):
        squaresHovered[card] = True

    # if cursor isn't in card... you're. uh. not. hovering over it. yeah. yup. ok. yeah.
    elif not isCursorInCard(*allLimits(col, row)):
        squaresHovered[card] = False

def makeCardPartTwo(col, row, card):
    """Draws the cards to the screen, along with the tooltip text.

    makeCardPartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
        card (int): The unique number of the card.
    """
    draw_rectangle(leftLimit(col), upLimit(row), cardSize, cardSize, squareColor[card]) # draw the card itself. the color is a variable so it can be modified when marked.
    draw_text(goner.mikeTheBoard(card), leftLimit(col)+5, upLimit(row)+5, 15, BLUE) # draw the text on top of the card.
    # this took me forever for literally no reason but it supplies tool tips now. so. yay!
    if isCursorInCard(*allLimits(col, row)):
        draw_text(goner.okMikeCanYouDescribeItForMe(card), 0, 530, 15, BLUE)

# CARD CREATION ^^^ vvv BUTTON CREATION

def makeCreditsPartOne():
    global inCredits
    global currentScreen
    global visitedEggRoom
    """Makes the credits button capable of being clicked.

    makeCreditsPartTwo should be included inside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.
    """
    # check if a card is being clicked to begin with, and if so, what card specficially. 
    # the card should be inside of the limits. if it isn't. that's bad.
    if isClickingCard(creditsLeft, creditsUp, creditsLeft+creditsWidth, creditsUp+creditsHeight):
        if not inCredits: # if you're on screen 2, really... or screen 4
            if not visitedEggRoom: # if you haven't gotten the "Egg"
                inbetween = random.randint(50, 100)
                if inbetween == 66:
                    currentScreen = 4
                    visitedEggRoom = True

                else: # if you aren't lucky, you go to credits.
                    currentScreen = 3
                    inCredits = True

            else: # if you've visited the forgotten man, skip the check.
                currentScreen = 3
                inCredits = True

        elif inCredits: # if you're on screen 3m really...
            if not visitedEggRoom: # if you haven't gotten the "Egg"
                inbetween = random.randint(50, 100)
                if inbetween == 66:
                    currentScreen = 4
                    visitedEggRoom = True

                else: # if you aren't lucky, you go to bingo again.
                    currentScreen = 2
                    inCredits = False

            else: # if you've visited the forgotten man, skip the check.
                currentScreen = 2
                inCredits = False

def makeCreditsPartTwo(font):
    """Draws the credits button to the screen.

    makeCardPartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad. Also, I don't actually know if it's raylib.font.
    
    Args:
        font (raylib.font): The font you want the text to be displayed as.
    """
    draw_rectangle(creditsLeft, creditsUp, creditsWidth, creditsHeight, GREEN) # draw the card itself. the color is a variable so it can be modified when marked.
    if not inCredits:
        draw_text_ex(font, "CREDITS", [creditsLeft+25, creditsUp], standardFontSize*3, 0, BLACK)
    elif inCredits:
        draw_text_ex(font, "BACK", [creditsLeft+55, creditsUp], standardFontSize*3, 0, BLACK)
    
# --- FUNCTIONS END --- #