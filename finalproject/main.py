from enemies import Enemy
from gamelevel import GameLevel


def main():
    print("Welcome to Ketsia's Showdown!")

    # Create the four opponents
    opponent1 = Enemy("Ketsia", 100, 10)
    opponent2 = Enemy("Tony Stank", 100, 15)
    opponent3 = Enemy("Loki", 100, 20)
    opponent4 = Enemy("Nebula", 100, 25)

    # Create the four levels
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

    # Show all four levels
    for level in levels:
        level.show_level()


main()