import random

class Enemy:
    def __init__(self, name, points, power):
        self.name = name
        self.points = points
        self.power = power

    def set_points(self, new_points):
        if new_points < 0:
            self.points = 0
        elif new_points > 100:
            self.points = 100
        else:
            self.points = new_points

    def attack(self, player):
        points = random.randint(5, self.power)
        player.set_points(player.points - points)
        print(f"{self.name} scored {points} points!")