#Execise 1
def display_message():
    print("I am learning about functions in Python. Ain't that exciting?") #prints a message about learning functions
display_message() #calls the function to display the message

#Exercise 2
def favorite_book(title="A Streetcat Named Bob"):
    print(f"One of my favorite books is {title}.") #prints a message about the favorite book

#Exercise 3
def describe_city(city="Unknown", country="Unknown"):
    print(f"{city} is in {country}.") #prints a message about the city and country
describe_city("New York", "USA") #calls the function with New York and USA as arguments
describe_city("Tokyo", "Japan") #calls the function with Tokyo and Japan as arguments
describe_city("Paris", "France") #calls the function with Paris and France as arguments
describe_city("London") #calls the function with London and UK as arguments
describe_city("Sydney", "Australia") #calls the function with Sydney and Australia as arguments

#Exercise 4
import random
def get_random_number():
    guess = int(input("Enter a number between 1 and 100: ")) #asks user to enter a number between 1 and 100
    random_number = random.randint(1, 100) #generates a random integer between 1 and 100
    return guess, random_number

guess, random_number = get_random_number()
if guess == random_number:
    print("Success!") #prints a message if the guess is correct
else:
    print(f"Fail! You number: {guess}, Random number: {random_number}") #prints a message if the guess is incorrect

#Exercise 5
def make_shirt(size="Large", text="I love Python"):
    print(f"The shirt size is {size} and the message is '{text}'.") #prints a message about the shirt size and message
make_shirt() #calls the function with default arguments
make_shirt(size="medium") #calls the function with size argument and default text argument
make_shirt(size="small", text="Data Analysis is a slay queen") #calls the function with size and text arguments
make_shirt(size="small", text="Hello!") #calls the function with size and text arguments

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Cris Angel'] #creates a list of magician names
def show_magicians(magician_list): #defines a function that takes a list of magician names as an argument
    for magician in magician_list: #iterates through the list of magician names
        print(magician) #prints each magician name in the list

def make_great(magician_list): #defines a function that takes a list of magician names as an argument
    for i in range(len(magician_list)): #iterates through the list of magician names using their index
        magician_list[i] = "The Great " + magician_list[i] #adds "The Great" to the beginning of each magician name in the list

show_magicians(magician_names) #calls the function to show the original list of magician names

make_great(magician_names) #calls the function to modify the list of magician names by adding "The Great" to each name

show_magicians(magician_names) #calls the function to show the modified list of magician names

#Exercise 7

import random

def get_random_temp(month):
    # Winter: Dec, Jan, Feb
    if month in [12, 1, 2]:
        season = "Winter"
        temperature = random.uniform(-10, 10)

    # Spring: Mar, Apr, May
    elif month in [3, 4, 5]:
        season = "Spring"
        temperature = random.uniform(5, 20)

    # Summer: Jun, Jul, Aug
    elif month in [6, 7, 8]:
        season = "Summer"
        temperature = random.uniform(20, 40)

    # Fall: Sep, Oct, Nov
    elif month in [9, 10, 11]:
        season = "Fall"
        temperature = random.uniform(5, 25)

    else:
        raise ValueError("Invalid month. Please enter a number between 1 and 12.")

    return temperature, season


def main():
    month = int(input("Enter the month as a number (1-12): "))

    temperature, season = get_random_temp(month)

    print(f"Season: {season}")
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 23:
        print("Nice weather.")
    elif 23 <= temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


main()