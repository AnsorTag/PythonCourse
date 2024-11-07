from getpass import getpass as input


def addOne(player, counter):
    player += 1
    counter += 1


print("E P I C    🗿 📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")

print()

p1 = 0
p2 = 0

counter = 0

while True:

    Player1 = input("Player1 > ")
    Player2 = input("Player2 > ")

    if Player1 == "R" and Player2 == "R":
        print(
            "Player1's rock smashes Player2's rock, igniting sparkles, both cracking into dust. It's Draw!"
        )
        counter += 1

    elif Player1 == "R" and Player2 == "P":
        print(
            "Player2's paper wraps around Player1's rock, trapping it, making the rock impossible to move. Player2 wins!"
        )
        addOne(p2, counter)

    elif Player1 == "R" and Player2 == "S":
        print(
            "Player1's rock withstands sharp blades of Player2's scissors, making the scissors crubmle into metal shards. Player1 wins"
        )
        addOne(p1, counter)

    elif Player1 == "P" and Player2 == "R":
        print(
            "Player1's paper wraps around Player2's rock, trapping it, making the rock impossible to move. Player1 wins!"
        )
        addOne(p1, counter)

    elif Player1 == "P" and Player2 == "P":
        print(
            "Player1's paper flaps around Player2's paper, making the paper flying in the air. What a beatiful sight, however it's Draw!"
        )
        counter += 1

    elif Player1 == "P" and Player2 == "S":
        print(
            "Player2's scissors cuts Player1's paper into tiny pieces, making the paper fall to the ground. Player2 wins!"
        )
        addOne(p2, counter)

    elif Player1 == "S" and Player2 == "R":
        print(
            "Player2's rock withstands sharp blades of Player1's scissors, making the scissors crubmle into metal shards. Player2 wins!"
        )
        addOne(p2, counter)

    elif Player1 == "S" and Player2 == "P":
        print(
            "Player1's scissors cuts Player2's paper into tiny pieces, making the paper fall to the ground. Player1 wins!"
        )
        addOne(p1, counter)

    elif Player1 == "S" and Player2 == "S":
        print(
            "Player1's and Player2's scissors clash, in a beatiful dance of blades. In the end blades collide with a brihgt spark, breaking into small pieces. It's Draw!"
        )
        counter += 1

    if counter == 3 and (p1 == 3 or p2 == 3):
        break
    elif counter == 3 and (not p1 == 3 or not p2 == 3):
        p1 = 0
        p2 = 0
        counter = 0

        print("Resetting the game")
        continue

if p1 > p2:
    print("Player1 wins with", p1, "points!")
elif p1 < p2:
    print("Player2 wins with", p2, "points!")
elif p1 == p2:
    print("It's a draw!")
else:
    print("Something went wrong!")
