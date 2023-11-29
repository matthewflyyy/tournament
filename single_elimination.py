print("Input all players' names. Once you have inputed all the names, type 'done'")

players = {}
typed = input("Player: ")

while typed != 'done':
    if typed in players:
        print("Player already exists")
    else:
        players[typed] = [0]
    typed = input("Player: ")

print(players)