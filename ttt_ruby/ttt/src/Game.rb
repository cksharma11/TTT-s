class Game
  def initialize(board, player1, player2)
    @board = board
    @players = [player1, player2]
    @currentPlayerIndex = 1
    @winningCombinations = [
      [1,2,3],
      [4,5,6],
      [7,8,9],
      [1,4,7],
      [2,5,8],
      [3,6,9],
      [1,5,9],
      [3,5,7]
    ]
  end

  def updateCurrentPlayerIndex
    @currentPlayerIndex = 1 - @currentPlayerIndex;
  end

  def getCurrentPlayer
    @players.at(@currentPlayerIndex)
  end

  def makeMove(move)
    self.getCurrentPlayer.makeMove(move)
    @board.placeSymbol(move - 1, self.getCurrentPlayer.getSymbol())
    self.updateCurrentPlayerIndex
  end

  def won?(moves)
    winningCombinations.any?{|combination| combination.all? { |move| moves.include?(move)}}
  end

  def printBoard
    @board.printBoard()
  end
end