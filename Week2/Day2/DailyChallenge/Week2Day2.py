MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = [list(row) for row in MATRIX_STR.strip().splitlines()]

print(matrix)


# Step 2: Iterate through columns
# ... code to iterate through columns ...
rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    print(f"Column {col}: ", end="")
    for row in range(rows):
        print(matrix[row][col], end="")
    print()

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...
matrix = [list(row) for row in MATRIX_STR.strip().splitlines()]

temp = ""

rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    for row in range(rows):
        char = matrix[row][col]

        if char.isalpha():
            temp += char

print(temp)

# Step 4: Replace symbols with spaces
def decoded_message(matrix):
    result = ""

    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            result += char if char.isalpha() else " "

    return " ".join(result.split())
# ... code to replace symbols with spaces ...

# Step 5: Print the decoded message
print(decoded_message)