#include <raylib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "gonermaker.c"

// window sizes
const int windowWidth = 900;
const int windowHeight = 700;

// card sizes
const int cardSize = 114;
const int cardMargin = 5;
const int fullCard = cardSize + cardMargin;

// card colors
const Color blueGray = { 218, 222, 230, 255 };
const Color darkBlue = { 11, 14, 20, 255 };
const Color deeperBlueGray = { 27, 31, 36, 255 };

// credit sizes
const int creditsLeft = 700;
const int creditsUp = 640;
const int creditsWidth = 195;
const int creditsHeight = 50;

// font
const int standardFontSize = 16;

// egg room
Texture2D eggRoomFrame[21];

// dialogue lists
const char* gasterMessages[] = {
    "ARE YOU\n\nTHERE?",
    "ARE WE\n\nCONNECTED?",
    "EXCELLENT.",
    "TRULY\n\nEXCELLENT.",
    "NOW.",
    "ARE YOU\n\nEXCITED?",
    "TO RACE\n\nIN MY\n\nDELTARUNE?",
    "YOUR SKILLS.\n\nYOUR WONDERFUL\n\nPLANNED OUT\n\nSTRATEGY.",
    ""
};
const int gasterMessagesLen = sizeof gasterMessages / sizeof *gasterMessages;

const char* otherMessages[] = {
    "Will now be\ndiscarded.",
    "No one will just\nplay Deltarune\nwithout a twist\nin this group chat.",
    "      Your\n\n\n   bingo card\n\n\n\n       is",
    "",
    "",
    "",
    "",
    "stop spamming you piece of shit"
};
const int otherMessagesLen = sizeof otherMessages / sizeof *otherMessages;

const char* forgottenMessages[] = {
    "* (Well, there is a man here.)",
    "* (Well, he seems to be a little lost.)",
    "* (He seemed like he wanted to speak,\n  but...)",
    "* (Well, the man smiled when he saw\n  you.)",
    "* (And there was nothing in his hands.)",
    "* (But there was this... lingering\n  weight on your shoulder.)",
    "* (It carried far, far, into the\n  distance.)",
    "* (...)",
    "* (You received the \"Egg\".)",
    ""
};
const int forgottenMessagesLen = sizeof forgottenMessages / sizeof *forgottenMessages;

bool squaresMarked[] = {
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false
};

bool squaresHovered[] = {
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false,
  false, false, false, false, false
};

Color squareColor[] = {
  blueGray, blueGray, blueGray, blueGray, blueGray,
  blueGray, blueGray, blueGray, blueGray, blueGray,
  blueGray, blueGray, blueGray, blueGray, blueGray,
  blueGray, blueGray, blueGray, blueGray, blueGray,
  blueGray, blueGray, blueGray, blueGray, blueGray
};

const char* cardText[] = {
  "0", "1", "2", "3", "4",
  "5","6", "7", "8", "9",
  "10", "11", "12", "13", "14",
  "15", "16", "17", "18", "19",
  "20", "21", "22", "23", "24"
};

// initial variables start
// dialogue stuff
int currentScreen = 0;
int framesCounter = 0;
int messageCount = 0;
float opacity = 0.0f;
float depthsOpacity = 0.0f;
bool getBrighter = true;
bool depthsGetBrighter = false;

// bingo stuff
int cardPartOneCounter = 0;
int cardPartTwoCounter = 0;
bool win = false;

// credits stuff
bool inCredits = false;
bool visitedEggRoom = false;

// egg room stuff
int framesCounterForAnimation = 0;
int currentAnimationFrame = 0;

// #define DEBUG
// ^ comment/uncomment to disable/enable debug shitsies respectively

void dialoguePartOne(
  char* dialogue[]
) {
    framesCounter++;

  if (IsKeyPressed(KEY_Z)) {
    if (framesCounter >= strlen(dialogue[messageCount])) {
      messageCount++;
      framesCounter = 0;
}
  }
}

