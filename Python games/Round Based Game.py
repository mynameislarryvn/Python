import random

game = True
game_run: bool = True
game_end = []


def BOTATK():
    return random.randint(bot["ATK_MIN"], bot["ATK_MAX"])


def win(name):
    print(f'\n{name} has won the game\n')


while game_run:
    game = True

    GameRound: int = 0

    player = {
        'name': "default",
        "ATK": 20,
        "HEAL": 24,
        "HEALTH": 150
    }

    bot = {
        'name': "bruh",
        "ATK_MIN": 24,
        "ATK_MAX": 28,
        "HEALTH": 100
    }

    print('can u please give me ur name: ')
    player['name'] = str(input())
    print((f'''
    player name: {player["name"]}
    Atk: {player["ATK"]}
    Heal: {player["HEAL"]}
    Health {player["HEALTH"]}'''))

    print('\nBruh ur did it, welcome to a shitty game\nPress any key to continue')
    input()
    while game:
        bruhWin: bool = False
        playerWin: bool = False
        GameRound = GameRound + 1
        print("-" * 27)
        print("\nplease select option")
        print("1. Attack")
        print("2. Heal")
        print("3. Run")
        print("4. Stats")
        print("5. Exit")
        Pchoise = int(input())
        if Pchoise == 1:
            print("\nBONK")
            bot["HEALTH"] = bot["HEALTH"] - player["ATK"]
            print("You have dealt " + str(player["ATK"]))

            if bot["HEALTH"] <= 0:
                playerWin = True

            else:
                player["HEALTH"] = player["HEALTH"] - BOTATK()
                print(f'bruh has dealt' + str(BOTATK))

                if player["HEALTH"] <= 0:
                    bruhWin = True

        elif Pchoise == 2:
            print(f"\nI healed for{player['HEALTH']} \n")
            player["HEALTH"] = player["HEALTH"] + player["HEAL"]
            player["HEALTH"] = player["HEALTH"] - BOTATK()

            if player["HEALTH"] <= 0:
                bruhWin = True

        elif Pchoise == 3:
            print('\nU fled away')
            game = False
            bruhWin = True
            #game = False

        elif Pchoise == 4:
            for stat in game_end:
                print(stat)
        elif Pchoise == 5:
            game_run = False
            game = False
        else:
            print("\nInvalid input")

        if bruhWin == False and playerWin == False:
            print("\nPlayer health: " + str(player["HEALTH"]))
            print("Bruh health: " + str(bot["HEALTH"]))

        elif playerWin:
            win(player['name'])
            end = {
                'Name': player['name'],
                'Health': player["HEALTH"],
                'Round': GameRound
            }
            game_end.append(end)
            game = False

        elif bruhWin:
            win(bot['name'])
            end = {
                'Name': bot['name'],
                'Health': bot["HEALTH"],
                'Round': GameRound
            }
            game_end.append(end)
            game = False
