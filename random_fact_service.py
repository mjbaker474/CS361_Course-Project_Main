# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Random Fact Service
# Description:  Uses ZeroMQ to serve random facts to client.

import zmq
import random


def random_fact(option: str = "4") -> str:
    """Returns a random fact from 1 of 3 categories or a random category as determined by the option parameter."""
    science_facts = [
        "Water can boil and freeze at the same time, known as the triple point.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts and blue blood.",
        "There is enough DNA in the human body to stretch from the Sun to Pluto and back—17 times!",
        "A day on Venus is longer than a year on Venus.",
        "Hot water freezes faster than cold water, known as the Mpemba effect.",
        "Honey never spoils; edible honey has been found in ancient Egyptian tombs.",
        "Sharks existed before trees; they have been around for over 400 million years.",
        "Neutron stars are so dense that a sugar-cube-sized amount would weigh about a billion tons.",
        "You can’t burp in space because there’s no gravity to separate gas from liquid in your stomach.",
        "There’s a species of jellyfish that can potentially live forever.",
        "An ant can survive a fall from any height because of its small mass and air resistance.",
        "A teaspoon of a neutron star would weigh about six billion tons.",
        "There are more stars in the universe than grains of sand on Earth.",
        "Lightning is five times hotter than the surface of the Sun.",
        "The Eiffel Tower grows taller in the summer due to thermal expansion.",
        "Water expands when it freezes, which is why ice floats.",
        "The average human body carries more bacterial cells than human cells.",
        "A cloud can weigh more than a million pounds.",
        "Wombat poop is cube-shaped.",
        "It rains diamonds on Jupiter and Saturn.",
        "The speed of a sneeze can exceed 100 miles per hour.",
        "Sloths can hold their breath longer than dolphins—up to 40 minutes.",
        "The human stomach gets a new lining every few days to prevent it from digesting itself.",
        "A cockroach can live for weeks without its head.",
        "The Earth's core is as hot as the surface of the Sun.",
        "Your bones are about five times stronger than steel of the same density.",
        "The Great Wall of China is not visible from the Moon with the naked eye.",
        "There's a planet where it rains molten glass sideways.",
        "The smell of freshly-cut grass is actually a plant distress signal.",
        "Blood appears blue in veins due to the way light interacts with skin, but it's always red.",
        "There is a gas cloud in space that smells like rum and tastes like raspberries.",
        "Saturn’s moon Titan has lakes of liquid methane and ethane.",
        "Humans share about 60% of their DNA with bananas.",
        "A single lightning bolt contains enough energy to toast 100,000 slices of bread.",
        "A flea can accelerate faster than a space shuttle.",
        "Sound travels faster in water than in air.",
        "If you remove all the empty space in atoms, the entire human race could fit in a sugar cube.",
        "Butterflies can taste with their feet.",
        "Giraffes only need 30 minutes of sleep per day."
    ]

    history_facts = [
        "The Great Pyramid of Giza was the tallest structure in the world for over 3,800 years.",
        "Cleopatra lived closer in time to the moon landing than to the construction of the pyramids.",
        "Napoleon was once attacked by a horde of bunnies in a hunting mishap.",
        "The shortest war in history was between Britain and Zanzibar in 1896—it lasted only 38 to 45 minutes.",
        "Ancient Romans used urine as a mouthwash and laundry detergent.",
        "The Eiffel Tower was originally meant to be a temporary structure.",
        "The University of Oxford is older than the Aztec Empire.",
        "A chicken survived for 18 months after having its head cut off.",
        "Julius Caesar was once kidnapped by pirates who underestimated his ransom demand.",
        "The guillotine was used in France until 1977.",
        "Albert Einstein was offered the presidency of Israel in 1952 but declined.",
        "George Washington’s teeth were not made of wood but included human, cow, and horse teeth.",
        "Ancient Egyptian doctors used moldy bread to treat infections, anticipating penicillin.",
        "The Eiffel Tower can be 15 cm taller in summer due to expansion from heat.",
        "The oldest known 'your mom' joke is over 3,500 years old, found on a Babylonian tablet.",
        "The U.S. once planned to drop an atomic bomb on the Moon as a show of power during the Cold War.",
        "In the 19th century, ketchup was sold as a medicine.",
        "A medieval knight’s armor could weigh up to 100 pounds, but they were still quite mobile.",
        "The Colosseum in Rome was once filled with water for naval battle reenactments.",
        "Ancient Olympic athletes competed naked.",
        "Winston Churchill was hit by a car in New York City and apologized to the driver.",
        "During World War II, British spies used semen as invisible ink.",
        "A war between Greece and the city of Troy was supposedly started over a golden apple.",
        "The world's first known computer, the Antikythera Mechanism, was built over 2,000 years ago.",
        "Before alarm clocks, people called 'knocker-uppers' were hired to wake others up by tapping on their windows.",
        "During the Great Fire of London in 1666, Samuel Pepys buried his cheese to protect it.",
        "Ancient Romans had fast-food restaurants called 'thermopolia'.",
        "The Leaning Tower of Pisa took 199 years to build and started leaning before it was finished.",
        "The first recorded pizza delivery was made in 1889 to Queen Margherita of Savoy.",
        "A 12th-century sultan built a 'door of bees' as a booby trap against invaders.",
        "The Vikings reached North America around 500 years before Columbus.",
        "Napoleon was once nearly assassinated by an exploding bunch of bread carts.",
        "A pigeon named Cher Ami saved nearly 200 soldiers in World War I.",
        "The oldest known 'knock-knock' joke was found in a 10th-century manuscript.",
        "Ancient Romans cleaned their clothes with fermented urine.",
        "A war between two countries, The Three Hundred and Thirty-Five Years’ War, lasted from 1651 to 1986 with no casualties.",
        "Spartans used iron bars instead of coins to discourage greed.",
        "During Prohibition, the U.S. government poisoned alcohol to discourage drinking, leading to thousands of deaths.",
        "A Japanese soldier kept fighting World War II until 1974, unaware the war had ended."
    ]

    pop_culture_facts = [
        "The voice of Mickey Mouse and the voice of Minnie Mouse were married in real life.",
        "The first-ever music video played on MTV was 'Video Killed the Radio Star' by The Buggles.",
        "Elvis Presley only won three Grammy Awards—and all were for gospel music.",
        "The Simpsons is the longest-running American sitcom, debuting in 1989.",
        "Marvel’s Stan Lee made cameo appearances in nearly every Marvel movie until his passing in 2018.",
        "The famous 'Wilhelm scream' sound effect has been used in over 400 movies.",
        "In the original Pac-Man, the ghosts have different behaviors—only Blinky actively chases you.",
        "James Cameron drew the famous nude portrait of Rose in Titanic himself.",
        "The actor who played Darth Vader, David Prowse, didn’t know his voice would be replaced by James Earl Jones.",
        "The first product ever scanned with a barcode was a pack of Wrigley’s gum.",
        "Friends was originally going to be called 'Insomnia Cafe'.",
        "The Harry Potter books have been translated into more than 80 languages.",
        "Before becoming famous, Brad Pitt dressed as a giant chicken to promote a restaurant.",
        "The original name of Google was 'Backrub'.",
        "The Super Mario Bros. theme song has lyrics—though they were rarely used.",
        "Beyoncé’s alter ego, Sasha Fierce, was created to help her perform more confidently on stage.",
        "Michael Jackson co-wrote the theme song for Sonic the Hedgehog 3.",
        "The first ever YouTube video was uploaded on April 23, 2005, titled 'Me at the Zoo'.",
        "Shrek was originally supposed to be voiced by Chris Farley before his passing.",
        "The famous DeLorean from Back to the Future was originally supposed to be a refrigerator.",
        "Netflix was originally a DVD rental service before switching to streaming.",
        "The first toy advertised on television was Mr. Potato Head in 1952.",
        "The ‘90s Beanie Baby craze led to people treating them as serious investments.",
        "The movie Toy Story 2 was almost deleted from Pixar’s servers by accident.",
        "Rihanna's song 'Umbrella' was originally written for Britney Spears, but she turned it down.",
        "The longest-running TV show in the world is 'The Simpsons'.",
        "Before playing James Bond, Sean Connery was a bodybuilder.",
        "The creators of Stranger Things originally wanted to call it 'Montauk'.",
        "The McDonald’s Big Mac was originally called 'The Aristocrat'.",
        "Walt Disney was afraid of mice, despite creating Mickey Mouse.",
        "Before becoming a rapper, Ice Cube studied architectural drafting.",
        "The famous 'E.T. phone home' line from E.T. was originally written as 'E.T. home phone'.",
        "Taylor Swift wrote her first song at age 12, called 'Lucky You'.",
        "The Nintendo company was founded in 1889 as a playing card company.",
        "The longest-ever concert lasted 453 hours and took place in Canada.",
        "The famous 'I am your father' line from Star Wars was a closely guarded secret during filming.",
        "Kanye West’s first job was working at The Gap.",
        "In the original script for Pretty Woman, it was supposed to have a much darker ending.",
        "Oprah Winfrey’s real name is Orpah, but people kept mispronouncing it."
    ]

    rand = random.randint(0, 100)
    if option == "4":
        option = str(random.randint(1, 3))
    match option:
        case "1":
            return science_facts[rand % len(science_facts)]
        case "2":
            return history_facts[rand % len(history_facts)]
        case "3":
            return pop_culture_facts[rand % len(pop_culture_facts)]
        case _:
            return "Fact: An error has occurred."

def main():
    # Create a ZMQ context object and use it to bind a socket.
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2026")

    # Listen for a request from client.
    while True:
        message = socket.recv()
        message = message.decode()

        # Determine appropriate action for request
        if len(message) > 0:
            print(f"Received request from the client: {message}")
            response = random_fact(message)
            socket.send_string(response)
            print(f"Sending response to the client: {response}")

if __name__ == '__main__':
    main()