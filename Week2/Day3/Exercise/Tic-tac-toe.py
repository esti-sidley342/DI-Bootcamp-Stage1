# Define the board and its layout
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

print("Welcome to TIC TAC TOE!")


def display_instructions():
    print("    1   2   3")
    print("*************")
    print("*   |   |   *")
    print("*---|---|---*")
    print("*   |   |   *")
    print("*---|---|---*")
    print("*   |   |   *")
    print("*************")
    print()


def display_board():
    print("TIC TAC TOE")
    print("*************")
    print(f"* {board[0]} | {board[1]} | {board[2]} *")
    print("*---|---|---*")
    print(f"* {board[3]} | {board[4]} | {board[5]} *")
    print("*---|---|---*")
    print(f"* {board[6]} | {board[7]} | {board[8]} *")
    print("*************")
    print()


def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): "))
            col = int(input(f"Player {player}, enter column (1-3): "))

            if row not in [1, 2, 3] or col not in [1, 2, 3]:
                print("Please enter numbers between 1 and 3.")
                continue

            index = (row - 1) * 3 + (col - 1)

            if board[index] != " ":
                print("That spot is already taken!")
                continue

            return index

        except ValueError:
            print("Please enter valid numbers.")


def check_winner(player):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combos:
        if all(board[i] == player for i in combo):
            return True

    return False


display_instructions()

player = "X"

for turn in range(9):
    display_board()

    index = player_input(player)

    board[index] = player

    if check_winner(player):
        display_board()
        print(f"Player {player} wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    display_board()
    print("It's a draw!")