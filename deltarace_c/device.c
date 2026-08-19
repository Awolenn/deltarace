// raylib (not pyray like some pussy ass bomboclat)
#include "raylib.h"
#include "time.h"

// files
#include "fun.c"

#define ASSET "DONOTENTERPLEASE/"

int main() {
  srand(time(NULL));
  InitWindow(windowWidth, windowHeight, "CONNECTION ESTABLISHED .");
  InitAudioDevice();
  SetTraceLogLevel(4); // preventing log spam

  // copy board to lucio since lucio isnt assignable
  int* board = finalChoice();
  if (board) {
    memcpy(lucio, board, 25 * sizeof(int));
    free(board);
  }

  // image loading
  loadEggRooms();
  Image temp = {
      0}; // {0} is basically a null object in C (serves as an object with 0
          // values which is what all objects are initialized to)
  // ^ also because i hate having repetition with one being off
  temp = LoadImage(ASSET "depthsPartOne.png");
  const Texture2D depthsA = LoadTextureFromImage(temp);
  temp = LoadImage(ASSET "depthsPartTwo.png");
  const Texture2D depthsB = LoadTextureFromImage(temp);
  temp = LoadImage(ASSET "credits.png");
  const Texture2D creditsImage = LoadTextureFromImage(temp);
  temp = LoadImage(ASSET "Egg_item.png");
  const Texture2D eggImage = LoadTextureFromImage(temp);
  // ^ all of them are const because they never change
  // non-const variables take up more space and are harder to compile
  //
  // also ASSET is a macro it expands to the thing above where it says #define
  // ASSET its just a shorthand so i dont have to type DONOTENTERPLEASE/ every
  // time two strings together like "a" "b" in C results in concatenation ( "ab"
  // ) so it just resolves to the path anyway (i will probably pre-expand the
  // macros so)

  // sound loading
  const Sound man = LoadSound(ASSET "man.ogg");
  const Sound anotherhim = LoadSound(ASSET "AUDIO_ANOTHERHIM.ogg");
  const Sound w = LoadSound(ASSET "w.ogg");
  const Sound eggSound = LoadSound(ASSET "snd_egg.wav");
  const Sound clickSound = LoadSound(ASSET "snd_noise.wav");
  const Sound winSound = LoadSound(ASSET "snd_won.wav");

  // font loading
  const Font monoFont = LoadFont(ASSET "DTM-Mono.otf");
  const Font sansFont = LoadFont(ASSET "DTM-Sans.otf");
  const Font wingdingding = LoadFont(ASSET "Wingdings-Regular.ttf");

  while (!WindowShouldClose()) {
    // main loop start
    // screen 0 ; gaster dialogue
    if (currentScreen == 0) {
      SetTargetFPS(15);
      if (IsSoundValid(anotherhim) && !IsSoundPlaying(anotherhim)) {
        PlaySound(anotherhim);
      }
      dialoguePartOne((char**)gasterMessages);

      if (opacity >= 1.0f) {
        getBrighter = false;
      } else if (opacity <= 0.0f) {
        getBrighter = true;
      }

      if (getBrighter) {
        opacity += 0.05f;
      } else if (!getBrighter) {
        opacity -= 0.05f;
      }

      if (depthsOpacity >= 1.0f) {
        depthsGetBrighter = false;
      } else if (depthsOpacity <= 0.0f) {
        depthsGetBrighter = true;
      }

      if (depthsGetBrighter) {
        depthsOpacity += 0.01f;
      } else if (!depthsGetBrighter) {
        depthsOpacity -= 0.01f;
      }

      if (messageCount == gasterMessagesLen-1) {
        messageCount = 0;
        currentScreen = 1;
        opacity = 0.0f;
      }
    }

    // screen 1 ; other dialogue
    else if (currentScreen == 1) {
      SetWindowTitle(" ");
      SetTargetFPS(10);
      StopSound(anotherhim);
      dialoguePartOne((char**)otherMessages);

      if (messageCount >= 2) {
        if (IsSoundValid(w) && !IsSoundPlaying(w)) {
          PlaySound(w);
        }
        opacity += 0.02f;
      }

      if (opacity >= 1.0f) {
        messageCount = 0;
        opacity = 0.0f;
        currentScreen = 2;
      }
    }

    else if (currentScreen == 2) {
      SetWindowTitle("SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!");
      StopSound(w);
      StopSound(man);
      SetTargetFPS(60);
      // T HIS DOES LITERALLY NOTIHING
      for (int cardCounter = 0; cardCounter < 25; cardCounter++) {
        for (int col = 1; col < 6; col++) {
          for (int row = 1; row < 6; row++) {
            makeCardPartOne(row, col, clickSound, ((row-1)+(col-1)*5));
          }
        }
      }
      makeCreditsPartOne(clickSound, eggSound);
      possibleBingoWinCheck(winSound);
    }
    // the python doesnt have the else infront of the if and thus makes it
    // so that it instantly goes into the credits while the function is
    // checking if it IS in the credits to bring it back
    // i.e it instantly went in and out of credits
    else if (currentScreen == 3) {
      SetWindowTitle("SADIE AND SAM'S SUPER SAUCY CREDITS!");
      SetTargetFPS(60);
      makeCreditsPartOne(clickSound, eggSound);
    }

    else if (currentScreen == 66) {
      SetWindowTitle(" ");
      SetTargetFPS(20);
      dialoguePartOne((char**)forgottenMessages);
      if (messageCount == forgottenMessagesLen-1) {
        messageCount = 0;
        currentScreen = 2;
      }

      if (IsSoundValid(man) && !IsSoundPlaying(man)) {
        SetSoundVolume(man, 1);
        PlaySound(man);
      }
    }

    BeginDrawing();
    printf("%d", currentScreen);
    if (currentScreen == 0) {
      ClearBackground(BLACK);
      Vector2 depthsPos = {
        -30,
        0
      };
      DrawTextureEx(depthsB, depthsPos, 0, 3, GRAY);
      DrawTextureEx(depthsA, depthsPos, 0, 3, Fade(WHITE, depthsOpacity));

      dialoguePartTwo(monoFont, (char**)gasterMessages, 200, 152, windowWidth-300, windowHeight-252, 3, 10, BLACK);
      dialoguePartTwo(monoFont, (char**)gasterMessages, 200, 152, windowWidth-300, windowHeight-252, 3, 10, Fade(WHITE, opacity));
      dialoguePartTwo(monoFont, (char**)gasterMessages, 200, 148, windowWidth-300, windowHeight-248, 3, 10, BLACK);
      dialoguePartTwo(monoFont, (char**)gasterMessages, 200, 148, windowWidth-300, windowHeight-248, 3, 10, Fade(WHITE, opacity));
      dialoguePartTwo(monoFont, (char**)gasterMessages, 198, 150, windowWidth-298, windowHeight-250, 3, 10, BLACK);
      dialoguePartTwo(monoFont, (char**)gasterMessages, 198, 150, windowWidth-298, windowHeight-250, 3, 10, Fade(WHITE, opacity));
      dialoguePartTwo(monoFont, (char**)gasterMessages, 202, 150, windowWidth-302, windowHeight-250, 3, 10, BLACK);
      dialoguePartTwo(monoFont, (char**)gasterMessages, 202, 150, windowWidth-302, windowHeight-250, 3, 10, Fade(WHITE, opacity));
      dialoguePartTwo(monoFont, (char**)gasterMessages, 200, 150, windowWidth-300, windowHeight-252, 3, 10, WHITE);
    }

    else if (currentScreen == 1) {
      clearText(BLACK);
      dialoguePartTwo(monoFont, (char**)otherMessages, 200, 100, windowWidth-300, windowHeight-200, 3, 0, WHITE);
      if (messageCount == 2) {
        clearText(Fade(WHITE, opacity));
      }
    }

    else if (currentScreen == 2) {
      ClearBackground(WHITE);
      DrawRectangle(0, 600, windowWidth, 100, GRAY);
      Vector2 blingoPos = {
        290,
        600
      };
      DrawTextEx(sansFont, "SADIE AND SAM'S SUPER SAUCY BLINGO BLIZZARD!", blingoPos, standardFontSize*2, 1, GREEN);
      Vector2 descPos = {
        290,
        630
      };
      DrawTextEx(sansFont, "you only win the race if you beat all chapters and secret bosses\nAND fill outa bingo! for the easiest time verifying your bingo,\nstream your playthrough! hover over a card for details.", descPos, standardFontSize*1, 0, GREEN);
      DrawRectangle(0, 0, 280, windowHeight, BLACK);
      for (int col = 1; col < 6; col++) {
        for (int row = 1; row < 6; row++) {
          makeCardPartTwo(row, col, ((row-1)+(col-1)*5), sansFont, monoFont);
        }
      }
      makeCreditsPartTwo(sansFont, eggImage);
    }

    else if (currentScreen == 3) {
      clearText(RAYWHITE);
      Vector2 creditsImagePos = {
        110, 0
      };
      DrawTextureEx(creditsImage, creditsImagePos, 0, 0.5f, WHITE);
      Vector2 p1 = {5, 0};
      DrawTextEx(sansFont, "also thanks to:\ndeltarune dev team (made this possible, music, sounds, assets, etc.)\nkolibri (helped me program and ported everything to C thanks dude ily)\nraylib dev team (i'm using it)\npython raylib bindings devs (i'm also using it)\n@JapanYoshi on behance.net (this awesome font)", p1, standardFontSize*1, 1, BLACK);
      CardLimits samCard = {150, 210, 150+260, 210+270};
      if (isCursorInCard(samCard)) {
        Vector2 sam1 = {240, 140};
        DrawTextEx(sansFont, "SAM", sam1, standardFontSize*4, 1, BLACK);
        Vector2 sam2 = {150, 480};
        DrawTextEx(sansFont, "he/they/neos\nalso known as reaper or awolen\nguy who made this.\nprogrammer, gave some ideas for\nbingo cards but not a lot.", sam2, standardFontSize*1, 1, BLACK);
      }

      CardLimits sadieCard = {470, 240, 470+290, 240+300};
      if (isCursorInCard(sadieCard)) {
        Vector2 sadie1 = {550, 170};
        DrawTextEx(sansFont, "SADIE", sadie1, standardFontSize*4, 1, BLACK);
        Vector2 sadie2 = {470, 540};
        DrawTextEx(sansFont, "she/any\nalso known as amelia or talistelis\ngal who made this.\ngave most of the bingo card ideas, drew\nthis awesome art.", sadie2, standardFontSize*1, 1, BLACK);
      }
      makeCreditsPartTwo(sansFont, eggImage);
    }

    else if (currentScreen == 66) {
      clearText(BLACK);
      animateEggRoom();
      DrawRectangle(40, 490, 840, 190, WHITE);
      DrawRectangle(50, 500, 820, 170, BLACK);
      dialoguePartThree(monoFont, (char**)forgottenMessages, 70, 520, 2.5f, 0, WHITE);
      visitedEggRoom = true;
    }

    EndDrawing();
  }

  CloseWindow();
  CloseAudioDevice();
}
