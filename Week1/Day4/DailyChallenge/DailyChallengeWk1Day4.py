#Challenge 1
# Ask the user for input in the form of an integer number and a length for the list of multiples
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Create a list of multiples
multiples = []

for i in range(1, length + 1):
    multiples.append(number * i) #this will stop the loop when the length is reached and will add the multiples of the number to the list

# Print the list
print(multiples)

#Challenge 2

# Ask the user for a string
text = input("Enter a string, with duplicate letters so I can have fun showing you that I've removed the duplicates: ")

# Start the new string with the first character
result = text[0]

# Check each character against the previous one, removes it if it is the same, and adds it to the new string if it is different
for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        result += text[i]

# Print the result
print(result)