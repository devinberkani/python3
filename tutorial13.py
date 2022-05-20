import itertools

# function to determine winners
def win(current_game):

    # horizontal winner
    for row in game:
        if ((row.count(row[0]) == len(row)) and (row[0] != 0)):
            print(f"Player {row[0]} is the winner horizontally!")

    # vertical winner
    for col in range(len(game)):
        check = []
        for row in game: 
            check.append(row[col])
        
        if ((check.count(check[0]) == len(check)) and (check[0] != 0)):
            print(f"Player {check[0]} is the winner vertically!")  

    # diagonal winner
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if ((diags.count(diags[0]) == len(diags)) and (diags[0] != 0)):
        print(f"Player {diags[0]} is the winner diagonally (/)!")                   

    diags = []
    for ix in range (len(game)):
        diags.append(game[ix][ix])
    if ((diags.count(diags[0]) == len(diags)) and (diags[0] != 0)):
        print(f"Player {diags[0]} is the winner diagonally (\)!")
        

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player # applies player piece
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map
        
    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2", e)
    except Exception as e:
        print("Something went very wrong!", e)

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"current player: {current_player}")
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)