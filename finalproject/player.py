import random

class Player:
    def __init__(self, name, points, power, energy):
        self.name = name
        self.points = points
        self.power = power
        self.energy = energy

    def set_points(self, new_points):
        # Keep points between 0 and 100
        if new_points < 0:
            self.points = 0
        elif new_points > 100:
            self.points = 100
        else:
            self.points = new_points

    def basic_move(self, opponent):
        damage = random.randint(5, self.power)
        opponent.set_points(opponent.points - damage)
        print(f"{self.name} scored {damage} points!")

    def special_move(self, opponent):
        if self.energy < 20:
            print("Not enough energy!")
            return

        damage = random.randint(15, self.power + 10)
        opponent.set_points(opponent.points - damage)
        self.energy -= 20

        print(f"{self.name} used an EPIC BOOSTER for {damage} points!")