import random
import time

def evenNumPlayers(players):
    round = []
    while len(players) > 0:
        print(players)
        matchup = []
        player1Index = random.randint(0, len(players)-1)
        matchup.append(players[player1Index])
        players.pop(player1Index)
        player2Index = random.randint(0, len(players)-1)
        matchup.append(players[player2Index])
        players.pop(player2Index)
        round.append(matchup)
    return round



def createBracket (players):
    if len(players) % 2 == 0:
        matchups = evenNumPlayers(players)

    # return oddNumPlayers
    print("Here are the matchups for this round:")
    for matchup in matchups:
        print(f"{matchup[0]} vs. {matchup[1]}")
    return matchups

def playRound(matchups):
    ready = input("Ready to play? ")
    if ready == 'Yes':
        matchupNum = 1
        for matchup in matchups:
            input(f"Who won {matchup[0]} vs. {matchup[1]}? ")

    elif ready == 'Cancel':
        exit
    else:
        playRound(matchups)




def start():
    print("Input all players' names. Once you have inputed all the names, type 'done'")

    typed = input("Player: ")
    players = []

    while typed != 'done':
        if typed in players:
            print("Player already exists")
        else:
            players.append(typed)
        typed = input("Player: ")

    print("Players: ")
    time.sleep(0.5)
    for player in players:
        print("-" + player)
        time.sleep(0.5)

    print("Creating bracket...")
    time.sleep(0.5)
    matchups = createBracket(players)
    playRound(matchups)

start()