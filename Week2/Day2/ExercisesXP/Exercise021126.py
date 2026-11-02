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