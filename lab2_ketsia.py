# Snippet 1

x = 10
if x != 0:
    print(10 / x)
else:
    print("Cannot divide by zero")

# Snippet 2

numbers = [0, 1, 2, 3, 4]
for i in range(len(numbers)):
    print(numbers[i - 1])

# Snippet 3

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

# Snippet 4

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

# Snippet 5

for i in range(5):
    print(i)

# Snippet 6

name = "Ketsia"
if name == "Ava" or name == "Mia":
    print("Hello, friend!")
else:
    print("Hello, stranger!")

# Snippet 7

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

# Snippet 8

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Snippet 9

name = input("Alice")
if name == "Alice" or "Bob":
    print("Hello, Friend" + name)
else:
    print("Hello, stranger!")

# Snippet 10

divisor = 0
if divisor != 0:
    print(10,divisor)
else:
    print("Cannot divide by zero")