void dialoguePartTwo(
  Font font,
  char* dialogue[],
  int x,
  int y,
int width,
  int height,
  int size,
  int spacing,
  Color color
) {
  Vector2 textSize = MeasureTextEx(font, dialogue[messageCount], standardFontSize*size, spacing);
  Vector2 textPos = {
    (float)x + ( (float)width/2 - textSize.x/2 ) / 2,
    (float)y + ( (float)height/2 - textSize.y/2 ) / 2
  };
  DrawTextEx(font, TextSubtext(dialogue[messageCount], 0, framesCounter), textPos, standardFontSize*size, spacing, color);
}

void dialoguePartThree(
  Font font,
  char* dialogue[],
  int x,
  int y,
  float size,
  int spacing,
  Color color
) {
  Vector2 textPos = {
    (float)x,
    (float)y
  };
  DrawTextEx(font, TextSubtext(dialogue[messageCount], 0, framesCounter), textPos, standardFontSize*size, spacing, color);
}

void clearText(Color color) {
  DrawRectangle(0, 0, windowWidth, windowHeight, color);
}

int leftLimit(int col) {
  return fullCard*(col-1)+300;
}

int upLimit(int row) {
  return fullCard*(row-1)+5;
}

typedef struct {
  int left;
  int top;
  int right;
  int bottom;
} CardLimits;
// ^ make a custom structure for card limits
// cause C doesnt have tuples

CardLimits allLimits(int col, int row) {
  CardLimits limits = {
    leftLimit(col),
    upLimit(row),
    cardSize+leftLimit(col),
    cardSize+upLimit(row)
  };

  return limits;
}

bool isClickingCard(CardLimits limits) {
  return GetMouseX() >= limits.left &&
  GetMouseX() <= limits.right &&
  GetMouseY() >= limits.top &&
  GetMouseY() <= limits.bottom &&
  IsMouseButtonPressed(MOUSE_LEFT_BUTTON);
}

bool isCursorInCard(CardLimits limits) {
  return GetMouseX() >= limits.left &&
  GetMouseX() <= limits.right &&
  GetMouseY() >= limits.top &&
  GetMouseY() <= limits.bottom;
}

// drawWrappedCardText and drawWrappedTooltipText make me
// want to vomit
//
// i shouldve never offered my help

void drawWrappedCardText(
  int card,
  Font font,
  int col,
  int row
) {
  int spaceRemaining = 14;
  int newTextLineCount = 0;

  const char* input = mikeTheBoard(card);

  int inputlen = strlen(input);

  // worst case scenario is every word gets \n so double the buffer
  int bufferlen = inputlen * 2 + 16;

  char* brandSpankingNewText = malloc(bufferlen);
  if (!brandSpankingNewText) return; // malloc shat itself
  // strings in C are null (\0) terminated so make sure that
  // even if its an empty string its still null terminated
  brandSpankingNewText[0] = '\0';

  // in C you cant like split by a character you gotta use this thing
  // called strtok which modifies the original string so
  // work on a copy

  // strdup -> string duplicate
  char* inputCopy = strdup(input);
  if (!inputCopy) {
    free(brandSpankingNewText); // free the buffer memory
    return; // return because strdup shat itself
  }

  bool first = true;
  // strtok returns a pointer to the first matching thing up until the delimeter
  // moving the rest of the string passed the first one
  // i.e:
  //          HELLO  WORLD\0
  //          ^
  //          str
  //
  //          word = strtok(str, " ");
  //
  //          HELLO\0WORLD\0
  //          ^      ^
  //          word   str
  char* word = strtok(inputCopy, " ");
  while (word != NULL) {
    int wordlen = (int)strlen(word);

    // if it isnt the first word, prepend with a space
    if (!first) {
      strcat(brandSpankingNewText, " ");
    }

    // strcat just adds the 2nd string to the first, its just
    // append
    if (wordlen > spaceRemaining) {
      strcat(brandSpankingNewText, "\n");
strcat(brandSpankingNewText, word);
      newTextLineCount++;
      spaceRemaining = 14 - wordlen;
    } else {
      strcat(brandSpankingNewText, word);
      spaceRemaining = spaceRemaining - wordlen;
    }

    first = false;
    word = strtok(NULL, " ");
  }

  // free the copy
  free(inputCopy);

  // pick up the damn pencil
  Vector2 pos = {
    (float)(leftLimit(col) + 2),
    (float)upLimit(row)
  };
  DrawTextEx(font, brandSpankingNewText, pos, standardFontSize, 0, darkBlue);
  // free the buffer
  free(brandSpankingNewText);
}

