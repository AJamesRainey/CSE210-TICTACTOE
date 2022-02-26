'''
James Rainey
CSE210
02/25/2022
file: tictactoefinal.py

Description: Create a tic tac toe game to run in terminal.
Finally rewrote and learned some new things based on the 
final solution!
'''



class Board():
    def __init__(self):
        pass
    def create_board(self):
        board = []
        for square in range(9):
            board.append(square + 1)
        return board

    def display_board(self,board):   
        print()
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print('-+-+-')
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print('-+-+-')
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print()


class Game:
    def __init__(self):
        pass
    def determine_player(self, current):
        if current == "o":
            return "x"
        elif current == "x":
            return "o"
    def check_win(self, board):
        return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    def check_draw(self, board):
        for square in range(9):
            if board[square] != "x" and board[square] != "o":
                return False
        return True         

    def make_move(self, player, board):
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player

    def next_player(self, current):
        if current == "" or current == "o":
            return "x"
        elif current == "x":
            return "o"

def main():
    game = Game()
    player = game.determine_player("o")
    board = Board()
    game_board = board.create_board()
    while not (game.check_win(game_board) or game.check_draw(game_board)):
        board.display_board(game_board)
        game.make_move(player,game_board)
        player = game.next_player(player)
    board.display_board(game_board)
    print("Good game. Thanks for playing!")    

if __name__ == "__main__":
    main()