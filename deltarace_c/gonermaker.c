#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "vessel.c"

// variables start
//   [ I must perfect every form you've been taught,
// even if I must repeat the same stance a thousand—no,
//  ten thousand—times over… if I am to be a perfectly
//           tailored textbook for you. ]
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

// 0+   -> regular card
// -1   -> free space / unset

// functions start

int randint(int min, int max) {
  return (rand() % ((max - min) + 1)) + min;
}

int easyChoice() {
  return randint(0, easyNamesLen-1);
}

int hardChoice() {
  return randint(0, hardNamesLen-1);
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
  char* choice,
  int boardList[25],
  int idx
) {
  int newCard;

  // strcmp is a byte-by-byte comparison of two strings returning the difference between the first different bytes
  // if the difference is 0 that means all bytes match and the strings are the same
  // you can't do choice == "hard" because strings are pointers and youre comparing the pointers not the contents

  if (strcmp(choice, "hard") == 0) {
    newCard = hardChoice();
  } else if (strcmp(choice, "free") == 0) {
    newCard = -1;
  } else if (strcmp(choice, "easy") == 0) {
    newCard = easyChoice();
  } else {
    printf("you fucked up and entered it wrong (done goofed, even)");
    // its fucked up man
  }

  // also using -1 as a value to mean unset so if its a free space
  // then its going to show up as if its already there 100% of the time
  // however the actual free space only shows up once so we dont need
  // to worry about if its repeated or not

  if (newCard != -1) {
    while (doesAlreadyExist(newCard, boardList)) {
      printf("%d is not used because it is already in the list.", newCard);
      printf("rerolling!");

      if (strcmp(choice, "hard") == 0) {
        newCard = hardChoice();
      } else if (strcmp(choice, "free") == 0) {
        // wont ever happen
        newCard = -1;
      } else if (strcmp(choice, "easy") == 0) {
        newCard = easyChoice();
      } else {
        printf("you fucked up and entered it wrong (done goofed, even)");
        // its fucked up man
      }
    }
  }

  printf("setting index %d to card %d", idx, newCard);
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
    if (i == 4 || i == 6 || i == 10 || i == 18 || i == 22) {
      cardAdder("hard", board, i);
    } else if (i == 12) {
      cardAdder("free", board, i);
    } else {
      cardAdder("easy", board, i);
    }
  }

  return board;
}

// malac i mean lucio (not anymore dipshit - awo) is gonna be assigned in main because you cant
// make global variables be non compile time constants but its just gonna be
// the same thing

const char* mikeTheBoard(int card) {
  if (card == 4 || card == 6 || card == 10 || card == 18 || card == 22) {
    return hardNames[malachy[card]];
  } else if (card == 12) {
    return "FREE SPACE";
  } else {
    return easyNames[malachy[card]];
  }
}

const char* okMikeCanYouDescribeItForMe(int card) {
  if (card == 4 || card == 6 || card == 10 || card == 18 || card == 22) {
    return hardDesc[malachy[card]];
  } else if (card == 12) {
    return "FREE SPACE";
  } else {
    return easyDesc[malachy[card]];
  }
}
