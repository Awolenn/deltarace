# --- IMPORTS START --- #
import random
import vessel
# --- IMPORTS END --- #

# --- VARIABLES START --- #
# [ YES, HE SCRAWLS HIS NAME IN THE MARGINS OF HIS NOTES. HE NAMES PROGRAMMING VARIABLES AFTER HIM. ]
# the list that holds onto the final product. he won't come in until later.
malachy = []
# --- VARIABLES END --- #

# --- FUNCTIONS START --- #
def easyChoice():
    """Selects a random integer that can be carded in the easyNames list.

    Returns:
        int: A random integer that can be carded in the easyNames list.
    """
    return random.randint(0, len(vessel.easyNames)-1)

def hardChoice():
    """Selects a random integer that can be carded in the hardNames list.

    Returns:
        int: A random integer that can be carded in the hardNames list.
    """
    return random.randint(0, len(vessel.hardNames)-1)

def cardAdder(choice, boardList):
    """Assists in the act of picking cards for the bingo board by disallowing duplicates.

    Really only intended to be used in finalChoice(), if it breaks outside of that... I don't care.

    Args:
        choice (str): The choice for that area. Needs to be "hard", "free", or "easy", others won't work as intended.
        boardList ([]): A (preferably) empty list that the cards get added to.
    """
    if choice == "hard":
        newCard = hardChoice()
    elif choice == "free":
        newCard = "FREE SPACE"
    elif choice == "easy":
        newCard = easyChoice()
    else:
        print("you fucked this up and entered it wrong")
    while newCard in boardList:
        print(newCard, "is not used because it is already in the list.")
        print("rerolling!")
        if choice == "hard":
            newCard = hardChoice()
        elif choice == "free":
            newCard = "FREE SPACE"
        elif choice == "easy":
            newCard = easyChoice()
        else:
            print("you fucked this up and entered it wrong")
    print("appending", newCard, "to list.")
    boardList.append(newCard)
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
        if card == 4 or card == 6 or card == 10 or card == 18 or card == 22:
            cardAdder("hard", board)
        elif card == 12:
            cardAdder("free", board)
        else:
            cardAdder("easy", board)
    return board

# it's malachy. i told you he'd be back! he's awkwardly placed but whatever parts of my code have to suck or else i'll think i'm the best.
malachy = finalChoice()

def mikeTheBoard(card):
    if card == 4 or card == 6 or card == 10 or card == 18 or card == 22:
        return vessel.hardNames[malachy[card]]
    if card == 12:
        return "FREE SPACE"
    else:
        return vessel.easyNames[malachy[card]]

def okMikeCanYouDescribeItForMe(card):
    if card == 4 or card == 6 or card == 10 or card == 18 or card == 22:
        return vessel.hardDesc[malachy[card]]
    if card == 12:
        return "FREE SPACE"
    else:
        return vessel.easyDesc[malachy[card]]
# --- FUNCTIONS END --- #
print(mikeTheBoard(1))
print(okMikeCanYouDescribeItForMe(1))
print(mikeTheBoard(4))
print(okMikeCanYouDescribeItForMe(4))
print(malachy)