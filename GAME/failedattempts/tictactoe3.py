'''
James Rainey
CSE210
01/15/2022
file: tictactoe.py

Description: Create a tic tac toe game to run in terminal. This file is as far as I got without looking at the solution. 
This was my first major attempt at classes, so I knew I was doing some things subpar.
In terms of the actual game, I was able to get the grid to print in the terminal, and the grid to update based on user input, 
but after 4 hours I couldn't get implement the grid updating after every turn or you being able to lose/win/end the game. 
'''

#board class for keeping track of grid values and printing grid
class Board():
    def __init__(self,p1, p2, p3, p4, p5, p6, p7, p8, p9, player, u_input):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.p9 = p9
        self.player = player
        self.u_input = u_input

#function for updating values to be placed on the board
    def spawn_board(player,u_input):
        if u_input != ():
            if u_input == 1:
                p1 = player
            else:
                p1 = 1
            if u_input == 2:
                p2 = player
            else:
                p2 = 2
            if u_input == 3:
                p3 = player
            else:
                p3 = 3
            if u_input == 4:
                p4 = player
            else: p4 = 4
            if u_input == 5:
                p5 = player
            else: p5 = 5
            if u_input == 6:
                p6 = player
            else: p6 = 6
            if u_input == 7:
                p7 = player
            else: p7 = 7
            if u_input == 8:
                p8 = player
            else: p8 = 8
            if u_input == 9:
                p9 = player
            else: p9 = 9


#the game board
        board = (f""" \n
            {p1}|{p2}|{p3} \n
            -+-+- \n 
            {p4}|{p5}|{p6} \n
            -+-+- \n
            {p7}|{p8}|{p9} \n
                
                """)
        print(board)
        return board


#function to print game board
    def print_board():
        board = Board.spawn_board("",())
        print(board)   

#player class to receive input and determine whether player is x or o
class Player():
    player1 = "x"
    player2 = "o"

    def one_player_input():
        user_input = int(input("x's turn to choose a square (1-9): "))
        return user_input
    def two_player_input():
        user_input = int(input("o's turn to choose a square (1-9): "))
        return user_input

    
        
#class for the game loop and calling other functions within other classes
class Game():

    def __init__(self, victory):
        self.victory = victory
        victory = True

    def check_if_won():
        pass


    def play_game():

        while True:
            p1_turn = Player.one_player_input()
            Board.spawn_board(Player.player1, p1_turn)
            #Board.print_board()

            p2_turn = Player.two_player_input()
            Board.spawn_board(Player.player2, p2_turn)
            #Board.print_board()


#main function
def main():
    Game.play_game()



#call main
if __name__ == "__main__":
    main()