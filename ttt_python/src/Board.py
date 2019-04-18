class Board:
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    def placeSymbol(self, position, symbol):
        self.board[position] = symbol

    def printBoard(self):
        print(" _"+self.board[0]+"_|_ "+self.board[1]+"_|_"+self.board[2]+"_")
        print(" _"+self.board[3]+"_|_ "+self.board[4]+"_|_"+self.board[5]+"_")
        print("  "+self.board[6]+" |  "+self.board[7]+" | "+self.board[8]+" ")

    def isPlaceEmpty(self,position):
        return self.board[position] != ' '

    def areAllPlaceOccupied(self):
        return all(place != ' ' for place in self.board)
