import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2025")

activities = [
    "Going hiking",
    "Attending a concert",
    "Going dancing",
    "Working out",
    "Playing video games",
    "Reading a book",
    "Cooking a new recipe",
    "Going to a museum",
    "Watching a movie",
    "Going out to eat",
    "Swimming at the beach",
    "Going on a road trip",
    "Visiting an amusement park",
    "Camping in the mountains",
    "Taking a walk",
    "Practicing yoga",
    "Volunteering at a local charity",
    "Going for a bike ride",
    "Fishing at a lake",
    "Going to a cooking class",
    "Trying an escape room",
    "Playing board games with friends",
    "Going bowling",
    "Taking a dance class",
    "Exploring a new city",
    "Painting or drawing",
    "Going for a jog",
    "Attending a sports event",
    "Writing in a journal",
    "Gardening in the backyard",
    "Going stargazing",
    "Taking a scenic train ride",
    "Trying rock climbing",
    "Going to a comedy show",
    "Visiting a botanical garden",
    "Joining a trivia night",
    "Doing a puzzle",
    "Practicing meditation",
    "Going to a farmer’s market",
    "Trying out archery"
]


def main():
    while True:
        print("Listening for request")
        random_number = int(socket.recv().decode().strip())

        if random_number < 0 or random_number > 39:
            print("Invalid number")
            break
            
        return_string = activities[random_number]
        socket.send_string(return_string)
    context.term()


main()
