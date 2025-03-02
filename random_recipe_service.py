# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Random Quote Service
# Description:  Uses ZeroMQ to serve random inspirational quotes to client.

import zmq
import random


def random_quote(option: str = "4") -> str:
    """Returns a random quote from 1 of 3 categories or a random category as determined by the option parameter."""
    artist_quotes = [
        # Artists
        "Every artist was first an amateur. — Ralph Waldo Emerson",
        "Art enables us to find ourselves and lose ourselves at the same time. — Thomas Merton",
        "Creativity takes courage. — Henri Matisse",
        "Learn the rules like a pro, so you can break them like an artist. — Pablo Picasso",
        "Great things are done by a series of small things brought together. — Vincent Van Gogh",
        "Art is not what you see, but what you make others see. — Edgar Degas",
        "Inspiration exists, but it has to find you working. — Pablo Picasso",
        "The role of the artist is to ask questions, not answer them. — Anton Chekhov",
        "An artist is not paid for his labor but for his vision. — James Whistler",
        "Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep. — Scott Adams",

        # Musicians
        "Without deviation from the norm, progress is not possible. — Frank Zappa",
        "Music can change the world because it can change people. — Bono",
        "One good thing about music, when it hits you, you feel no pain. — Bob Marley",
        "Don’t be afraid to be different, be afraid of being the same as everyone else. — Lady Gaga",
        "The beautiful thing about learning is nobody can take it away from you. — B.B. King",
        "You have to take the good with the bad, smile with the sad, love what you got, and remember what you had. — Beyoncé",
        "Success is falling nine times and getting up ten. — Jon Bon Jovi",
        "It's never too late to be what you might have been. — George Eliot",
        "It’s easy to play any musical instrument: all you have to do is touch the right key at the right time and the instrument will play itself. — Johann Sebastian Bach",
        "I’m just a musical prostitute, my dear. — Freddie Mercury",

        # Actors
        "The greatest thing you’ll ever learn is just to love and be loved in return. — Nat King Cole",
        "All the world's a stage, and all the men and women merely players. — William Shakespeare",
        "Do not let anyone ever make you feel like you don't deserve what you want. — Heath Ledger",
        "Why fit in when you were born to stand out? — Dr. Seuss",
        "Be so good they can’t ignore you. — Steve Martin",
        "Acting is not about being someone different. It’s finding the similarity in what is apparently different, then finding myself in there. — Meryl Streep",
        "Perseverance is failing 19 times and succeeding the 20th. — Julie Andrews",
        "If you obey all the rules, you miss all the fun. — Katharine Hepburn",
        "If you're the smartest person in the room, you're in the wrong room. — Michael Caine",
        "The most important thing is to enjoy your life—to be happy—it's all that matters. — Audrey Hepburn",

        # Writers
        "You can’t use up creativity. The more you use, the more you have. — Maya Angelou",
        "Do what you feel in your heart to be right—for you’ll be criticized anyway. — Eleanor Roosevelt",
        "Not all those who wander are lost. — J.R.R. Tolkien",
        "We are all broken, that’s how the light gets in. — Ernest Hemingway",
        "There is no greater agony than bearing an untold story inside you. — Maya Angelou",
        "The scariest moment is always just before you start. — Stephen King",
        "Start where you are. Use what you have. Do what you can. — Arthur Ashe",
        "It is our choices, Harry, that show what we truly are, far more than our abilities. — J.K. Rowling",
        "A writer is someone for whom writing is more difficult than it is for other people. — Thomas Mann",
        "Fairy tales are more than true—not because they tell us that dragons exist, but because they tell us that dragons can be beaten. — Neil Gaiman"
    ]
    historic_figure_quotes = [
        # Historical Figures
        "The only thing we have to fear is fear itself. — Franklin D. Roosevelt",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt",
        "It always seems impossible until it’s done. — Nelson Mandela",
        "Well done is better than well said. — Benjamin Franklin",
        "Happiness depends upon ourselves. — Aristotle",
        "We are what we repeatedly do. Excellence, then, is not an act, but a habit. — Aristotle",
        "Diligence is the mother of good luck. — Benjamin Franklin",
        "The weak can never forgive. Forgiveness is the attribute of the strong. — Mahatma Gandhi",
        "You must be the change you wish to see in the world. — Mahatma Gandhi",
        "An eye for an eye will only make the whole world blind. — Mahatma Gandhi",

        # World Leaders
        "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
        "To improve is to change; to be perfect is to change often. — Winston Churchill",
        "Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen. — Winston Churchill",
        "Injustice anywhere is a threat to justice everywhere. — Martin Luther King Jr.",
        "Faith is taking the first step even when you don’t see the whole staircase. — Martin Luther King Jr.",
        "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that. — Martin Luther King Jr.",
        "Give me six hours to chop down a tree and I will spend the first four sharpening the axe. — Abraham Lincoln",
        "Whatever you are, be a good one. — Abraham Lincoln",
        "The best way to predict your future is to create it. — Abraham Lincoln",
        "When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one that has opened for us. — Alexander Graham Bell",

        # Visionaries & Philosophers
        "An unexamined life is not worth living. — Socrates",
        "The mind is everything. What you think you become. — Buddha",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. — Buddha",
        "Knowing yourself is the beginning of all wisdom. — Aristotle",
        "It is not length of life, but depth of life. — Ralph Waldo Emerson",
        "The only true wisdom is in knowing you know nothing. — Socrates",
        "Do what is right, not what is easy nor what is popular. — Roy T. Bennett",
        "Do not go where the path may lead, go instead where there is no path and leave a trail. — Ralph Waldo Emerson",
        "If opportunity doesn’t knock, build a door. — Milton Berle",
        "Believe you can and you’re halfway there. — Theodore Roosevelt",

        # Military Leaders & Revolutionaries
        "Opportunities multiply as they are seized. — Sun Tzu",
        "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win. — Sun Tzu",
        "It is amazing what you can accomplish if you do not care who gets the credit. — Harry S. Truman",
        "Never interrupt your enemy when he is making a mistake. — Napoleon Bonaparte",
        "A leader is a dealer in hope. — Napoleon Bonaparte",
        "The only way to do great work is to love what you do. — Steve Jobs",
        "I have not failed. I've just found 10,000 ways that won’t work. — Thomas Edison",
        "Do what you feel in your heart to be right—for you’ll be criticized anyway. — Eleanor Roosevelt",
        "Nothing in life is to be feared, it is only to be understood. — Marie Curie",
        "Set your course by the stars, not by the lights of every passing ship. - Omar Bradley"
        "To handle yourself, use your head; to handle others, use your heart. — Eleanor Roosevelt"
    ]
    innovator_quotes = [
        # Scientists
        "Science and everyday life cannot and should not be separated. — Rosalind Franklin",
        "We cannot solve our problems with the same thinking we used when we created them. — Albert Einstein",
        "A person who never made a mistake never tried anything new. — Albert Einstein",
        "The important thing is not to stop questioning. Curiosity has its own reason for existing. — Albert Einstein",
        "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change. — Charles Darwin",
        "Somewhere, something incredible is waiting to be known. — Carl Sagan",
        "The good thing about science is that it’s true whether or not you believe in it. — Neil deGrasse Tyson",
        "The important thing in science is not so much to obtain new facts as to discover new ways of thinking about them. — William Lawrence Bragg",
        "Everything is theoretically impossible, until it is done. — Robert A. Heinlein",
        "Life would be tragic if it weren’t funny. — Stephen Hawking",

        # Engineers
        "Engineers like to solve problems. If there are no problems handily available, they will create their own. — Scott Adams",
        "The scientist discovers a new type of material or energy and the engineer discovers a new use for it. — Gordon Lindsay Glegg",
        "Scientists investigate that which already is; engineers create that which has never been. — Theodore von Kármán",
        "The ideal engineer is a composite … He is not a scientist, he is not a mathematician, he is not a sociologist or a writer; but he may use the knowledge and techniques of any or all of these disciplines in solving engineering problems. — Nathan W. Dougherty",
        "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. — Antoine de Saint-Exupéry",
        "Scientists dream about doing great things. Engineers do them. — James A. Michener",
        "The human foot is a masterpiece of engineering and a work of art. — Leonardo da Vinci",

        # Business Leaders
        "The way to get started is to quit talking and begin doing. — Walt Disney",
        "Your most unhappy customers are your greatest source of learning. — Bill Gates",
        "If you really look closely, most overnight successes took a long time. — Steve Jobs",
        "Innovation distinguishes between a leader and a follower. — Steve Jobs",
        "The secret of change is to focus all your energy not on fighting the old, but on building the new. — Socrates",
        "Risk more than others think is safe. Dream more than others think is practical. — Howard Schultz",
        "Don’t be afraid to give up the good to go for the great. — John D. Rockefeller",
        "Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
        "I find that the harder I work, the more luck I seem to have. — Thomas Jefferson",
        "Do what you love and success will follow. Passion is the fuel behind a successful career. — Meg Whitman",

        # Innovators & Entrepreneurs
        "Opportunities don’t happen. You create them. — Chris Grosser",
        "Logic will get you from A to B. Imagination will take you everywhere. — Albert Einstein",
        "As we look ahead into the next century, leaders will be those who empower others. — Bill Gates",
        "Don’t worry about failure; you only have to be right once. — Drew Houston",
        "It’s fine to celebrate success, but it is more important to heed the lessons of failure. — Bill Gates",
        "The biggest risk is not taking any risk. — Mark Zuckerberg",
        "Quality means doing it right when no one is looking. — Henry Ford",
        "Chase the vision, not the money; the money will end up following you. — Tony Hsieh",
        "Success is not how high you have climbed, but how you make a positive difference to the world. — Roy T. Bennett"
    ]
    # Randomly pick one of the options for the Suprise Me choice
    rand = random.randint(0, 100)
    if option == "4":
        option = str(random.randint(1, 3))

    # Output the quote from the appropriate category.
    match option:
        case "1":
            return artist_quotes[rand % len(artist_quotes)]
        case "2":
            return historic_figure_quotes[rand % len(historic_figure_quotes)]
        case "3":
            return innovator_quotes[rand % len(innovator_quotes)]
        case _:
            return "Doh. - Homer Simpson"

def main():
    # Create a ZMQ context object and use it to bind a socket.
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2027")

    while True:
        message = socket.recv()
        message = message.decode()

        # Determine appropriate action for request
        if len(message) > 0:
            print(f"Received request from the client: {message}")
            response = random_quote(message)
            socket.send_string(response)
            print(f"Sending response to the client: {response}")

if __name__ == '__main__':
    main()