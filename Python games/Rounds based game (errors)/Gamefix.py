import random
game = True

def bruhATK():
    return random.randint(bruh["ATK_MIN"], bruh["ATK_MAX"])
def win(name):
    print(f"{name} has won the game")

while game == True:
    def bruhATK():
        return random.randint(bruh["ATK_MIN"], bruh["ATK_MAX"])


    def win(name):
        print(f"{name} has won the game")


    new = True
    player = {"name": "default", "ATK": 20, "HEAL": 24, "HEATH": 100}
    bruh = {"name": "Masu", "ATK_MIN": 12, "ATK_MAX": 22, "HEATH": 100}
    player["name"] = input()
    print("player stat: ATK: " + str(player["ATK"]) + " HEAL: " + str(player["HEAL"]) + " Heath: " + str(
    player["HEATH"]))
    playerWin = False
    bruhWin = False
    while new == True:

        print("-" * 27)
        print("\nplease select option")
        print("1. attack")
        print("2. heal")
        print("3. exit")

        Pchoise = input()

        if Pchoise == 1:
            print("\nBONK")
            bruh["HEATH"] = bruh["HEATH"] - player["ATK"]  # * random.randint (1,2)
            if bruh["HEATH"] <= 0:
                playerWin = True
            else:
                # bruhATK = random.randint(bruh["ATK_MIN"],bruh["ATK_MAX"])
                player["HEATH"] = player["HEATH"] - bruhATK()  # * random.randint (1,2)
                if player["HEATH"] <= 0:
                    bruhWin = True
            # print("player heath: " + str(player["HEATH"]))
            # print("bruh heath: " + str(bruh["HEATH"]))

        elif Pchoise == 2:
            print("\nI heal")
            # bruhATK = random.randint(bruh["ATK_MIN"], bruh["ATK_MAX"])
            player["HEATH"] = player["HEATH"] + player["HEAL"]
            player["HEATH"] = player["HEATH"] - bruhATK()  # * random.randint(1, 2)
            if player["HEATH"] <= 0:
                bruhWin = True
            # print("player heath: " + str(player["HEATH"]))
            # print("bruh heath: " + str(bruh["HEATH"]))
        if bruhWin == False and playerWin == False:
            print("player heath: " + str(player["HEATH"]))
            print("bruh heath: " + str(bruh["HEATH"]))
        elif playerWin:
            win(player["name"])
            game = False
        elif bruhWin:
            win(bruh["name"])
            game = False

        elif Pchoise == 3:
            print("u flee")
            game = False

        else:
            print("bruh cant even type")
