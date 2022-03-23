
class Board():
    """The game board.

    The responsibility of the game board is to keep track of the game board. It has methods for 
   adding the board, adding 0's and x's to the board

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        self.board = []

    def create_board(self):
        for square in range(9):
            self.board.append(square + 1)
        return self.board

    def display_board(self,board):
        print()
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print('-+-+-')
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print('-+-+-')
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print()

