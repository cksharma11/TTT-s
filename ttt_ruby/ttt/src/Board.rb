class Board
  def initialize()
    @board = Array.new(9).fill(" ")
  end

  def printBoard
    puts @board[0].to_s + "|" + @board[1].to_s + "|" + @board[2].to_s 
    puts @board[3].to_s + "|" + @board[4].to_s + "|" + @board[5].to_s
    puts @board[6].to_s + "|" + @board[7].to_s + "|" + @board[8].to_s
  end

  def placeSymbol(position, symbol)
    @board[position] = symbol
  end
end