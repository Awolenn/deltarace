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

def finalChoice():
    """Creates a bingo board from various cards.

    Returns:
        board ([]): The bingo board, all integers except for "FREE SPACE".
    """
    # line breaks are only for readabililty. they don't affect function.
    # it'd be pretty bad if they did actually.
    board = [easyChoice(), easyChoice(), easyChoice(), easyChoice(), hardChoice(), 
    easyChoice(), hardChoice(), easyChoice(), easyChoice(), easyChoice(),
    hardChoice(), easyChoice(), "FREE SPACE", easyChoice(), easyChoice(),
    easyChoice(), easyChoice(), easyChoice(), hardChoice(), easyChoice(),
    easyChoice(), easyChoice(), hardChoice(), easyChoice(), easyChoice()]

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