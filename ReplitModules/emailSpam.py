"""
1. Add email
2. Remove email
3. View emails
4. Spam first 10 emails
"""

from time import sleep
from os import system


class emailSpammer:
    # Application
    def __init__(self) -> None:
        self.emailList = []

    # Main functionalities
    def addEmail(self, note):
        self.emailList.append(note)

        print(self.emailList)

    def deleteEmail(self, noteIndex):
        del self.emailList[noteIndex]

    def viewEmails(self):
        print("Your Notes:")
        for index, note in enumerate(self.emailList):
            print(f"{index + 1}. {note}")

    def spamEmail(self):
        for email in self.emailList:
            print(
                f""" Dear {email}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.
Love and hugs,
Ian Spammington III
                  """
            )

            sleep(5)
            system("cls")

    def run(self):
        while True:
            print(
                """\n\033[32mEmail Spammer 3000:\33[0m
Do you want to add to, delete, view your email list or spam emails? Type exit to exit the application\n"""
            )

            user_input = input("").lower()

            # User input verification
            if user_input == "add":
                newEmail = input("Enter the email: ")
                self.addEmail(newEmail)

            elif user_input == "delete":
                try:
                    noteNumber = (
                        int(
                            input(
                                "Which email do you want to delete? Enter the number of the email: "
                            )
                        )
                        - 1
                    )
                    self.deleteEmail(noteNumber)
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid email number.")

            elif user_input == "spam":
                self.spamEmail()

            elif user_input == "view":
                self.viewEmails()

                input("\n. . . Do you want to return to home page? Press any key ")

            elif user_input == "exit":
                print("Exiting application")
                break

            else:
                print("Incorrect input")
                input("Enter to restart application . . .")


if __name__ == "__main__":
    app = emailSpammer()
    app.run()
