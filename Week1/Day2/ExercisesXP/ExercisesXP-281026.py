print ("Hello, World!\n" * 4)

first_calc = (99**3)*8
print(first_calc)

#>>> 5 < 3 # false
#>>> 3 == 3 # true
#>>> 3 == "3" # false
#>>> "3" > 3 # false
#>>> "Hello" == "hello" # false
# except these don't work because they are not valid Python syntax:

computer_brand = "HP"
print(f"My computer brand is {computer_brand}")

info = {
    "computer_brand": "HP",
    "age": 40,
    "shoe_size": 6
}
print(f"My computer brand is {info['computer_brand']}, I am {info['age']} years old, and my shoe size is {info['shoe_size']}.")

a = 7
b = 3
if a > b:
    print("Hello World")

even_number = input("Enter a number between 1 and 100: ")
if int(even_number) % 2 == 0:
    print("You entered an even number.")
else:
    print("You entered an odd number.")

my_name = "Dolly"
your_name = input("What is your name? ")
if your_name == my_name:
    print("Well, what are the chances in this crazy world!")
elif your_name != my_name:
    print("That's a shame. Dolly is the best name ever. Especially if you're a tuxedo cat!")

your_height = int(input("What is your height in cm? "))
if your_height > 145:
    print("You are tall enough to ride the roller coaster.")
else:
    print("Sorry, you need to grow a little more first!")