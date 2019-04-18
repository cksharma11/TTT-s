require_relative "src/Board"
require_relative "src/Player"
require_relative "src/Game"

game = Game.new(Board.new(), Player.new("A", "X"), Player.new("B", "O"));

game.makeMove(1);
game.makeMove(2);
game.makeMove(3);
game.makeMove(4);

puts game.printBoard()