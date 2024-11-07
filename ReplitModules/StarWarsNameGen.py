print("Star Wars Name Generetor".upper())

names = input(
    "Enter your first name, last name, Mum's maiden name and the city you were born in:\n"
)

firstName, lastName, maidenName, birthCity = names.split()

print(f"{firstName=}, {lastName=}, {maidenName=}, {birthCity=}")

print(
    f"Your Star Wars name is: {firstName[0:3]}{lastName[0:2].lower()} {maidenName[0:3]}{birthCity[-3:].lower()}"
)
