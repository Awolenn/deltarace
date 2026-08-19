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
cardSize = 114
cardMargin = 5
fullCard = cardSize + cardMargin
# CARD SIZES ^^^ vvv CREDIT SIZES
creditsLeft = 700
creditsUp = 640
creditsWidth = 195
creditsHeight = 50
standardFontSize = 16
# CREDIT SIZES ^^^ vvv EGG ROOM
eggRoomFrame = []
# EGG ROOM ^^^ vvv DIALOGUE LISTS
gasterMessages = ["ARE YOU\n\nTHERE?", "ARE WE\n\nCONNECTED?", "EXCELLENT.", "TRULY\n\nEXCELLENT.", "NOW.", "ARE YOU\n\nEXCITED?", "TO RACE\n\nIN MY\n\nDELTARUNE?", "YOUR SKILLS.\n\nYOUR WONDERFUL\n\nPLANNED OUT\n\nSTRATEGY.", ""]
otherMessages = ["Will now be\ndiscarded.", "No one will just\nplay Deltarune\nwithout a twist\nin this group chat.", "      Your\n\n\n   bingo card\n\n\n\n       is", "", "", "", "", "stop spamming you piece of shit"]
forgottenMessages = ["* (Well, there is a man here.)", "* (Well, he seems to be a little lost.)", "* (He seemed like he wanted to speak,\n  but...)", "* (Well, the man smiled when he saw\n  you.)", "* (And there was nothing in his hands.)", "* (But there was this... lingering\n  weight on your shoulder.)", "* (It carried far, far, into the\n  distance.)", "* (...)", '* (You received the "Egg".)', ""]
# DIALOGUE LISTS ^^^ vvv CARD-SPECIFIC LISTS
squaresMarked = [False, False, False, False, False, #0-4
                 False, False, False, False, False, #5-9
                 False, False, False, False, False, #10-14
                 False, False, False, False, False, #15-19
                 False, False, False, False, False] #20-24
squaresHovered = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
squareColor = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
cardText = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
# --- CONSTANTS END --- #

# --- INITIAL VARIABLES START --- #
currentScreen = 0 # RESET TO ZERO ONCE YOU'RE DONE TESTING!
framesCounter = 0
messageCount = 0
opacity = 0
depthsOpacity = 0
getBrighter = True
depthsGetBrighter = False
# DIALOGUE STUFF ^^^ vvv BINGO STUFF
cardPartOneCounter = 0
cardPartTwoCounter = 0
win = False
# BINGO STUFF ^^^ vvv CREDITS STUFF
inCredits = False
visitedEggRoom = False # RESET TO FALSE ONCE YOU'RE DONE TESTING!
# CREDITS STUFF ^^^ vvv EGG ROOM STUFF
framesCounterForAnimation = 0
currentAnimationFrame = 0
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
        x + lerp(0, width/2 - textSize.x/2, .5),
        y + lerp(0, height/2 - textSize.y/2, .5)
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
    return fullCard*(col-1)+300

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

def drawWrappedCardText(card, font, col, row):
    """Draws wrapped text. This one uses the dimensions and positions for cards.

    Args:
        card (int): The unique number of the card.
        font (raylib.font): The font you want the card text to be displayed as.
        col (int): The column of the card.
        row (int): The row of the card.
    """
    spaceRemaining = 14
    newTextLineCount = 0
    newText = []

    for word in goner.mikeTheBoard(card).split(" "):
        if len(word) > spaceRemaining:
            newText.append("\n" + word)
            newTextLineCount += 1
            spaceRemaining = 14 - len(word)
        else:
            newText.append(word)
            spaceRemaining = spaceRemaining - (len(word))
    brandSpankingNewText = " ".join(newText)
    draw_text_ex(font, brandSpankingNewText, [leftLimit(col)+2, upLimit(row)], standardFontSize*1, 0, WHITE)

