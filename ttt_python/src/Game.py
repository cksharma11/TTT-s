from Board import Board
from Player import Player
import numpy as np

class Game:
    def __init__(self, player1,player2, board):
        self.players = [player1, player2]
        self.board = board
        self.winningCombinations = [[1,2,3],[4,5,6],[7,8,9,],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

    def updateCurrentPlayer(self):
        self.players = [self.players[1]] + [self.players[0]]

    def getCurrentPlayer(self):
        return self.players[0]

    def makeMove(self,position):
        self.getCurrentPlayer().makeMove(position)
        self.board.placeSymbol(position-1, self.getCurrentPlayer().getSymbol())

    def hasWon(self):
        playerMoves = self.getCurrentPlayer().getMoves()
        return any(all(move in playerMoves for move in combination) for combination in self.winningCombinations)

    def isPlaceEmpty(self, position):
        return self.board.isPlaceEmpty(position-1)
    
    def printBoard(self):
        self.board.printBoard()

    def isDraw(self):
        return self.board.areAllPlaceOccupied()
