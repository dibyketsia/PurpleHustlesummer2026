# ============================================================
# LAB 7 - MY OWN ORDERING APP
# Week 7 - Hack the Hood
# ============================================================
# Name: __________________
#
# My store sells: Sneakers
# ============================================================

# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard
    def set_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative!")
        else:
            self.price = new_price

    # TICKET 5: Each item's own action
    def deliver(self):
        print(f"Your {self.name} is ready to shop!")


# TICKET 4: A second kind of item

class Sneaker(Item):
    def Cashier(self):
        print(f"What shoe size {self.name}?")


# TICKET 2: Make your real items

item1 = Item("Red Slides", 20)
item2 = Item("Brown Boots", 60)
item3 = Item("Green Sneakers", 95)

print(item1.name)

# Uncomment to test the price guard
# item1.set_price(-5)


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to cart.")

    # TICKET 9: Checkout
    def checkout(self):
        total = 0

        print("\n----- Checkout -----")

        for item in self.items:
            item.deliver()
            total += item.price

        print("--------------------")
        print(f"Total: ${total}")


# TICKET 7: My shoes and my cart

Shoes = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()

# TICKET 8: Let customers shop

print("\nWelcome to Ketsia's Sneaker Store!")

while True:
    print("\nShoes")
    print("1. Green Sneakers - $95")
    print("2. Red Slides - $20")
    print("3. Brown Boots - $60")

    choice = input("Choose an item (or type 'done'): ")

    if choice.lower() == "done":
        break

    if choice in Shoes:
        cart.add_item(Shoes[choice])
    else:
        print("Invalid choice.")

# TICKET 10: Test the whole app

cart.checkout()