def drawWrappedTooltipText(card, font):
    """Draws wrapped text. This one uses the dimensions and positions for tooltips.

    Args:
        card (int): The unique number of the card.
        font (raylib.font): The font you want the card text to be displayed as.
    """
    spaceRemaining = 26
    newTextLineCount = 0
    newText = []

    for word in goner.okMikeCanYouDescribeItForMe(card).split(" "):
        if len(word) > spaceRemaining:
            newText.append("\n" + word)
            newTextLineCount += 1
            spaceRemaining = 26 - len(word)
        else:
            newText.append(word)
            spaceRemaining = spaceRemaining - (len(word))
    brandSpankingNewText = " ".join(newText)
    draw_text_ex(font, brandSpankingNewText, [5, 5], standardFontSize*1, 0, WHITE)

def makeCardPartOne(col, row, sound, card):
    """Makes the cards capable of being marked and showing tooltips when hovered over.

    makeCardPartTwo should be included inside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
        sound (raylib.sound): The sound used when marking or unmarking a card.
        card (int): The unique number of the card.
    """
    # check if a card is being clicked to begin with, and if so, what card specficially. 
    # the card should be inside of the limits. if it isn't. that's bad.
    if isClickingCard(*allLimits(col, row)):
        set_sound_volume(sound, .4)
        play_sound(sound)
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

def makeCardPartTwo(col, row, card, font, font2):
    """Draws the cards to the screen, along with the tooltip text.

    makeCardPartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad. Also, I don't actually know if it's raylib.font.

    Args:
        col (int): The column of the card.
        row (int): The row of the card.
        card (int): The unique number of the card.
        font (raylib.font): The font you want the card text to be displayed as.
        font2 (raylib.font): The font you want the tooltip text to be displayed as.
    """
    draw_rectangle(leftLimit(col), upLimit(row), cardSize, cardSize, squareColor[card]) # draw the card itself. the color is a variable so it can be modified when marked.
    drawWrappedCardText(card, font, col, row) # draw the text on top of the card.
    # this took me forever for literally no reason but it supplies tool tips now. so. yay!
    if isCursorInCard(*allLimits(col, row)):
        drawWrappedTooltipText(card, font2)

def possibleBingoWinCheck(sound):
    """Checks all possible bingo wins and returns if there is any win.

    Args:
        sound (raylib.sound): The sound you want to be played after winning.

    Returns:
        bool: If there is a win on the board or not.
    """
    global win

    # it's a real undertale fangame it even has the dogshit switch case statement that can certainly be done better
    # marking all of row 1
    if not win and squaresMarked[0] and squaresMarked[1] and squaresMarked[2] and squaresMarked[3] and squaresMarked[4]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of row 2
    elif not win and squaresMarked[5] and squaresMarked[6] and squaresMarked[7] and squaresMarked[8] and squaresMarked[9]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of row 3
    elif not win and squaresMarked[10] and squaresMarked[11] and squaresMarked[12] and squaresMarked[13] and squaresMarked[14]:
        print("oh yeah you win")
        play_sound(sound)
        win = True
    
    # marking all of row 4
    elif not win and squaresMarked[15] and squaresMarked[16] and squaresMarked[17] and squaresMarked[18] and squaresMarked[19]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of row 5
    elif not win and squaresMarked[20] and squaresMarked[21] and squaresMarked[22] and squaresMarked[23] and squaresMarked[24]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of column 1
    elif not win and squaresMarked[0] and squaresMarked[5] and squaresMarked[10] and squaresMarked[15] and squaresMarked[20]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of column 2
    elif not win and squaresMarked[1] and squaresMarked[6] and squaresMarked[11] and squaresMarked[16] and squaresMarked[21]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of column 3
    elif not win and squaresMarked[2] and squaresMarked[7] and squaresMarked[12] and squaresMarked[17] and squaresMarked[22]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of column 4
    elif not win and squaresMarked[3] and squaresMarked[8] and squaresMarked[13] and squaresMarked[18] and squaresMarked[23]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking all of column 5
    elif not win and squaresMarked[4] and squaresMarked[9] and squaresMarked[14] and squaresMarked[19] and squaresMarked[24]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking the diagonal that starts from the top left
    elif not win and squaresMarked[0] and squaresMarked[6] and squaresMarked[12] and squaresMarked[18] and squaresMarked[24]:
        print("oh yeah you win")
        play_sound(sound)
        win = True

    # marking the diagonal that starts from the top right
    elif not win and squaresMarked[4] and squaresMarked[8] and squaresMarked[12] and squaresMarked[16] and squaresMarked[20]:
        print("oh yeah you win")
        play_sound(sound)
        win = True
    
    # if you uncheck something i guess, uses the hard locations to check since every diagonal has to include one
    elif win and not squaresMarked[4] and not squaresMarked[6] and not squaresMarked[10] and not squaresMarked[18] and not squaresMarked[22]:
        win = False

