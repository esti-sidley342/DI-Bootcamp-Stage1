MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''   

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = [list(row) for row in MATRIX_STR.strip().splitlines()]

print(matrix)


# Step 2: Iterate through columns
# ... code to iterate through columns ...
column_text = "" 

rows = len(matrix) #deal with rows
cols = len(matrix[0]) #deal with columns

for col in range(cols): #for each column, start from the first column and move to the next column
    for row in range(rows):  #loop through rows
        column_text += matrix[row][col] #add the character to column_text

print("Column-wise traversal:")
print(column_text)

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...
temp = ""

for char in column_text: #loop through each character in column_text
    if char.isalpha(): #check if the character is an alphabet
        temp += char #add the character to temp string if it is an alphabet

print("\nAlpha characters only:")
print(temp)

for col in range(cols): #loop through each column
    for row in range(rows): #loop through each row
        char = matrix[row][col] #get the character at the current row and column

        if char.isalpha(): #check if the character is an alphabet
            temp += char #add the character to temp string if it is an alphabet

print(temp)

# Step 4: Replace symbols with spaces
def decoded_message(text): 
    result = ""
    symbol_found = False

    for char in text:

        if char.isalpha():

            if symbol_found and result:
                result += " "

            result += char
            symbol_found = False #if the character is an alphabet, set symbol_found to False

        else:
            symbol_found = True #if the character is not an alphabet, set symbol_found to True and add a space to the result

    return result

# ... code to replace symbols with spaces ...

# Step 5: Print the decoded message
message = decoded_message(column_text)

print("\nDecoded message:")
print(message)