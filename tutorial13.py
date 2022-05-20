game = [[1, 0, 1],
        [1, 1, 0],
        [1, 2, 0]] 

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range (len(game)):
    diags.append(game[ix][ix])

# def win(current_game):
#     for row in game:
#         print(row)
#         if ((row.count(row[0]) == len(row)) and (row[0] != 0)):
#             print("winner!")

#     for col in range(len(game)):
#         check = []
#         for row in game: 
#             check.append(row[col])
        
#         if ((check.count(check[0]) == len(check)) and (check[0] != 0)):
#             print("winner!")   

# win(game)



# game = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

# def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
#     try:
#         print("   0  1  2")
#         if not just_display:
#             game_map[row][column] = player # applies player piece
#         for count, row in enumerate(game_map):
#             print(count, row)

#         return game_map
        
#     except IndexError as e:
#         print("Error: Make sure you input row/column as 0, 1 or 2", e)
#     except Exception as e:
#         print("Something went very wrong!", e)

# game = game_board(game, just_display=True)
# game = game_board(game_board, player = 1, row = 3, column = 1)