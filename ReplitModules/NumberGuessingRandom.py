from random import randint

print("Guess the number")
print()

theNumber = randint(1, 1000000)

counter = 0

while True:
    answer = int(input("What is your guess?: "))

    if answer > theNumber:
        print("Too high")
        print()
        counter += 1

    elif answer < theNumber:
        print("Too low")
        print()
        counter += 1

    else:
        print("Congrats, that's the correct answer")
        counter += 1

        break

print(f"It took you {counter} guesses to get it correct!")
