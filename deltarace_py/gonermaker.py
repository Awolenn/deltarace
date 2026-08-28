# --- IMPORTS START --- #
import random
import vessel
# --- IMPORTS END --- #

# --- VARIABLES START --- #
# [ YES, HE SCRAWLS HIS NAME IN THE MARGINS OF HIS NOTES. HE NAMES PROGRAMMING VARIABLES AFTER HIM. ]
# the list that holds onto the final product. he won't come in until later.
malachy = []
# stupid document later
malachy2 = []
# --- VARIABLES END --- #

# --- FUNCTIONS START --- #

def cardAdder(boardList):
    """Assists in the act of picking cards for the bingo board by disallowing duplicates.

    Really only intended to be used in finalChoice(), if it breaks outside of that... I don't care.

    Args:
        star (str): The choice for that area. Needs to be within 50, others won't work as intended.
        boardList ([]): A (preferably) empty list that the cards get added to.
    """
    global malachy2

    star = random.randint(1, 50)
    if star >= 1 and star <= 16:
        malachy3 = 1
        newCard = random.randint(0, len(vessel.oneStarNames)-1)
    elif star > 16 and star <= 29:
        malachy3 = 2
        newCard = random.randint(0, len(vessel.twoStarNames)-1)
    elif star > 29 and star <= 39:
        malachy3 = 3
        newCard = random.randint(0, len(vessel.threeStarNames)-1)
    elif star > 39 and star <= 45:
        malachy3 = 4
        newCard = random.randint(0, len(vessel.fourStarNames)-1)
    elif star > 45 and star <= 50:
        malachy3 = 5
        newCard = random.randint(0, len(vessel.fiveStarNames)-1)
    while newCard in boardList:
        print(newCard, "is not used because it is already in the list.")
        print("rerolling!")
        if star >= 1 and star <= 16:
            newCard = random.randint(0, len(vessel.oneStarNames)-1)
        elif star > 16 and star <= 29:
            newCard = random.randint(0, len(vessel.twoStarNames)-1)
        elif star > 29 and star <= 39:
            newCard = random.randint(0, len(vessel.threeStarNames)-1)
        elif star > 39 and star <= 45:
            newCard = random.randint(0, len(vessel.fourStarNames)-1)
        elif star > 45 and star <= 50:
            newCard = random.randint(0, len(vessel.fiveStarNames)-1)
    print("appending", newCard, "to list.")
    malachy2.append(malachy3)
    boardList.append(newCard)
    print(malachy2)
    print(boardList)

def finalChoice():
    """Creates a bingo board from various cards.

    Returns:
        board ([]): The bingo board, all integers except for "FREE SPACE".
    """
    # line breaks are only for readabililty. they don't affect function.
    # it'd be pretty bad if they did actually.
    board = []

    for card in range(25):
        if card == 12:
            malachy2.append(0)
            board.append("FREE SPACE")
        else:
            cardAdder(board)
    return board

# it's malachy. i told you he'd be back! he's awkwardly placed but whatever parts of my code have to suck or else i'll think i'm the best.
malachy = finalChoice()

def mikeTheBoard(card):
    if malachy2[card] == 0:
        return "FREE SPACE"
    if malachy2[card] == 1:
        return vessel.oneStarNames[malachy[card]]
    if malachy2[card] == 2:
        return vessel.twoStarNames[malachy[card]]
    if malachy2[card] == 3:
        return vessel.threeStarNames[malachy[card]]
    if malachy2[card] == 4:
        return vessel.fourStarNames[malachy[card]]
    if malachy2[card] == 5:
        return vessel.fiveStarNames[malachy[card]]

def okMikeCanYouDescribeItForMe(card):
    if malachy2[card] == 0:
        return "FREE SPACE"
    if malachy2[card] == 1:
        return vessel.oneStarDesc[malachy[card]]
    if malachy2[card] == 2:
        return vessel.twoStarDesc[malachy[card]]
    if malachy2[card] == 3:
        return vessel.threeStarDesc[malachy[card]]
    if malachy2[card] == 4:
        return vessel.fourStarDesc[malachy[card]]
    if malachy2[card] == 5:
        return vessel.fiveStarDesc[malachy[card]]

# --- FUNCTIONS END --- #