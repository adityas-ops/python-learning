import random


def get_choice():
    player_choice = input('Enter a choice (rock, paper, scissors:')
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    print(f"you choose {player_choice} --- computer choose {computer_choice}")
    return checkWin(player_choice,computer_choice)




def checkWin(player,computer):
    if player == computer:
        return "It's a tie!"
    elif  player == "rock":
        if computer == "scissor":
          return "Rock smashes Scissor! you win!"
        else:
            return "Paper Cover Rock! you loose!"
    elif  player == "Paper":
            if computer == "scissor":
              return "scissor cut paper! you loss!"
            else:
                return "Paper Cover Rock! you win!"
    elif  player == "scissor":
                if computer == "rock":
                  return "Rock smashes Scissor! you loss!"
                else:
                    return "scissor cut paper! you win!"



print(get_choice())