# CARD CREATION ^^^ vvv BUTTON CREATION

def makeCreditsPartOne(sound, eggNoise):
    global inCredits
    global currentScreen
    global visitedEggRoom
    """Makes the credits button capable of being clicked.

    makeCreditsPartTwo should be included inside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad.
    
    Args:
        sound (raylib.sound): The sound the CREDITS and BACK button makes when clicked on.
        eggNoise (raylib.sound): The sound the "Egg" makes when clicked on.
    """
    # check if a card is being clicked to begin with, and if so, what card specficially. 
    # the card should be inside of the limits. if it isn't. that's bad.
    if isClickingCard(creditsLeft, creditsUp, creditsLeft+creditsWidth, creditsUp+creditsHeight):
        if isClickingCard(865, 660, 865+25, 660+30):
                play_sound(eggNoise)
        else:
            set_sound_volume(sound, .4)
            play_sound(sound)
            if not inCredits: # if you're on screen 2, really... or screen 4
                if not visitedEggRoom: # if you haven't gotten the "Egg"
                    inbetween = random.randint(50, 100)
                    if inbetween == 66:
                        currentScreen = 66
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
                        currentScreen = 66
                        visitedEggRoom = True
                        inCredits = False

                    else: # if you aren't lucky, you go to bingo again.
                        currentScreen = 2
                        inCredits = False

                else: # if you've visited the forgotten man, skip the check.
                    currentScreen = 2
                    inCredits = False

def makeCreditsPartTwo(font, image):
    """Draws the credits button to the screen.

    makeCardPartOne should be included outside the "drawing" portion of the code if this is present to ensure full functionality, but I'm not your dad. Also, I don't actually know if it's raylib.font.
    
    Args:
        font (raylib.font): The font you want the text to be displayed as.
        image (raylib.texture): The image you want to use for the "Egg".
    """
    draw_rectangle(creditsLeft, creditsUp, creditsWidth, creditsHeight, GREEN) # draw the card itself. the color is a variable so it can be modified when marked.
    if not inCredits:
        draw_text_ex(font, "CREDITS", [creditsLeft+25, creditsUp], standardFontSize*3, 0, BLACK)
    elif inCredits:
        draw_text_ex(font, "BACK", [creditsLeft+55, creditsUp], standardFontSize*3, 0, BLACK)
    if visitedEggRoom:
            draw_texture(image, 865, 660, WHITE)

# BUTTON CREATION ^^^ vvv EGG ROOM

def loadEggRooms():
    global eggRoomFrame
    for i in range(21):
        k = "DONOTENTERPLEASE/eggRoomFrames/eggRoom"+str(i+1)+".gif"
        image = load_image(k)
        eggRoomFrame.append(load_texture_from_image(image))

def animateEggRoom():
    global currentAnimationFrame
    global framesCounterForAnimation
    framesCounterForAnimation += 1
    if framesCounterForAnimation%3 == 0:
        currentAnimationFrame += 1
        if currentAnimationFrame >= 20:
            currentAnimationFrame = 0
    draw_texture_ex(eggRoomFrame[currentAnimationFrame], [260, 100], 0, 3, WHITE)

# --- FUNCTIONS END --- #