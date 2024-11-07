text = input("What sentence do you want rainbowize?\n")

currentColor = "\033[0m"

print("\n\n")

for letter in text:
    if letter.lower() == "r":
        currentColor = "\033[31m"
    elif letter.lower() == "g":
        currentColor = "\033[32m"
    elif letter.lower() == "y":
        currentColor = "\033[33m"
    elif letter.lower() == "b":
        currentColor = "\033[34m"
    elif letter.lower() == "m":
        currentColor = "\033[35m"
    elif letter.lower() == "c":
        currentColor = "\033[36m"
    elif letter.lower() == "w":
        currentColor = "\033[37m"
    elif letter.lower() == " ":
        currentColor = "\033[0m"

    print(f"{currentColor}{letter}", end="")

print("\033[0m", end="")
