import itertools

# function to determine winners


def win(current_game):

    def all_same(l):
        if ((l.count(l[0]) == len(l)) and (l[0] != 0)):
            return True
        else:
            return False

    # horizontal winner
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # diagonal winner
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True
    
    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position in occupado! Choose another!")
            return game_map, False
        s = " "
        for i in range(len(game_map)):
            s += "  " + str(i)
        print(s)
        if not just_display:
            game_map[row][column] = player  # applies player piece
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        print("Welcome to Tic Tac Toe!")
        print("(enter '69' at any point to exit game)")
        current_player = next(player_choice)
        played = False

        while not played:
            print(f"Current player: {current_player}")
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            # exit game if player enters 69
            if column_choice == 69:
                play = False
                game_won = True
                break
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            # exit game if player enters 69
            if row_choice == 69:
                play = False
                game_won = True
                break
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n): ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                print("Thanks for playing!")
                play = False
            else:
                print("Thanks for playing!")
                play = False