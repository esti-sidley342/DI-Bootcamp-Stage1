# Ask the user for input in the form of an integer number and a length for the list of multiples
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Create a list of multiples
multiples = []

for i in range(1, length + 1):
    multiples.append(number * i) #this will stop the loop when the length is reached and will add the multiples of the number to the list

# Print the list
print(multiples)