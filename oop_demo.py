class Animal:
    def __init__(self, legs, fur, colors, lifespan, eyes, habitat, size)
        self.legs = legs
        self.fur = fur
        self.colors = colors
        self.lifespan = lifespan
        self.eyes = eyes
        self.habitat = habitat
        self.size = size

    def move(self):
        if self.legs >= 2:
            print("ZOOOOOOOM!")
        elif self.legs >=1:
            print("The animal is hooping along. Hop hop hop!")
        else:
            print("The animal did not move.")

dog = Animal(2, True, "brown", 15, 2, "house", "medium")

dog.move()