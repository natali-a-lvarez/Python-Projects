import random

player1: str
player2: str
round = 1
player1score = 0
player2score = 0

options = ["rock", "paper", "scissors"]

# choosing random 
def random_option(options):
    index = random.randrange(len(options))
    chosen = options[index]
    return chosen

# playing game
def play_game():
    player1 = random_option(options)
    player2 = random_option(options)

    if player1 == player2:
        print("there is a tie, try again")
    elif player1 == "rock" and player2 == "scissors":
        print("player 1 wins round")
        player1score += 1
    elif player1 == "paper" and player2 == "rock":
        print("player 1 wins round")
        player1score += 1
    elif player1 == "scissors" and player2 == "paper":
        print("player 1 wins round")
        player1score += 1
    elif player2 == "rock" and player1 == "scissors":
        print("player 2 wins round")
        player2score += 1
    elif player2 == "paper" and player1 == "rock":
        print("player 2 wins round")
        player2score += 1
    elif player2 == "scissors" and player1 == "paper":
        print("player 2 wins round")
        player2score += 1


play_game()