from random import randint

print("⚔ CHARTACTER BUILDER ⚔")
print()


def diceGen():
    # HP Stat Roll
    dice1hp = randint(1, 7)
    dice2hp = randint(1, 13)

    statRollHP = (dice1hp * dice2hp) / 2 + 10

    # Str Stat Roll
    dice1Str = randint(1, 7)
    dice2Str = randint(1, 9)

    statRollStr = (dice1Str * dice2Str) / 2 + 12

    return statRollHP, statRollStr


while True:
    name = input("Name your Legend: ")
    heroRace = input("Character Race (Human, Elf, Orc, Titan): ")

    hp, str = diceGen()

    print(f"{name}")
    print(f"Race: {heroRace}")
    print(f"HP: \033[31m{hp}\033[0m")
    print(f"Str: \033[36m{str}\033[0m")

    print()

    print("May your name go down in Legends ... ")

    usr_input = input("Again? (yes/no): ")

    if usr_input == "yes":
        continue
    else:
        exit()
