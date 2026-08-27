from enemies import Enemy


class GameLevel:
    def __init__(self, level_name, opponent):
        self.level_name = level_name
        self.opponent = opponent

    def show_level(self):
        print(f"\n===== {self.level_name.upper()} =====")
        print(f"Opponent: {self.opponent.name}")
        print(f"Opponent Points: {self.opponent.points}")
        print(f"Opponent Power: {self.opponent.power}")


# Four opponents
opponent1 = Enemy("Ketsia", 100, 10)
opponent2 = Enemy("Tony Stank", 100, 15)
opponent3 = Enemy("Loki", 100, 20)
opponent4 = Enemy("Nebula", 100, 25)


# Four levels
level1 = GameLevel("Easy", opponent1)
level2 = GameLevel("Confident", opponent2)
level3 = GameLevel("Face to Face", opponent3)
level4 = GameLevel("Impossible", opponent4)


levels = [
    level1,
    level2,
    level3,
    level4
]