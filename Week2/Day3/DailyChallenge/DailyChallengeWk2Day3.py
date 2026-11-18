import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

# Store numbers we've already seen
seen = set()

# Store matching pairs
pairs = []

for num in list_of_numbers: # Iterate through each number in the list
    complement = target_number - num # Calculate the complement that would sum with the current number to reach the target

    if complement in seen: # If the complement has already been seen, we have found a pair
        pairs.append((complement, num)) # Add the pair to the list of pairs

    seen.add(num) # Add the current number to the set of seen numbers for future reference

# Print all pairs found
for pair in pairs:
    print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}") # Print each pair and their sum