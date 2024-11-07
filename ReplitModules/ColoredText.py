def inputText():
    colorText1 = input("Enter your first colored sentence: ")
    colorText2 = input("Enter your second colored sentence: ")
    colorText3 = input("Enter your third colored sentence: ")

    def colorText(colorTXT1, colorTXT2, colorTXT3):
        colorTXT1 = f"\033[32m{colorTXT1}\033[0m"  # Green
        colorTXT2 = f"\033[31m{colorTXT2}\033[0m"  # Red
        colorTXT3 = f"\033[35m{colorTXT3}\033[0m"  # Magenta

        finalText = (
            f"Super Subroutine\nWith my {colorTXT1} I can just call red('and') {colorTXT2} "
            f"that word will appear in the color I set it to.\nWith no {colorTXT3}\nEpic"
        )

        print(finalText)

    colorText(colorText1, colorText2, colorText3)


inputText()
