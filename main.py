# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Main
# Description: Acts as the primary user interface and client for microservices.

import pyfiglet
import os
import random
import time
from pyautogui import hotkey
from pyfiglet import DEFAULT_FONT



def main():
    random.seed()
    main_screen()


def clear() ->None:
    """Clears the screen."""
    hotkey('ctrl', 'shift', ';')

def process_input(user_input:str) -> None:
    match user_input:
        case "q" | "Q":
            quit()
        case "h" | "H":
            help_screen()
        case "1":
            generate_random()
        case "2":
            random_inspiration()
        case "3":
            random_fact()

def welcome_screen()-> None:
    pass

def help_screen():
    clear()
    print_title()
    print_help_screen()
    user_input = input("")
    match user_input:
        case "q" | "Q":
            quit()
        case _ :
            main_screen()

def main_screen(title:int = 0) -> None:
    clear()
    print_title(title)
    print_main_menu()
    while True:
        user_input = input("")
        process_input(user_input)


def generate_random() -> None:
    """Outputs a random number to the screen."""
    rand_num = str(random.randint(0, 1000))
    clear()
    print_title()
    print("\n", "Enter Y to generate another random number or any other key to return. NOTE: Both of these actions "
                "will overwrite your current random number.", "\n"*2, f"Your random number is: {rand_num}",)
    user_input = input("")
    match user_input:
        case "Y" | "y":
            generate_random()
        case _:
            main_screen()

def random_inspiration() -> None:
    """Outputs a random inspirational quote to the screen"""
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky - Michael Scott",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "It always seems impossible until it's done. – Nelson Mandela",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "It is never too late to be what you might have been. – George Eliot",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "Act as if what you do makes a difference. It does. – William James",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "In the middle of every difficulty lies opportunity. – Albert Einstein",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Everything you can imagine is real. – Pablo Picasso",
        "The way to get started is to quit talking and begin doing. – Walt Disney",
        "Dream big and dare to fail. – Norman Vaughan",
        "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis"
    ]
    rand_num = random.randint(0, 1000)
    quote = quotes[rand_num % len(quotes)]
    clear()
    print_title()
    print("\n","Enter Y to generate another random inspiration quote or any other key to return. NOTE: Both of these"
                "actions will overwrite your current quote.", "\n"*2,quote )
    user_input = input("")
    match user_input:
        case "Y" | "y":
            random_inspiration()
        case _:
            main_screen()

def random_fact() -> None:
    """Outputs a random fact to the screen"""
    facts = [
        "Bananas are berries, but strawberries are not.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old.",
        "The Eiffel Tower can grow by more than 6 inches during the summer due to the expansion of the metal from the heat.",
        "Octopuses have three hearts and blue blood.",
        "Wombat poop is cube-shaped to prevent it from rolling away.",
        "A group of flamingos is called a 'flamboyance'.",
        "Sharks have been around longer than trees. Sharks have existed for over 400 million years, while trees have existed for about 350 million years.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
        "A day on Venus is longer than a year on Venus. It takes Venus 243 Earth days to rotate on its axis, but only 225 Earth days to orbit the sun.",
        "The longest hiccuping spree lasted 68 years, experienced by Charles Osborne.",
        "A single cloud can weigh more than 1 million pounds.",
        "An octopus can fit through any hole larger than its beak.",
        "The longest hiccuping spree lasted 68 years, experienced by Charles Osborne.",
        "The name for the shape of Pringles is called a 'Hyperbolic Paraboloid'.",
        "You can hear a blue whale’s heartbeat from over 2 miles away.",
        "There are more stars in the universe than grains of sand on all of Earth’s beaches.",
        "Cows have best friends and get stressed when they are separated.",
        "The shortest commercial flight in the world is just 57 seconds long, between two islands in the Orkney Islands of Scotland.",
        "The smell of freshly cut grass is actually a plant distress signal.",
        "The inventor of the Pringles can is buried in one."
    ]
    rand_num = random.randint(0, 1000)
    fact = facts[rand_num % len(facts)]
    clear()
    print_title()
    print("\n", "Enter Y to generate another random fact or any other key to return. NOTE: Both of these"
                "actions will overwrite your current fact.", "\n" * 2, fact)
    user_input = input("")
    match user_input:
        case "Y" | "y":
            random_fact()
        case _:
            main_screen()

def print_title(font_number: int = 0) -> None:
    """Prints out the title in either default font or font based off of random number passed to the function."""
    fonts = [DEFAULT_FONT, 'slant', 'alphabet', '3-d', '3x5', '5lineoblique', 'banner3-D', 'doh', 'isometric1',
             'letters', 'dotmatrix', 'bubble', 'bulbhead', 'digital']
    title = pyfiglet.figlet_format("The Randomizer", font=fonts[font_number], width = 256)
    print("\n", title, '_'*256, sep='')

def print_main_menu() -> None:
    """Prints out the main menu"""
    print("", "Welcome to the randomizer! Select an option from the menu below, press 'H' for help, or 'Q' to quit.",
          "", "1. Generate a random number", "2. Receive random inspiration", "3. Learn a random fact",
          "4. Option 4", sep = "\n")

def print_help_screen() -> None:
    """Prints out the help screen."""
    print("", "Welcome to the Randomizer app! This app is designed to increase the spontaneity to your life by providing",
              "you random results across a wide variety of categories. Simply enter your desired option using the",
              "keyboard when prompted and hit enter to navigate.  Whether you're looking for inspiration, help making",
              "a decision, or just something unexpected, this app has you covered.","",
                "Press any key to return to the main menu, or 'Q' to quit.", sep='\n')

if __name__ == '__main__':
    main()