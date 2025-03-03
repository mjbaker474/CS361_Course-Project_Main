# Name:  Matthew Baker
# OSU Email:  bakerma2@oregonstate.edu
# Course: CS361 - Software Engineering 1
# Assignment:  Course Project
#
# File: Random Recipe Service
# Description:  Uses ZeroMQ to serve random recipe suggestions to client.

import zmq
import random


def random_recipe(option: str = "4") -> str:
    """Returns a random recipe from 1 of 3 categories or a random category as determined by the option parameter."""
    appetizers = [
        "Bruschetta",
        "Stuffed Mushrooms",
        "Deviled Eggs",
        "Spinach and Artichoke Dip",
        "Caprese Skewers",
        "Garlic Parmesan Wings",
        "Buffalo Cauliflower Bites",
        "Mini Crab Cakes",
        "Loaded Potato Skins",
        "Bacon-Wrapped Jalapeño Poppers",
        "Shrimp Cocktail",
        "Cheese and Charcuterie Board",
        "Hummus with Pita Chips",
        "Coconut Shrimp",
        "Mini Meatballs",
        "Queso Dip",
        "Cucumber Bites with Herbed Cream Cheese",
        "Prosciutto-Wrapped Melon",
        "Baked Brie with Honey and Nuts",
        "Sweet and Spicy Nuts",
        "Teriyaki Chicken Skewers",
        "Samosas",
        "Empanadas",
        "Mini Quiches",
        "French Onion Soup Bites",
        "Tzatziki with Pita Bread",
        "Sushi Rolls",
        "Antipasto Skewers",
        "Fried Calamari",
        "Crispy Zucchini Fries",
        "Cheesy Garlic Bread",
        "Mushroom Crostini",
        "Spinach and Feta Phyllo Triangles",
        "Korean BBQ Beef Sliders",
        "Crispy Brussels Sprouts with Balsamic Glaze",
        "Bacon-Wrapped Dates",
        "Gyoza (Japanese Dumplings)",
        "BBQ Chicken Flatbread",
        "Salmon Tartare",
        "Chili Lime Roasted Chickpeas"
    ]

    entrees = [
        "Grilled Salmon with Lemon Butter",
        "Chicken Alfredo Pasta",
        "Beef Stroganoff",
        "Vegetable Stir-Fry with Tofu",
        "Lemon Garlic Shrimp Scampi",
        "Stuffed Bell Peppers",
        "Eggplant Parmesan",
        "Honey Garlic Chicken",
        "Teriyaki Glazed Salmon",
        "BBQ Ribs",
        "Shepherd's Pie",
        "Spaghetti Carbonara",
        "Baked Ziti",
        "Chicken Marsala",
        "Lamb Chops with Rosemary",
        "Vegetable Lasagna",
        "Jambalaya",
        "Shrimp and Grits",
        "Pork Chops with Apple Chutney",
        "Thai Green Curry",
        "Beef Tacos with Fresh Salsa",
        "Chicken Cordon Bleu",
        "Miso-Glazed Cod",
        "Pulled Pork Sandwiches",
        "Lobster Mac and Cheese",
        "Chicken Tikka Masala",
        "Gnocchi with Pesto Cream Sauce",
        "Stuffed Chicken Breast",
        "Grilled Portobello Mushrooms with Balsamic Glaze",
        "Paella",
        "Shakshuka",
        "Osso Buco",
        "Korean Bulgogi Beef",
        "Seafood Cioppino",
        "Butter Chicken",
        "Ratatouille",
        "Turkey Meatloaf",
        "Coconut Curry Chickpeas",
        "Duck à l'Orange",
        "General Tso's Chicken"
    ]
    desserts = [
        "Chocolate Lava Cake",
        "New York Cheesecake",
        "Tiramisu",
        "Crème Brûlée",
        "Apple Pie",
        "Molten Peanut Butter Brownies",
        "Strawberry Shortcake",
        "Key Lime Pie",
        "Panna Cotta",
        "Churros with Chocolate Sauce",
        "Baklava",
        "Lemon Bars",
        "Carrot Cake with Cream Cheese Frosting",
        "Red Velvet Cake",
        "Banoffee Pie",
        "Black Forest Cake",
        "Coconut Macaroons",
        "Pumpkin Pie",
        "Chocolate Mousse",
        "Rice Pudding",
        "Chocolate Chip Cookies",
        "Éclairs",
        "Vanilla Bean Ice Cream",
        "Raspberry Sorbet",
        "Flourless Chocolate Cake",
        "Peach Cobbler",
        "Macarons",
        "Pavlova",
        "Sticky Toffee Pudding",
        "Mango Sticky Rice",
        "Tres Leches Cake",
        "Cannoli",
        "Brown Butter Blondies",
        "Oreo Cheesecake",
        "Profiteroles",
        "Fruit Tart",
        "Almond Biscotti",
        "S'mores Bars",
        "Honey Baklava Cheesecake",
        "Chocolate-Covered Strawberries"
    ]
    # Randomly pick one of the options for the Suprise Me choice
    rand = random.randint(0, 100)
    if option == "4":
        option = str(random.randint(1, 3))

    # Output the quote from the appropriate category.
    match option:
        case "1":
            return appetizers[rand % len(appetizers)]
        case "2":
            return entrees[rand % len(entrees)]
        case "3":
            return desserts[rand % len(desserts)]
        case _:
            return "Error encountered."

def main():
    # Create a ZMQ context object and use it to bind a socket.
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2028")

    while True:
        message = socket.recv()
        message = message.decode()

        # Determine appropriate action for request
        if len(message) > 0:
            print(f"Received request from the client: {message}")
            response = random_recipe(message)
            socket.send_string(response)
            print(f"Sending response to the client: {response}")

if __name__ == '__main__':
    main()