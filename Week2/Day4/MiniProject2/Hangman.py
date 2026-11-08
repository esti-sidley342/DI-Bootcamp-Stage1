import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

# Hangman stages (0-6 wrong guesses)
hangman_stages = [
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
    word = random.choice(wordslist)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")

    while wrong_guesses < max_wrong:

        # Display current hangman
        print(hangman_stages[wrong_guesses])

        # Build word display
        display_word = ""

        for letter in word:
            if letter == " ":
                display_word += " "
            elif letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word:", display_word)

        # Win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.")
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

    # Final stage (fully drawn hangman)
    print(hangman_stages[wrong_guesses])
    print("\n💀 Game Over!")
    print("The word was:", word)

# Start the game
play_hangman()