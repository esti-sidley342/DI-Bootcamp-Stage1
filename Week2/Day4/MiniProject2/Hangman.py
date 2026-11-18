import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

# Hangman stages (0-6 wrong guesses)
hangman_stages = [
    #adds gallows and head, body, arms, and legs as the player makes wrong guesses
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """, 
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play_hangman():
    word = random.choice(wordslist) #chooses a random word from the list
    guessed_letters = [] 
    wrong_guesses = 0 #number of wrong guesses made by the player
    max_wrong = 6 #max wrong guesses before the game ends

    print("Welcome to Hangman!")

    while wrong_guesses < max_wrong:

        # Display current hangman
        print(hangman_stages[wrong_guesses])

        # Build word display
        display_word = ""

        for letter in word: #goes through each letter in the word and checks if it has been guessed
            if letter == " ":
                display_word += " "
            elif letter in guessed_letters: 
                display_word += letter
            else:
                display_word += "_"

        print("Word:", display_word) #displays the current state of the word with guessed letters and underscores for unguessed letters

        # Congratulates the player if they've won and confirms the word
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").lower() #asks the player to input a letter and converts it to lowercase

        # Input validation
        if len(guess) != 1 or not guess.isalpha(): #checks if the input is a single letter and if it is an alphabetic character
            print("Please enter a single letter.") 
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.") #if the letter has already been guessed, it informs the player and shows the guessed letters
            print("Guessed letters:", ", ".join(sorted(guessed_letters))) #confirms the guessed letters in alphabetical order
            continue

        guessed_letters.append(guess) #adds the guessed letter to the list of guessed letters

        # Check guess
        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

    # Final stage (fully drawn hangman)
    print(hangman_stages[wrong_guesses]) 
    print("\n💀 Game Over!")
    print("The word was:", word) #prints word if the player loses

# Start the game
play_hangman()