import random


def status():
    print(f'''
{bot['Name']} has {bot['Health']} HP left
{player['Name']} has {player['Health']} HP left
''')


new = True
player = {
    "Name": "",
    "Atk": 20,
    "Heal": 24,
    "Health": 100
}
bot = {
    'Name': "Larry",
    "Atk": 20,
    "Heal": 24,
    "Health": 100
}
if new:
    player["Name"] = input("Please input your name: ")
    print(f'''
    player name: {player["Name"]}
    Atk: {player["Atk"]}
    Heal: {player["Heal"]}
    Health {player["Health"]}''')
    new = False
playerwin = False
botwin = False
while True:
    print("-" * 27)
    print("\nplease select option")
    print("1. attack")
    print("2. heal")
    print("3. exit")
    pchoice = input("> ")
    if pchoice == '1':
        print("\nBONK")
        bot["Health"] = bot["Health"] - player["Atk"]  * random.randint(1, 2)
        print(f"{player['Name']} has attacked {bot['Name']}'")
        if bot["Health"] <= 0:
            print(f"{player['Name']} has win!")
            break
        else:
            player["Health"] = player["Health"] - bot["Atk"]  * random.randint(1, 2)
            print(f"{bot['Name']} has attacked {player['Name']}")
            if player["Health"] <= 0:
                print("Bot win")
                break
            else:
                status()
    elif pchoice == '2':
        print("\nHEAL!!")
        player["Health"] = player["Health"] + player["Heal"]
        print(f"{player['Name']} has heal {player['Heal']} HP! ")
        player["Health"] = player["Health"] - bot["Atk"]  * random.randint(1, 2)
        print(f"{bot['Name']} has attacked {player['Name']}")
        if player["Health"] <= 0:
            print(f"{bot['Name']} has win!")
            break
        else:
            status()
    elif pchoice == '3':
        break
    else: print("I can't understand")