from random import randint

print("⚔ CHARTACTER STAT GENERATOR ⚔")
print()


def diceGen():
    dice1 = randint(1, 7)
    dice2 = randint(1, 9)

    statRoll = dice1 * dice2

    return statRoll


def statGen():
    HP = diceGen()
    MP = diceGen()
    SP = diceGen()

    return HP, MP, SP


while True:
    name = input("Name your Hero: ")
    heroClass = input("Pick a class: ")

    hp, mp, sp = statGen()

    print(f"{name} is a fierce {heroClass}")
    print(f"{name}'s HP is \033[31m{hp}\033[0m")
    print(f"{name}'s MP is \033[34m{mp}\033[0m")
    print(f"{name}'s SP is \033[32m{sp}\033[0m")

    print()

    continue
