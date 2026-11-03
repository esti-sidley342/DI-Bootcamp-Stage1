def play():

    # Define the board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    print("Welcome to TIC TAC TOE!")

 # Display a guide showing players which row and column numbers to use
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

    def player_input(player): # Get a valid move from the current player, creates a function that takes the current player as an argument and returns the index of the square that the player wants to mark

        while True: # Keep asking until a valid row is entered
            try: # Ask the player for a row number
                row = int(input(f"Player {player}, enter row (1-3): "))    # Asks the player for a row number

                if row not in [1, 2, 3]:  # Check the row is between 1 and 3
                    print("ERROR: Row must be between 1 and 3.")
                    continue # Continue asking for a valid row

                break # Exit the loop if a valid row is entered

            except ValueError: # Catch the case where the input is not a number
                print("ERROR: Row must be a number between 1 and 3.")

        while True: # Keep asking until a valid column is entered
            try: # Ask the player for a column number
                col = int(input(f"Player {player}, enter column (1-3): ")) # Ask the player for a column number

                if col not in [1, 2, 3]: # Check the column is between 1 and 3
                    print("ERROR: Column must be between 1 and 3.") # Print an error message if the column is not valid
                    continue # Continue asking for a valid column

                break # Exit the loop if a valid column is entered

            except ValueError: # Catch the case where the input is not a number
                print("ERROR: Column must be a number between 1 and 3.")

        index = (row - 1) * 3 + (col - 1) # Convert row and column into a board index

        if board[index] != " ": # Check if the square is already occupied
            print("That spot is already taken!")
            return player_input(player) #asks the player for another move if the square is occupied

        return index #return the index of the square that the player wants to mark

    def check_win(board, player): #check if current player has won the game

        winning_combos = [ #all possible winning combinations
            [0, 1, 2], [3, 4, 5], [6, 7, 8], #checks rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], #checks columns
            [0, 4, 8], [2, 4, 6] #checks diagonal combinations
        ]

        for combo in winning_combos: #check each winning combination to see if the current player has won
            if all(board[i] == player for i in combo): # Check if all squares in the combination are marked by the current player
                return True #return True if the current player has won

        return False #return False if the current player has not won

    display_instructions() #shows the board with the row and column numbers to the players

    player = "X" #player x starts first

    display_board() #display the empty board

    for turn in range(9): #allows for a maximum of 9 turns (the number of squares on the board)

        index = player_input(player) #get the index of the square that the current player wants to mark

        board[index] = player #mark the square with the current player's symbol

        display_board() #display the updated board after the current player's move

        if check_win(board, player): #check if the current player has won the game
            print(f"Player {player} wins!") #print a message indicating that the current player has won
            return #end the game if the current player has won

        if player == "X": #switch to the other player for the next turn
            player = "O" #switch to player O
        else: #switch to the other player for the next turn
            player = "X" #switch to player X

    print("It's a draw!") #print a message indicating that the game is a draw if all squares are filled and no player has won


play() #start the game