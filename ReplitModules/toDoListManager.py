"""Create your own to do list manager. (This can be super useful!)

Ask the user whether they want to view, add, or edit their to do list.
If they want to view it, print it out in a nice way (Hint: subroutine).
If they choose to add an item to the to do list, allow them to type in the item and then add it to the bottom of the list.
If they want to edit the to do list, ask them which item they completed, and remove it from the list.
Don't worry about duplicates!
The first item you put in the list should be the first item you remove.
Add a title, some color, alignment to the text, or emojis. Show off your skills!
Example:

To Do List Manager:
Do you want to view, add, or edit your to do list?
view
Record video for day 34"""

# Application
noteList = []


# Main functionalities
def listAddNote(note):
    noteList.append(note)

    print(noteList)


def listEditNote(noteIndex):
    editedNote = input(f"Edit the note -> {(noteList[noteIndex])} \n")
    noteList[noteIndex] = editedNote


def listDeleteNote(noteIndex):
    noteList.__delitem__(noteIndex)


def viewNotes():
    print("Your Notes:")
    for index, note in enumerate(noteList):
        print(f"{index + 1}. {note}")


while True:

    def application():
        print(
            """\n\033[32mTo Do List Manager:\33[0m
Do you want to add to, edit, delete a note or view your to do list?\n"""
        )

        user_input = input("")

        # User input verification
        if user_input.lower() == "add":
            newNote = input("Enter your note: ")
            listAddNote(newNote)

        elif user_input.lower() == "edit":
            try:
                noteNumber = int(input("Which note do you want to edit?: ")) - 1
                listEditNote(noteNumber)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid note number.")

        elif user_input.lower() == "delete":
            try:
                noteNumber = int(input("Which note do you want to delete?: ")) - 1
                listDeleteNote(noteNumber)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid note number.")

        elif user_input.lower() == "view":
            viewNotes()

            input("\n. . . Do you want to return to home page? Press any key ")

        else:
            print("Incorrect input")
            input("Enter to restart application . . .")

    application()
