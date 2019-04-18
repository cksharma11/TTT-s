class Player
  def initialize(name, symbol)
    @name = name
    @symbol = symbol
    @moves = []
  end

  def makeMove(move)
    @moves.insert(move)
  end

  def getSymbol
    @symbol
  end

  def getMoves
    @moves
  end
end