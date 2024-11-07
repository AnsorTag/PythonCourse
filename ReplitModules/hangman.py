# Once the word has been picked, the following things need to happen:

# Prompt the user to type in a letter.
# Check if the letter is in the word.
# If it does, output the word with all blanks apart from the letter(s) they've already guessed.
# Keep a running list of the letters they've used.
# Count how many times they've picked a letter that isn't in the word - more than 6 and they lose.
# Output a 'win' message if they reveal all the letters.

"""
letter = input("Enter a letter")

if letter in wordQuiz:
    action
"""

from random import choice


class Hangman:
    def __init__(self) -> None:
        self.wordsQuiz = ["napoleon", "oscar", "olivier", "lincoln", "titus"]
        self.guessedLetters = []
        self.lifeScore = 6

    def draw_hangman(self):
        match self.lifeScore:
            case 6:
                print("       O\n      /|\\\n      / \\")
            case 5:
                print("       |\n       O\n      /|\\\n      / \\")
            case 4:
                print("    ____|\n       O\n      /|\\\n      / \\")
            case 3:
                print("   ____\n  |    |\n       O\n      /|\\\n      / \\")
            case 2:
                print("   ____\n  |    |\n  |    O\n      /|\\\n      / \\")
            case 1:
                print("   ____\n  |    |\n  |    O\n  |   /|\\\n  |   / \\")
            case 0:
                print("   ____\n  |    |\n  |    O\n  |   /|\\\n  |   / \\")

    def run(self):
        curWord = choice(self.wordsQuiz)

        print("\nGuess the word. Tap Enter to continue . . .")
        print(f"{len(curWord) * '_'}")

        while self.lifeScore > 0:
            userAnswer = input("\nEnter a letter: ").lower()

            # Validate input: single letter and alphabetical
            if len(userAnswer) != 1 or not userAnswer.isalpha():
                print("Please enter a single alphabetical letter.")
                continue

            # Check for duplicate guesses
            if userAnswer in self.guessedLetters:
                print("You've already guessed that letter. Try again.")
                continue

            self.guessedLetters.append(userAnswer)

            if userAnswer in curWord:
                print("Correct!")
            else:
                self.lifeScore -= 1
                print(f"Incorrect! You have {self.lifeScore} tries left")

            currentDisplay = "".join(
                [letter if letter in self.guessedLetters else "_" for letter in curWord]
            )

            print("Current word: ", currentDisplay.capitalize())
            self.draw_hangman()  # Call the method to draw the hangman

            if "_" not in currentDisplay:
                print("Congratulations, you've guessed the word!")
                break

        if self.lifeScore == 0:
            print("You've run out of tries! The word was: ", curWord.capitalize())


if __name__ == "__main__":
    app = Hangman()
    app.run()

"""Not to push, but I forgot to tell you about Armins BD
we are gathering money to give him in an hour at the birthday bash.

brother I'm broke
"""