// this one is gonna be devoid of comments because i already
// explained it all

void drawWrappedTooltipText(
  int card,
  Font font
) {
  int spaceRemaining = 26;
  int newTextLineCount = 0;

  const char* input = okMikeCanYouDescribeItForMe(card);

  int inputlen = strlen(input);

  int bufferlen = inputlen * 2 + 16;

  char* brandSpankingNewText = malloc(bufferlen);
  if (!brandSpankingNewText) return; // malloc shat itself
  brandSpankingNewText[0] = '\0';

  char* inputCopy = strdup(input);
  if (!inputCopy) {
    free(brandSpankingNewText); // free the buffer memory
    return; // return because strdup shat itself
  }

  bool first = true;
  char* word = strtok(inputCopy, " ");
  while (word != NULL) {
    int wordlen = (int)strlen(word);

    if (!first) {
      strcat(brandSpankingNewText, " ");
    }

    if (wordlen > spaceRemaining) {
      strcat(brandSpankingNewText, "\n");
      strcat(brandSpankingNewText, word);
      newTextLineCount++;
      spaceRemaining = 26 - wordlen;
    } else {
      strcat(brandSpankingNewText, word);
      spaceRemaining = spaceRemaining - wordlen;
    }

    first = false;
    word = strtok(NULL, " ");
  }

  free(inputCopy);

  Vector2 pos = {
    5.0f,
    5.0f
  };
  DrawTextEx(font, brandSpankingNewText, pos, standardFontSize, 0, blueGray);
  free(brandSpankingNewText);
}

void makeCardPartOne(
  int col,
  int row,
  Sound sound,
  int card
) {
if (isClickingCard(allLimits(col, row))) {
    SetSoundVolume(sound, 0.4f);
    PlaySound(sound);

    if (!squaresMarked[card]) {
      squareColor[card] = RED;
      squaresMarked[card] = true;
    } else if (squaresMarked[card]) {
      squareColor[card] = blueGray;
      squaresMarked[card] = false;
    }
  }

  if (isCursorInCard(allLimits(col, row))) {
    squaresHovered[card] = true;
  }

  if (isCursorInCard(allLimits(col, row))) {
    squaresHovered[card] = false;
  }
}

void makeCardPartTwo(
  int col,
  int row,
  int card,
  Font font,
  Font font2
) {
  DrawRectangle(leftLimit(col), upLimit(row), cardSize, cardSize, squareColor[card]);
  drawWrappedCardText(card, font, col, row);
  if (isCursorInCard(allLimits(col, row))) {
    drawWrappedTooltipText(card, font2);
}
}

