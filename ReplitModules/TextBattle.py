from random import randint
import os


def main_game():

    # SETTING PLAYERS
    players = {}

    print("\n ⚔️ BATTLE TIME ⚔️")
    print()

    def diceGen():
        # HP Stat Roll
        dice1hp = randint(9, 16)
        dice2hp = randint(9, 21)

        statRollHP = (dice1hp * dice2hp) / 2 + 10

        # Str Stat Roll
        dice1Str = randint(1, 7)
        dice2Str = randint(1, 9)

        statRollStr = (dice1Str * dice2Str) / 2 + 12

        return statRollHP, statRollStr

    def characterCreation():
        for i in range(2):
            name = input("Name your Legend: ")
            heroRace = input("Character Race (Human, Elf, Orc, Titan): ")

            hp, strength = diceGen()

            players[name] = {"Race": heroRace, "HP": hp, "Str": strength}

            print(f"{name}")
            print(f"Race: {heroRace}")
            print(f"HP: \033[31m{hp}\033[0m🧡")
            print(f"Str: \033[36m{strength}\033[0m💪")
            print()

            if i == 0:
                print(f"Who is {name} fighting?")
            continue

    characterCreation()

    # PLAYER STAT COPIES
    player_list = list(players.items())

    player1_name, player1_stats = player_list[0]
    player2_name, player2_stats = player_list[1]

    # player1_race = player1_stats["Race"]
    # player2_race = player2_stats["Race"]

    player1_hp = player1_stats["HP"]
    player2_hp = player2_stats["HP"]

    player1_str = player1_stats["Str"]
    player2_str = player2_stats["Str"]

    # DUEL STATS
    def atkChance():
        dice1 = randint(1, 7)
        dice2 = randint(1, 7)
        return dice1 + dice2

    def calculate_damage(base_strength):
        damage = int(randint(int(base_strength * 0.5), int(base_strength * 1.5)))
        return damage

    startFight = input("Do you want to start the duel? (yes/no): ")

    # DUELING
    roundCount = 0
    os.system("cls")
    if startFight == "yes":
        while True:
            player1_atkChance = atkChance()
            player2_atkChance = atkChance()

            print("⚔️ BATTLE TIME ⚔️")
            print("\nThe Battle begins!")

            if player1_atkChance > player2_atkChance:
                damage = calculate_damage(player1_str)
                player2_hp -= damage

                print(
                    f"{player1_name} rolls: {player1_atkChance}; {player2_name} rolls: {player2_atkChance}"
                )

                print(
                    f"{player1_name} slashes {player2_name} leaving a deep wound (\033[31m-{damage}\033[0m HP)"
                )
            elif player1_atkChance < player2_atkChance:
                damage = calculate_damage(player2_str)
                player1_hp -= damage

                print(
                    f"{player1_name} rolls: {player1_atkChance}; {player2_name} rolls: {player2_atkChance}"
                )

                print(
                    f"{player2_name} casts a fireball burning {player1_name} (\033[31m-{damage}\033[0m HP)"
                )
            else:
                print(
                    f"{player1_name} rolls: {player1_atkChance}; {player2_name} rolls: {player2_atkChance}"
                )
                print(f"{player1_name} and {player2_name} clash swords, none relenting")

            print(f"\n{player1_name} HP: {player1_hp}")
            print(f"{player2_name} HP: {player2_hp}\n")

            # LOSER
            if player1_hp <= 0:
                print(f"{player1_name} was \033[34mslain!\033[0m")
                print(
                    f"{player2_name} \033[34mdefeated\033[0m {player1_name} in {roundCount} rounds!"
                )
                break
            elif player2_hp <= 0:
                print(f"{player2_name} was \033[34mslain!\033[0m")
                print(
                    f"{player1_name} \033[34mdefeated\033[0m {player2_name} in {roundCount} rounds!"
                )
                break

            roundCount += 1
            input("Press Enter to continue the battle...")
            os.system("cls")

    else:
        main_game()


main_game()
