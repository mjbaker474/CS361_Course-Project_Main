# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Main
# Description: Acts as the primary user interface and client for microservices.

import pyfiglet
import random
import random_quote_service
import random_fact_service
from pyautogui import hotkey


class Randomizer:
    def __init__(self):
        random.seed()
        self.title_font = pyfiglet.DEFAULT_FONT

    def clear(self) -> None:
        """Clears the screen."""
        hotkey('ctrl', 'shift', ';')

    def print_title(self) -> None:
        """Prints out the title in either default font or a randomly selected font."""
        title = pyfiglet.figlet_format("The Randomizer", self.title_font, width=256)
        print("\n", title, '_' * 256, sep='')

    def set_title_font(self, font) -> None:
        """Updates the title font."""
        self.title_font = font

    def randomize_font(self):
        """Randomly changes the title font."""
        fonts = [pyfiglet.DEFAULT_FONT, 'slant', 'alphabet', '3-d', '3x5', '5lineoblique', 'banner3-D', 'doh',
                 'isometric1','letters', 'dotmatrix', 'bubble', 'bulbhead', 'digital']
        rand = random.randint(0, 100)
        new_font = fonts[rand % len(fonts)]
        self.set_title_font(new_font)

    def main_menu(self) -> None:
        self.clear()
        self.print_title()
        print("", "Welcome to the randomizer! Select an option from the menu below, press 'H' for help, or 'Q' to quit.",
              "", "1. Generate a random number", "2. Receive random inspiration", "3. Learn a random fact",
              "4. Surprise me!", "5. Randomize Font", sep="\n")
        while True:
            user_input = input("")
            match user_input:
                case "q" | "Q":
                    self.quit_screen()
                case "h" | "H":
                    self.help_screen()
                case "1":
                    self.generate_random()
                case "2":
                    self.random_inspiration_menu()
                case "3":
                    self.random_fact_menu()
                case "4":
                    self.surprise_me()
                case "5":
                    self.randomize_font()
                    self.main_menu()
                case _:
                    print("Invalid input, please try again.")

    def random_inspiration_menu(self):
        """Prints the random quote sub menu."""
        self.clear()
        self.print_title()
        print("", "Select an option from the menu below, or any other key to return to the main menu.",
              "", "1. Inspiration from an artist", "2. Inspiration from a historical figure",
              "3. Inspiration from an innovator", "4. Surprise me!", sep="\n")
        while True:
            user_input = input("")
            match user_input:
                case "1" | "2" | "3" | "4":
                    self.random_inspiration(user_input)
                case _:
                    self.main_menu()

    def random_fact_menu(self):
        """Prints the random fact sub menu."""
        self.clear()
        self.print_title()
        print("", "Select an option from the menu below, or any other key to return to the main menu.",
              "", "1. Learn about science", "2. Learn about history",
              "3. Learn about pop culture", "4. Surprise me!", sep="\n")
        while True:
            user_input = input("")
            match user_input:
                case "1" | "2" | "3" | "4":
                    self.random_fact(user_input)
                case _:
                    self.main_menu()

    def help_screen(self) -> None:
        """Displays help screen to user."""
        self.clear()
        self.print_title()
        print("",
              "Welcome to the Randomizer app! This app is designed to increase spontaneity in your life by providing",
              "you random results across various categories. Enter your desired option using the",
              "keyboard when prompted and hit enter to navigate.",
              "", "Press any key to return to the main menu, or 'Q' to quit.", sep='\n')
        user_input = input("")
        match user_input:
            case "q" | "Q":
                self.quit_screen()
            case _:
                self.main_menu()

    def quit_screen(self) -> None:
        """Displays quit confirmation screen to user."""
        self.clear()
        self.print_title()
        print('\n', "Are you sure you want to quit? Press any key to return to the main menu, or 'Q' to quit.")
        user_input = input("")
        match user_input:
            case "q" | "Q":
                quit()
            case _:
                self.main_menu()


    def generate_random(self) -> None:
        """Outputs a random number to the screen."""
        rand_num = str(random.randint(0, 1000))
        self.clear()
        self.print_title()
        print("\n", "Enter Y to generate another random number or any other key to return.", "\n" * 2, f"Your random number is: {rand_num}")
        user_input = input("")
        if user_input.lower() == 'y':
            self.generate_random()
        else:
            self.main_menu()

    def surprise_me(self) -> None:
        """Randomly chooses an option from the main menu."""
        random.choice([self.generate_random, self.random_inspiration, self.random_fact])()


    def random_inspiration(self, option) -> None:
        """Outputs a random inspirational quote to the screen."""
        options = {"1": "Artist ", "2": "Historical Figure ", "3": "Innovator ", "4": ""}
        quote = random_quote_service.random_quote(option)
        self.clear()
        self.print_title()
        print("\n", f"Enter Y to generate another random inspirational {options[option]}quote, R to return to previous"
                    f" menu, or any other key to return.", "\n" * 3, quote)
        user_input = input("")
        match user_input:
            case "Y" | 'y':
                self.random_inspiration(option)
            case "R" | 'r':
                self.random_inspiration_menu()
            case _:
                self.main_menu()

    def random_fact(self, option) -> None:
        """Outputs a random fact to the screen."""
        options = {"1": "Science ", "2": "History ", "3": "Pop Culture ", "4": ""}
        fact = random_fact_service.random_fact(option)
        self.clear()
        self.print_title()
        print("\n", f"Enter Y to generate another random {options[option]}fact, R to return to previous"
                    f" menu, or any other key to return.", "\n" * 3, fact)
        user_input = input("")
        match user_input:
            case "Y" | 'y':
                self.random_fact(option)
            case "R" | 'r':
                self.random_fact_menu()
            case _:
                self.main_menu()

    def run(self):
        self.main_menu()


if __name__ == '__main__':
    app = Randomizer()
    app.run()
