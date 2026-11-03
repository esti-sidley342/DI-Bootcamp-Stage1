board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

print("Welcome to TIC TAC TOE!")


def print_board():
    print("TIC TAC TOE")
    print("*****************")
    print("    1   2   3")
    print("  -------------")
    print(f"1 | {board[0]} | {board[1]} | {board[2]} |")
    print("  -------------")
    print(f"2 | {board[3]} | {board[4]} | {board[5]} |")
    print("  -------------")
    print(f"3 | {board[6]} | {board[7]} | {board[8]} |")
    print("  -------------")
    print("*****************")
    print()


def check_winner(player):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in winning_combos:
        if all(board[i] == player for i in combo):
            return True

    return False


player = "X"

for turn in range(9):
    print_board()
    print(f"Player {player}'s turn...")

    row = int(input(f"Player {player}, enter row (1-3): "))
    col = int(input(f"Player {player}, enter column (1-3): "))

    index = (row - 1) * 3 + (col - 1)

    if board[index] in ["X", "O"]:
        print("That spot is already taken!")
        continue

    board[index] = player

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break

    # Switch players
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print_board()
    print("It's a draw!")