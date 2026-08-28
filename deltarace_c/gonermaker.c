#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "vessel.c"

// variables start
// [ YES, HE SCRAWLS HIS NAME IN THE MARGINS OF HIS NOTES. HE NAMES PROGRAMMING VARIABLES AFTER HIM. ]
int malachy[25] = {
  -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1
};
// the textbook that holds onto the final product.
// he won't come in until later.
// document later
int malachy2[25] = {
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0
};

// 0+   -> regular card
// -1   -> free space / unset

// functions start

int randint(int min, int max) {
  return (rand() % ((max - min) + 1)) + min;
}

// C doesnt have an "in" function so manually check if it already exists
bool doesAlreadyExist(
  int card,
  int boardList[25]
) {
  for (int i = 0; i < 25; i++) {
    if (boardList[i] == card) return true;
  }
  return false;
}

// added idx parameter because in using -1 as unset it would never
// get past the actual free space spot + it doesnt require any
// extra computation to just pass the fucking index so im just
// doing that because i cba cba cba cba cba cba FUCK YOU
// FUCK YOU FUCK YOU FUCK YOU I HATE YOU I FUCKING HATE YOU

void cardAdder(
  int boardList[25],
  int idx
) {
  int newCard;
  int star = randint(1, 50);
  int malachy3;

  // strcmp is a byte-by-byte comparison of two strings returning the difference between the first different bytes
  // if the difference is 0 that means all bytes match and the strings are the same
  // you can't do choice == "hard" because strings are pointers and youre comparing the pointers not the contents

  if (star >= 1 && star <= 16) {
    malachy3 = 1;
    newCard = randint(0, oneStarNamesLen-1);
  } else if (star > 16 && star <= 29) {
    malachy3 = 2;
    newCard = randint(0, twoStarNamesLen-1);
  } else if (star > 29 && star <= 39) {
    malachy3 = 3;
    newCard = randint(0, threeStarNamesLen-1);
  } else if (star > 39 && star <= 45) {
    malachy3 = 4;
    newCard = randint(0, fourStarNamesLen-1);
  } else if (star > 45 && star <= 50) {
    malachy3 = 5;
    newCard = randint(0, fiveStarNamesLen-1);
  }

  // also using -1 as a value to mean unset so if its a free space
  // then its going to show up as if its already there 100% of the time
  // however the actual free space only shows up once so we dont need
  // to worry about if its repeated or not

  if (newCard != -1) {
    while (doesAlreadyExist(newCard, boardList)) {
      printf("%d is not used because it is already in the list.", newCard);
      printf("rerolling!");

      if (star >= 1 && star <= 16) {
        newCard = randint(0, oneStarNamesLen-1);
      } else if (star > 16 && star <= 29) {
        newCard = randint(0, twoStarNamesLen-1);
      } else if (star > 29 && star <= 39) {
        newCard = randint(0, threeStarNamesLen-1);
      } else if (star > 39 && star <= 45) {
        newCard = randint(0, fourStarNamesLen-1);
      } else if (star > 45 && star <= 50) {
        newCard = randint(0, fiveStarNamesLen-1);
  }
    }
  }

  printf("setting index %d to card %d", idx, newCard);
  malachy2[idx] = malachy3;
  boardList[idx] = newCard;
}

int* finalChoice() {
  // declare board on the heap so it doesnt get destroyed with the finalChoice stack frame
  int* board = malloc(25 * sizeof(int));
  if (!board) return NULL; // malloc failed LOL!

  for (int i = 0; i < 25; i++) {
    board[i] = -1;
  }

  for (int i = 0; i < 25; i++) {
    if (i == 12) {
      malachy2[i] = 0;
      board[i] = -1;
    } else {
      cardAdder(board, i);
    }
  }

  return board;
}

// malac i mean lucio (not anymore dipshit - awo) is gonna be assigned in main because you cant
// make global variables be non compile time constants but its just gonna be
// the same thing

const char* mikeTheBoard(int card) {
  if (malachy2[card] == 0) {
    return "FREE SPACE";
  } else if (malachy2[card] == 1) {
    return oneStarNames[malachy[card]];
  } else if (malachy2[card] == 2) {
    return twoStarNames[malachy[card]];
  } else if (malachy2[card] == 3) {
    return threeStarNames[malachy[card]];
  } else if (malachy2[card] == 4) {
    return fourStarNames[malachy[card]];
  } else if (malachy2[card] == 5) {
    return fiveStarNames[malachy[card]];
  }
  else {
    return "you done fucked up";
  }
}

const char* okMikeCanYouDescribeItForMe(int card) {
  if (malachy2[card] == 0) {
    return "FREE SPACE";
  } else if (malachy2[card] == 1) {
    return oneStarDesc[malachy[card]];
  } else if (malachy2[card] == 2) {
    return twoStarDesc[malachy[card]];
  } else if (malachy2[card] == 3) {
    return threeStarDesc[malachy[card]];
  } else if (malachy2[card] == 4) {
    return fourStarDesc[malachy[card]];
  } else if (malachy2[card] == 5) {
    return fiveStarDesc[malachy[card]];
  }
  else {
    return "you done fucked up";
  }
}
