class toDoList:
    # Application
    def __init__(self) -> list:
        self.noteList = []

    # Main functionalities
    def listAddNote(self, note):
        self.noteList.append(note)

        print(self.noteList)

    def listEditNote(self, noteIndex):
        editedNote = input(f"Edit the note -> {(self.noteList[noteIndex])} \n")
        self.noteList[noteIndex] = editedNote

    def listDeleteNote(self, noteIndex):
        self.noteList.__delitem__(noteIndex)

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
                self.listAddNote(newNote)

            elif user_input == "edit":
                try:
                    noteNumber = int(input("Which note do you want to edit?: ")) - 1
                    self.listEditNote(noteNumber)
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid note number.")

            elif user_input == "delete":
                try:
                    noteNumber = int(input("Which note do you want to delete?: ")) - 1
                    self.listDeleteNote(noteNumber)
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid note number.")

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
