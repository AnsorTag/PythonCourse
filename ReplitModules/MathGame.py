from random import randint

print("Math Game")

score = 0

for _ in range(10):
    x = randint(1, 100)
    y = randint(1, 100)

    answer = x * y

    userAnswer = int(input(f"{x} x {y} = "))

    if answer == userAnswer:
        print("Great Work buddy! 🥳")
        score += 1
    else:
        print(f"Nope! :( the answer was {answer}")

print("...")

print(f"You scored {score} out of 10")
