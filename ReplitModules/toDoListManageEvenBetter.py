"""Create a menu where the user can view, add, or remove an item.
The user should be able to edit the text of an item on the list too. ✅
Don't allow the user to add duplicates.
Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)✅
Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)✅
"""


class toDoList:
    # Application
    def __init__(self) -> None:
        self.noteList = []

    # Main functionalities
    def addNote(self, note):

        if note in self.noteList:
            print("This note already exists.")
        else:
            self.noteList.append(note)
            print("Note added!\n")

        print(self.noteList)

    def editNote(self, noteIndex):
        editedNote = input(f"Edit the note -> {(self.noteList[noteIndex])} \n")
        self.noteList[noteIndex] = editedNote

    def deleteNote(self, noteIndex):
        self.noteList.__delitem__(noteIndex)

    def deleteAllNotes(self):
        self.noteList.clear()

    def viewNotes(self):
        print("Your Notes:")
        for index, note in enumerate(self.noteList):
            print(f"{index + 1}. {note}")

    def run(self):
        while True:
            print(
                """\n\033[32mTo Do List Manager:\33[0m
Do you want to add to, edit, delete a note or view your to do list? Type exit to exit the application\n"""
            )

            user_input = input("").lower()

            # User input verification
            if user_input == "add":
                newNote = input("Enter your note: ")
                self.addNote(newNote)

            elif user_input == "edit":
                try:
                    noteNumber = int(input("Which note do you want to edit?: ")) - 1
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid note number.")

            elif user_input == "delete":
                try:
                    noteNumber = int(input("Which note do you want to delete?: ")) - 1

                    reassurence = input(
                        "Do you really want to delete this note?: "
                    ).lower()

                    if reassurence == "yes":
                        self.deleteNote(noteNumber)
                    else:
                        continue

                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid note number.")

            elif user_input == "delete all":
                reassurence = input(
                    "Do you really want to delete all of the notes?: "
                ).lower()

                if reassurence == "yes":
                    self.deleteAllNotes()
                else:
                    continue

            elif user_input == "view":
                self.viewNotes()

                input("\n. . . Do you want to return to home page? Press any key ")

            elif user_input == "exit":
                print("Exiting application")
                break

            else:
                print("Incorrect input")
                input("Enter to restart application . . .")


if __name__ == "__main__":
    app = toDoList()
    app.run()
