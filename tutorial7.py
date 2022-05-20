game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(player = 0, row = 0, column = 0, just_display = False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player # applies player piece
    for count, row in enumerate(game):
        print(count, row)

# game[0][1] = 1

game_board(just_display=True)
game_board(1, 2, 1)