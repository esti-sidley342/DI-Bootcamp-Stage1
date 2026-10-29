# Exercise 1


my_fave_numbers = {2, 3, 7, 11, 17, 21}
my_fave_numbers.add(27) #adds one more number
my_fave_numbers.add(30) #adds one more number
my_fave_numbers.pop() #removes last item
print(my_fave_numbers)

friend_fav_numbers = {4, 8, 18, 24, 28, 32}

our_fave_numbers = my_fave_numbers | friend_fav_numbers #combines both sets
print(our_fave_numbers)

#Exercise 2
my_tuple = (1, 2, 3, 4, 5)
#my_tuple.add (6) doesn't work because you can't add more to a tuple
my_tuple2 = (6, 7, 8, 9, 10)
combined_tuple = my_tuple + my_tuple2 #combines both tuples because you can't add more to a tuple
print(combined_tuple)

#Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana") #removes banana
basket.remove("Blueberries") #removes blueberries
basket.append("Kiwi") #adds kiwi
basket.insert(0, "Apples") #adds apples to the beginning of the list
print(basket.count("Apples")) #counts how many apples are in the list

basket.clear() #clears the basket
print(basket) #prints the basket which is now empty

#Exercise 4
#Difference between a float and an integer is a float is a number with a decimal point and an integer is a whole number without a decimal point. 

combo_floats_int = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(combo_floats_int)

combo_floats_int2 = [i / 2 for i in range(3, 11)] #creates a list of numbers from 1.5 to 5 by generating an integer from 3 to 11 and dividing it by 2
print(combo_floats_int2)

#Exercise 5
for i in range(1, 21): #prints numbers from 1 to 20
    print(i)

    for i in range(1, 21): #prints numbers from 1 to 20
        if i % 2 == 0: #checks if the number is even
            print(i) #prints the even number

#Exercise 6

while True:
    name = input("What is your name? ") #Asks for the name
    if len(name) < 3: #name needs to be a minimum of 3 characters long
        print("Name needs to be at least 3 characters long.")
    elif name.isdigit(): #checks that numbers were not entered
        print("Name cannot be a number.")
    else: #if the name is valid, it will print thank you and break the loop
        print("Thank you")
        break
            
#Exercise 7
fave_fruits = input(
    "What are your favorite fruits? Separate them with commas: "
).lower().split(",") #asks for favorite fruits and splits them into a list and converts eveything to lower case

fave_fruits = [fruit.strip() for fruit in fave_fruits] #removes any extra spaces from the fruits in the list

fruit = input("Enter the name of a fruit: ").lower().strip() #asks user to enter more fruits

if fruit in fave_fruits:
    print("You chose one of your favorite fruits! Enjoy!") #if it matches the previous list they gave, it prints this message
else:
    print("You chose a new fruit. I hope you enjoy!") #if it is not, it will print this message

#Exercise 8
base_price = 10.00
topping_price = 2.50
pizza_toppings_count = 0

pizza_toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").lower().strip() #asks user to enter pizza toppings
    if topping == "quit": #if they type quit, it will break the loop
        break
    else:
        pizza_toppings.append(topping) #adds the topping to the list

    pizza_toppings.append(topping) #adds the topping to the list
    print(f"Adding {topping} to your pizza.") #prints the current list of toppings

    pizza_toppings_count += 1 #increments the count of toppings by 1
    print(f"Added {topping}!") #confirms what user just entered
    print(f"\nTotal toppings: {pizza_toppings_count}") #confirms total number of toppings
print(f"Total cost: ${pizza_toppings_count * topping_price + base_price:.2f}") #confirms total cost of pizza with toppings and base price

#Exercise 9
total_cost = 0
while True:
    age = input("Enter your age (or type 'quit' to finish): ") #asks user to enter their age
    if age.lower() == "quit": #if they type quit, it will break the loop
        break

    age = int(age) #converts the age to an integer
    if age < 3: #if the age is less than 3, it will print that the ticket is free
        print("This ticket is free.")
    elif 3 <= age <= 12: #if the age is between 3 and 12, it will print the cost
        print("This ticket is $10.")
        total_cost += 10
    else: #if the age is 13 or older, it will print the cost
        print("This ticket is $15.")
        total_cost += 15

print(f"Total cost for all your tickets: ${total_cost:.2f}") #confirms total cost of all tickets