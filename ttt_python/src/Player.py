class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = []

    def makeMove(self, position):
        self.moves.append(position)

    def getMoves(self):
        return self.moves

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.name
