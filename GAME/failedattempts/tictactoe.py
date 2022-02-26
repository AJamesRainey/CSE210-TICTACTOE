def create_game_grid():
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0],]
    print(" 0 1 2")

    for count,row in enumerate(grid):
        #print(count,row)
        for item in row:
            print(item)

create_game_grid()