bool possibleBingoWinCheck(Sound sound) {
  // i fucking hate you sam

  // row 1
  if (!win && squaresMarked[0] && squaresMarked[1] && squaresMarked[2] && squaresMarked[3] && squaresMarked[4]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // row 2
  else if (!win && squaresMarked[5] && squaresMarked[6] && squaresMarked[7] && squaresMarked[8] && squaresMarked[9]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // row 3
  else if (!win && squaresMarked[10] && squaresMarked[11] && squaresMarked[12] && squaresMarked[13] && squaresMarked[14]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // row 4
  else if (!win && squaresMarked[15] && squaresMarked[16] && squaresMarked[17] && squaresMarked[18] && squaresMarked[19]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

// row 5
  else if (!win && squaresMarked[20] && squaresMarked[21] && squaresMarked[22] && squaresMarked[23] && squaresMarked[24]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // col 1
  else if (!win && squaresMarked[0] && squaresMarked[5] && squaresMarked[10] && squaresMarked[15] && squaresMarked[20]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // col 2
  else if (!win && squaresMarked[1] && squaresMarked[6] && squaresMarked[11] && squaresMarked[16] && squaresMarked[21]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // col 3
  else if (!win && squaresMarked[2] && squaresMarked[7] && squaresMarked[12] && squaresMarked[17] && squaresMarked[22]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // col 4
  else if (!win && squaresMarked[3] && squaresMarked[8] && squaresMarked[13] && squaresMarked[18] && squaresMarked[23]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // col 5
  else if (!win && squaresMarked[4] && squaresMarked[9] && squaresMarked[14] && squaresMarked[19] && squaresMarked[24]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // top left diag
  else if (!win && squaresMarked[0] && squaresMarked[6] && squaresMarked[12] && squaresMarked[18] && squaresMarked[24]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // top right diag
  else if (!win && squaresMarked[4] && squaresMarked[8] && squaresMarked[12] && squaresMarked[16] && squaresMarked[20]) {
    printf("oh yeah you win");
    PlaySound(sound);
    win = true;
  }

  // I HTAE YOU I HATE YOU I HATE YOU I HAT EYOU I H i keyboard spammed so much that my terminal opened a new tab
  else if (win && !squaresMarked[4] && !squaresMarked[6] && !squaresMarked[10] && !squaresMarked[18] && !squaresMarked[22]) {
    win = false;
  }

  return win;
}

void makeCreditsPartOne(
  Sound sound,
  Sound eggNoise
) {
  CardLimits creditsLimits = {
    creditsLeft,
    creditsUp,
    creditsLeft+creditsWidth,
    creditsUp+creditsHeight
  };

  CardLimits eggLimits = {
    15,
    660,
    15+24,
    660+28
  };

  if (isClickingCard(eggLimits)) {
    PlaySound(eggNoise);
  }
  if (isClickingCard(creditsLimits)) {
    SetSoundVolume(sound, 0.4f);
    PlaySound(sound);
    if (!inCredits) {
      if (!visitedEggRoom) {
        int inbetween = randint(50, 100);
        if (inbetween == 66) {
          currentScreen = 66;
          visitedEggRoom = true;
        } else {
          currentScreen = 3;
          inCredits = true;
        }
      } else {
        currentScreen = 3;
        inCredits = true;
      }
    } else {
      if (!visitedEggRoom) {
        int inbetween = randint(50, 100);
        if (inbetween == 66) {
          currentScreen = 66;
            visitedEggRoom = true;
          inCredits = false;
        } else {
          currentScreen = 2;
          inCredits = false;
        }
      } else {
        currentScreen = 2;
        inCredits = false;
      }
    }
  }
}

void makeCreditsPartTwo(
  Font font,
  Texture2D image
) {
  DrawRectangle(creditsLeft-2, creditsUp-2, creditsWidth+4, creditsHeight+4, deeperBlueGray);
  DrawRectangle(creditsLeft, creditsUp, creditsWidth, creditsHeight, blueGray);
  if (!inCredits) {
    Vector2 textLoc = {
      creditsLeft + 25,
      creditsUp
    };
    DrawTextEx(font, "CREDITS", textLoc, standardFontSize*3, 0, BLACK);
  } else {
    Vector2 textLoc = {
      creditsLeft + 55,
      creditsUp
    };
    DrawTextEx(font, "BACK", textLoc, standardFontSize*3, 0, BLACK);
  }
  if (visitedEggRoom) {
    DrawTexture(image, 15, 660, WHITE);
  }
}

void loadEggRooms() {
  for (int i = 0; i < 21; i++) {
    char k[256];
    // sprintf writes a formatted string to a buffer (k)
    sprintf(k, "DONOTENTERPLEASE/eggRoomFrames/eggRoom%d.gif", i+1);
    Image image = LoadImage(k);
    eggRoomFrame[i] = LoadTextureFromImage(image);
  }
}

void animateEggRoom() {
  framesCounterForAnimation++;
  if (framesCounterForAnimation % 3 == 0) {
    currentAnimationFrame++;
    if (currentAnimationFrame >= 20) {
      currentAnimationFrame = 0;
    }
  }
  Vector2 eggPos = {
    260,
    100
  };
  DrawTextureEx(eggRoomFrame[currentAnimationFrame], eggPos, 0, 3, WHITE);
}
