from src.Board import Board
from src.Player import Player
from src.Game import Game

def getValidMoveMove(game):
    move = int(raw_input(game.getCurrentPlayer().getName() + "'s turn :"))
    while(game.isPlaceEmpty(move)):
            print("Place is already occupied!")
            move =  getValidMoveMove(game)
    return move

def showSymbols(player1, player2):
    print(player1 + "'s symbol is X")
    print(player2 + "'s symbol is O")

def createGame():
    board = Board()
    player1Name = raw_input("Enter First Player Name : ")
    player2Name = raw_input("Enter Second Player Name : ")
    player1 = Player(player1Name, "X")
    player2 = Player(player2Name, "O")
    showSymbols(player1Name, player2Name)
    game = Game(player1, player2, board)
    return game

def conductGame(game):
    while(game.isDraw() != True):
        game.printBoard()
        currentPlayerMove = getValidMoveMove(game)
        game.makeMove(currentPlayerMove)
        if(game.hasWon()):
            game.printBoard()
            print(game.getCurrentPlayer().getName() + " has Won!")
            return
        game.updateCurrentPlayer()

    print("Draw !")

def main():
    game = createGame()
    conductGame(game)

main()