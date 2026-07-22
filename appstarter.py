# ============================================================
# LAB 7 - MY OWN ORDERING APP
# Week 7 - Hack the Hood
# ============================================================

import random

# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Price guard
    def set_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative!")
        else:
            self.price = new_price

    # Deliver item
    def deliver(self):
        print(f"Your {self.name} is ready to shop!")

# Second class
class Sneaker(Item):
    def deliver(self):
        print(f"Enjoy your new {self.name}!")

# Make your items
item1 = Item("Red Slides", 20)
item2 = Item("Brown Bag", 60)
item3 = Sneaker("Green Sneakers", 95)

# Brown Bag goes on sale
item2.set_price(40)
print(f"{item2.name} is on sale for ${item2.price}!")

# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to cart.")

    def checkout(self):
        total = 0

        print("\n----- Checkout -----")

        for item in self.items:
            item.deliver()
            total += item.price

        print("--------------------")
        print(f"Total: ${total}")

# Store menu
Shoes = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()

# ============================================================
# EXTENSION TICKET 1 - Random Welcome
# ============================================================

welcome_messages = [
    "Welcome to Ketsia's Fashion Store!",
    "Thank you for shopping with us!",
    "Great to see you! Let's find your next piece!"
]

print(random.choice(welcome_messages))

# ============================================================
# EXTENSION TICKET 3 - Print Menu
# ============================================================

print("\nHere is what we have:")

for number, item in Shoes.items():
    print(number + ": " + item.name + " - $" + str(item.price))

# ============================================================
# EXTENSION TICKET 4 - Shopping Loop
# ============================================================

while True:
    choice = input("\nChoose an item (or type 'done'): ")

    if choice.lower() == "done":
        break
    elif choice in Shoes:
        cart.add_item(Shoes[choice])
    else:
        print("Sorry, that's not on the menu!")

# ============================================================
# EXTENSION TICKET 5 - Receipt
# ============================================================

print("\n----- Your Receipt -----")

for item in cart.items:
    print(item.name + " ..... $" + str(item.price))

# ============================================================
# EXTENSION TICKET 6 - Count Items
# ============================================================

print("\nYou bought " + str(len(cart.items)) + " item(s).")

# Checkout
cart.checkout()