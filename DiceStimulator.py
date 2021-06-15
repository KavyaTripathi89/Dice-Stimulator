import random


def main():
    player1 = 0
    player1Wins = 0
    player2 = 0
    player2Wins = 0
    rounds = 1

    while rounds!=4:
        print("ROUNDS: "+str(rounds))
        player1 = dice_roll()
        print("Player1: "+str(player1))
        player2 = dice_roll()
        print("Player2: "+str(player2))

        if player1==player2:
            print("DRAW!\n")
        elif player1 > player2:
            player1Wins += 1
            print("Player 1 WON\n")
        else:
            player2Wins += 1
            print("Player 2 WON\n")

        rounds +=1

    
    if player1Wins == player2Wins:
        print("OVERALL DRAW")
    elif player1Wins > player2Wins:
        print("Player1 WON, rounds: "+str(player1Wins))
    else:
        print("Player2 WON, rounds: "+str(player2Wins))

    
def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()

