class WordCounter:
    def __init__(self) -> None:
        self.filePath = ""

    def openNreadFile(self):
        filePath = input("enter the file path: ")

        try:
            with open(filePath, "r") as file:
                allText = "".join(file.readlines())
                finalWordCount = len(allText.split())
                print(f"Word count = {finalWordCount}")
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")

    def run(self):
        while True:
            choice = input("Would you like to read a file? (yes/no) ").lower()

            if choice == "yes":
                self.openNreadFile()
            else:
                break


if __name__ == "__main__":
    application = WordCounter()
    application.run()
