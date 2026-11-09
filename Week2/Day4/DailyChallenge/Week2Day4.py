#Challenge 1: Sorting
# Step 1: Get Input
words = input("Enter words separated by commas: ")

# Step 2: Split the String and remove spaces
words_list = [word.strip() for word in words.split(",")]

# Step 3: Sort the List
words_list.sort()

# Step 4: Join the Sorted List
sorted_words = ",".join(words_list)

# Step 5: Print the Result
print(sorted_words)

#Challenge 2: Longest Word

# Define a function named longest_word that accepts a sentence as a parameter
def longest_word(sentence):

    # Split the sentence into a list of words using spaces as separators
    words = sentence.split()

    # Create a variable to store the longest word found so far
    longest = ""

    # Loop through each word in the list
    for word in words:

        # Check if the current word is longer than the current longest word
        if len(word) > len(longest):

            # If it is longer, update longest to this word
            longest = word

    # Return the longest word after checking all words
    return longest


# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the function and store the returned longest word
result = longest_word(sentence)

# Print the longest word
print(result)