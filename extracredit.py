import random

welcome_messages = [
    "Welcome to Ketsia's Fashion Store!",
    "Thank you for shopping with us!",
    "Great to see you! Let's find your next piece!"
]

print(random.choice(welcome_messages))


item2 = Item("Brown Bag", 60)
item2.set_price(40)
print(f"{item2.name} is on sale for ${item2.price}!")

print("\nHere is what we have:")

for number, item in Shoes.items():
    print(number + ": " + item.name + " - $" + str(item.price))

if choice.lower() == "done":
    break

if choice in Bags:
    cart.add_item(Bags[choice])
else:
    print("Invalid choice.")

if choice.lower() == "done":
    break
elif choice in Bags:
    cart.add_item(Bags[choice])
else:
    print("Sorry, this is out of stock")

print("\n----- Your Receipt -----")

for item in cart.items:
    print(item.name + " ..... $" + str(item.price))

print("\nYou bought " + str(len(cart.items)) + " item(s).")