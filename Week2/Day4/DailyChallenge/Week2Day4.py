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