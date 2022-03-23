#Unused player class attempting to incorporate both the x and y player. 

class Player():

    def __init__(self):
        self.symbol = ""



    def set_symbol(self, symbol):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._symbol = symbol

    def make_move(self,player, board):
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player


    def make_move(self,player, board):
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player

    def next_player(self, current):
        if current == "" or current == "o":
            return "x"
        elif current == "x":
            return "o"
