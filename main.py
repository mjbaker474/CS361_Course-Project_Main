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

    print_title()
    print_main_menu()
    message_box()


def process_input():
    pass

def welcome_screen()-> None:
    pass

def help_screen():
    pass

def message_box():
    ctypes.windll.user32.MessageBoxW(0, "TEst", "Titles Test", 1)

def print_title(font_number: int = 0) -> None:
    """Prints out the title in either default font or font based off of random number passed to the function."""
    fonts = [DEFAULT_FONT, 'slant', 'alphabet', '3-d', '3x5', '5lineoblique', 'banner3-D', 'doh', 'isometric1',
             'letters', 'dotmatrix', 'bubble', 'bulbhead', 'digital']
    title = pyfiglet.figlet_format("The Randomizer", font=fonts[font_number], width = 256)
    print("\n", title, '_'*256, sep='')

def print_main_menu():
    """Prints out the main menu"""
    print("", "Welcome to the randomizer! Select an option from the menu below, press 'H' for help, or 'Q' to quit.",
          "", "1. Option 1", "2. Option 2", "3. Option 3", "4. Option 4", sep = "\n")

if __name__ == '__main__':
    main()