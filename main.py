# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Main
# Description: Acts as the primary user interface and client for microservices.

import pyfiglet
import random
import zmq
from pyautogui import hotkey


class Randomizer:
    """A randomizer object is an instance of the Randomizer app."""
    def __init__(self):
        random.seed()
        self.socket_a = connect_socket(2025) # Random activity service
        self.socket_b = connect_socket(2026) # Random fact service
        self.socket_c = connect_socket(2027) # Random inspirational quote service
        self.socket_d = connect_socket(2028) # Random recipe suggestion
        self.title_font = pyfiglet.DEFAULT_FONT

    def print_title(self) -> None:
        """Prints out the title in either default font or a randomly selected font."""
        title = pyfiglet.figlet_format("The Randomizer", self.title_font, width=256)
        print("\n", title, '_' * 256, sep='')

    def main_menu(self) -> None:
        clear()
        self.print_title()
        print("", "Welcome to the randomizer! Select an option from the menu below, press 'H' for help, or 'Q' to quit.",
              "", "1. Generate a random number", "2. Suggest a random activity", "3. View a random inspirational quote",
              "4. Learn a random fact", "5. Get a random recipe suggestion", "6. Randomize Font", "7. Surprise me!", sep="\n")
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
                    self.random_activity()
                case "3":
                    self.random_quote_menu()
                case "4":
                    self.random_fact_menu()
                case "5":
                    self.random_recipe_menu()
                case "6":
                    self.randomize_font()
                    self.main_menu()
                case "7":
                    self.surprise_me()
                case _:
                    print("Invalid input, please try again.")

    def generate_random(self) -> None:
        """Outputs a random number to the screen."""
        rand_num = str(random.randint(0, 1000))
        clear()
        self.print_title()
        print("\n", f"Your random number is: {rand_num}", "\n" * 3,"Enter Y to generate another random number or any other key to return." )
        user_input = input("")
        if user_input.lower() == 'y':
            self.generate_random()
        else:
            self.main_menu()

    def random_activity(self) -> None:
        """Outputs a random activity suggestion to the screen."""
        rand = str(random.randint(0, 39))
        self.socket_a.send_string(rand)
        activity = self.socket_a.recv().decode()
        clear()
        self.print_title()
        print("\n", f"You should try: {activity}", "\n" * 3, f"Enter Y to receive another suggestions or any other key "
                                        f"to return.")
        user_input = input("")
        if user_input.lower() == 'y':
            self.random_activity()
        else:
            self.main_menu()

    def random_quote_menu(self) -> None:
        """Prints the random quote sub menu."""
        clear()
        self.print_title()
        print("", "Select an option from the menu below, or any other key to return to the main menu.",
              "", "1. Inspiration from an artist", "2. Inspiration from a historical figure",
              "3. Inspiration from an innovator", "4. Surprise me!", sep="\n")
        while True:
            user_input = input("")
            match user_input:
                case "1" | "2" | "3" | "4":
                    self.random_quote(user_input)
                case _:
                    self.main_menu()

    def random_quote(self, option) -> None:
        """Outputs a random inspirational quote to the screen."""
        options = {"1": "Artist ", "2": "Historical Figure ", "3": "Innovator ", "4": ""}
        self.socket_c.send_string(option)
        quote = self.socket_c.recv().decode()
        clear()
        self.print_title()
        print("\n", quote, "\n" * 3, f"Enter Y to generate another random inspirational {options[option]}quote, R to "
                                     f"return to previous menu, or any other key to return.")
        user_input = input("")
        match user_input:
            case "Y" | 'y':
                self.random_quote(option)
            case "R" | 'r':
                self.random_quote_menu()
            case _:
                self.main_menu()

    def random_fact_menu(self) -> None:
        """Prints the random fact sub menu."""
        clear()
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

    def random_fact(self, option: str) -> None:
        """Outputs a random fact to the screen."""
        options = {"1": "Science ", "2": "History ", "3": "Pop Culture ", "4": ""}
        self.socket_b.send_string(option)
        fact = self.socket_b.recv().decode()
        clear()
        self.print_title()
        print("\n", fact, "\n" * 3, f"Enter Y to generate another random {options[option]}fact, R to return to previous"
                    f" menu, or any other key to return.")
        user_input = input("")
        match user_input:
            case "Y" | 'y':
                self.random_fact(option)
            case "R" | 'r':
                self.random_fact_menu()
            case _:
                self.main_menu()

    def random_recipe_menu(self) -> None:
        """Prints the random recipe sub menu."""
        clear()
        self.print_title()
        print("", "Select an option from the menu below, or any other key to return to the main menu.",
              "", "1. Get an appetizer suggestion", "2. Get an entree suggestion",
              "3. Get a dessert suggestion", "4. Surprise me!", sep="\n")
        while True:
            user_input = input("")
            match user_input:
                case "1" | "2" | "3" | "4":
                    self.random_recipe(user_input)
                case _:
                    self.main_menu()

    def random_recipe(self, option: str) -> None:
        """Outputs a random recipe idea to the screen."""
        options = {"1": "Appetizer ", "2": "Entree ", "3": "Dessert ", "4": ""}
        self.socket_d.send_string(option)
        recipe = self.socket_d.recv().decode()
        clear()
        self.print_title()
        print("\n", recipe, "\n" * 3, f"Enter Y to generate another random {options[option]}suggestion, R to return to previous"
                    f" menu, or any other key to return.")
        user_input = input("")
        match user_input:
            case "Y" | 'y':
                self.random_recipe(option)
            case "R" | 'r':
                self.random_recipe_menu()
            case _:
                self.main_menu()

    def set_title_font(self, font: str) -> None:
        """Updates the title font."""
        self.title_font = font

    def randomize_font(self) -> None:
        """Randomly changes the title font."""
        fonts = [pyfiglet.DEFAULT_FONT, 'slant', 'alphabet', '3-d', '3x5', '5lineoblique', 'banner3-D', 'doh',
                 'isometric1','letters', 'dotmatrix', 'bubble', 'bulbhead', 'digital']
        rand = random.randint(0, 100)
        new_font = fonts[rand % len(fonts)]
        self.set_title_font(new_font)

    def surprise_me(self) -> None:
        """Randomly chooses an option from the main menu."""
        random.choice([self.generate_random, self.random_quote, self.random_fact])()

    def help_screen(self) -> None:
        """Displays help screen to user."""
        clear()
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
        clear()
        self.print_title()
        print('\n', "Are you sure you want to quit? Press any key to return to the main menu, or 'Q' to quit.")
        user_input = input("")
        match user_input:
            case "q" | "Q":
                quit()
            case _:
                self.main_menu()

def connect_socket(port: int) -> zmq.Socket:
    """Creates a ZeroMQ TCP connection to communicate with microservices."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")
    return socket

def clear() -> None:
    """Clears the screen."""
    hotkey('ctrl', 'shift', ';')

if __name__ == '__main__':
    app = Randomizer()
    app.main_menu()
