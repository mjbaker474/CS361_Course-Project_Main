# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Main
# Description: Acts as the primary user interface and client for microservices.

import pyfiglet
import os
import ctypes
import random
import time
from pyautogui import hotkey
from pyfiglet import DEFAULT_FONT



def main():
    main_screen()



def process_input(user_input:str) -> None:
    match user_input:
        case "q" | "Q":
            quit()
        case "h" | "H":
            help_screen()



def welcome_screen()-> None:
    pass

def help_screen():
    hotkey("ctrl", "shift", ";")
    print_title()
    print_help_screen()
    user_input = input("")
    match user_input:
        case "q" | "Q":
            quit()
        case _ :
            main_screen()

def main_screen(title:int = 0) -> None:
    hotkey("ctrl", "shift", ";")
    print_title(title)
    print_main_menu()
    while True:
        user_input = input("")
        process_input(user_input)
        time.sleep(1)

def message_box():
    ctypes.windll.user32.MessageBoxW(0, "TEst", "Titles Test", 1)

def print_title(font_number: int = 0) -> None:
    """Prints out the title in either default font or font based off of random number passed to the function."""
    fonts = [DEFAULT_FONT, 'slant', 'alphabet', '3-d', '3x5', '5lineoblique', 'banner3-D', 'doh', 'isometric1',
             'letters', 'dotmatrix', 'bubble', 'bulbhead', 'digital']
    title = pyfiglet.figlet_format("The Randomizer", font=fonts[font_number], width = 256)
    print("\n", title, '_'*256, sep='')

def print_main_menu() -> None:
    """Prints out the main menu"""
    print("", "Welcome to the randomizer! Select an option from the menu below, press 'H' for help, or 'Q' to quit.",
          "", "1. Option 1", "2. Option 2", "3. Option 3", "4. Option 4", sep = "\n")

def print_help_screen() -> None:
    """Prints out the help screen."""
    print("", "Welcome to the Randomizer app! This app is designed to increase the spontaneity to your life by providing",
              "you random results across a wide variety of categories. Simply enter your desired option using the",
              "keyboard when prompted and hit enter to navigate.  Whether you're looking for inspiration, help making",
              "a decision, or just something unexpected, this app has you covered.","",
                "Press any key to return to the main menu, or 'Q' to quit.", sep='\n')
if __name__ == '__main__':
    main()