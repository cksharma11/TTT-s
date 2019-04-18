#include <stdio.h>
int SIZE_OF_BOARD = 9;
typedef struct player player;

void printBoard(char board[])
{
  printf("_%c_|_%c_|_%c_\n", board[0], board[1], board[2]);
  printf("_%c_|_%c_|_%c_\n", board[3], board[4], board[5]);
  printf(" %c | %c | %c \n", board[6], board[7], board[8]);
}

struct player
{
  char name;
  int moves[5];
  char symbol;
  int moveCount;
};

int hasWon(int playersMove[])
{
  int winningCombinations[8][3] = {{1, 2, 3},
                                   {4, 5, 6},
                                   {7, 8, 9},
                                   {1, 5, 9},
                                   {3, 5, 7},
                                   {1, 4, 7},
                                   {2, 5, 8},
                                   {3, 6, 9}};
  for (int index = 0; index < 8; index++)
  {
    if (isSubset(playersMove, winningCombinations[index]))
    {
      return 1;
    }
  }
  return 0;
}

int isSubset(int set[5], int winningCombination[3])
{
  int FLAG = 0;
  for (int winComIndex = 0; winComIndex < 3; winComIndex++)
  {
    for (int setIndex = 0; setIndex < 5; setIndex++)
    {
      if (set[setIndex] == winningCombination[winComIndex])
      {
        FLAG = 1;
        continue;
      }
      FLAG = 0;
    }
  }
  return FLAG;
}

int makeMove()
{
  int move;
  printf("Enter your mmove : ");
  scanf("%d", &move);
  return move;
}

int updatePlayer(int currentPlayerIndex)
{
  return 1 - currentPlayerIndex;
}

int main(void)
{
  char board[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
  int player1moves[5] = {0, 0, 0, 0, 0};
  int player2moves[5] = {0, 0, 0, 0, 0};
  int currentPlayerIndex = 0;

  player player1 = {.name = 'A', .moves = player1moves, .symbol = 'X', .moveCount = 0};
  player player2 = {.name = 'B', .moves = player2moves, .symbol = 'O', .moveCount = 0};
  player players[2] = {player1, player2};
  printBoard(board);

  while (!hasWon(players[currentPlayerIndex].moves))
  {
    int move = makeMove();
    player currentPlayer = players[currentPlayerIndex];
    board[move - 1] = currentPlayer.symbol;
    currentPlayer.moves[currentPlayer.moveCount] = move;

    currentPlayer.moveCount = currentPlayer.moveCount + 1;
    currentPlayerIndex = updatePlayer(currentPlayerIndex);

    printBoard(board);
  }

  return 0;
}