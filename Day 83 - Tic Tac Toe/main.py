import random

print("""
___________.____________   ________________  _________   ___________________  ___________
\__    ___/|   \_   ___ \  \__    ___/  _  \ \_   ___ \  \__    ___/\_____  \ \_   _____/
  |    |   |   /    \  \/    |    | /  /_\  \/    \  \/    |    |    /   |   \ |    __)_ 
  |    |   |   \     \____   |    |/    |    \     \____   |    |   /    |    \|        )
  |____|   |___|\______  /   |____|\____|__  /\______  /   |____|   \_______  /_______  /
                       \/                  \/        \/                     \/        \/ 
""")

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
game_is_on = True

def show_board():
    row = ""
    for x in board:
        for y in x:
            row += y + " "
        print(row)
        row = ""

def check_winner():
    global game_is_on
    if board[0][0] == board[1][0] == board[2][0] == "X" or board[0][0] == board[1][1] == board[2][2] == "X" or board[0][
        0] == board[0][1] == board[0][2] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == \
            board[1][2] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X" or board[1][0] == \
            board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X":
        print("You Win!")
        game_is_on = False
    elif board[0][0] == board[1][0] == board[2][0] == "O" or board[0][0] == board[1][1] == board[2][2] == "O" or \
            board[0][0] == board[0][1] == board[0][2] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or \
            board[0][2] == board[1][2] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O" or \
            board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "O":
        show_board()
        print("You Lost!")
        game_is_on = False
    else:
        new_board = ""
        for x in board:
            for y in x:
                new_board += y
        if "-" not in new_board:
            print("Draw!")
            game_is_on = False

def game():
    global game_is_on
    show_board()
    user_choice = input("\nEnter row and column numbers(e.g. 3 2) : ")
    user_choice2 = user_choice.split(" ")
    if board[int(user_choice2[0]) - 1][int(user_choice2[1]) - 1] == "-":
        board[int(user_choice2[0]) - 1][int(user_choice2[1]) - 1] = "X"
    show_board()
    check_winner()
    while game_is_on == True:
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        computer_choice = board[random_row][random_column]
        if computer_choice == "X" or computer_choice == "O":
            continue
        else:
            if board[random_row][random_column] == "-":
                board[random_row][random_column] = "O"
                print("\n-----------------------\n")
                check_winner()
                break
            else:
                continue

while game_is_on == True:
    game()
