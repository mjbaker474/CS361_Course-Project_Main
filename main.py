import pyfiglet
import random
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

    def main_screen(self) -> None:
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
                    self.random_inspiration()
                case "3":
                    self.random_fact()
                case "4":
                    self.surprise_me()
                case "5":
                    self.randomize_font()
                    self.main_screen()
                case _:
                    print("Invalid input, please try again.")

    def help_screen(self):
        """Displays help screen to user."""
        self.clear()
        self.print_title()
        print("",
              "Welcome to the Randomizer app! This app is designed to increase spontaneity in your life by providing",
              "you random results across various categories. Enter your desired option using the",
              "keyboard when prompted and hit enter to navigate.",
              "", "Press any key to return to the main menu, or 'Q' to quit.", sep='\n')
        user_input = input("")
        if user_input.lower() == 'q':
            self.quit_screen()
        else:
            self.main_screen()

    def quit_screen(self):
        """Displays quit confirmation screen to user."""
        self.clear()
        self.print_title()
        print('\n', "Are you sure you want to quit? Press any key to return to the main menu, or 'Q' to quit.")
        user_input = input("")
        if user_input.lower() == 'q':
            quit()
        else:
            self.main_screen()

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
            self.main_screen()

    def surprise_me(self) -> None:
        """Randomly chooses an option from the main menu."""
        choice = random.choice([self.generate_random, self.random_inspiration, self.random_fact])
        choice()

    def random_inspiration(self) -> None:
        """Outputs a random inspirational quote to the screen."""
        quotes = [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
            "It does not matter how slowly you go as long as you do not stop. – Confucius",
            "Believe you can and you're halfway there. – Theodore Roosevelt",
            "You miss 100% of the shots you don’t take. – Wayne Gretzky - Michael Scott",
        ]
        quote = random.choice(quotes)
        self.clear()
        self.print_title()
        print("\n", "Enter Y to generate another random inspiration quote or any other key to return.", "\n" * 2, quote)
        user_input = input("")
        if user_input.lower() == 'y':
            self.random_inspiration()
        else:
            self.main_screen()

    def random_fact(self) -> None:
        """Outputs a random fact to the screen."""
        facts = [
            "Bananas are berries, but strawberries are not.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs over 3,000 years old.",
            "The Eiffel Tower can grow by more than 6 inches during the summer due to metal expansion.",
            "Octopuses have three hearts and blue blood.",
            "Wombat poop is cube-shaped to prevent it from rolling away.",
        ]
        fact = random.choice(facts)
        self.clear()
        self.print_title()
        print("\n", "Enter Y to generate another random fact or any other key to return.", "\n" * 2, fact)
        user_input = input("")
        if user_input.lower() == 'y':
            self.random_fact()
        else:
            self.main_screen()

    def run(self):
        self.main_screen()


if __name__ == '__main__':
    app = Randomizer()
    app.run()
