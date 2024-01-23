import random

def play_rock_paper_scissors(player1_choice):
    player2 = random.choice(["rock", "paper", "scissor"]).lower()
    print("Player 2 selected:", player2)

    if player1_choice == "rock" and player2 == "paper":
        return "Player 2 Won"
    elif player1_choice == "paper" and player2 == "scissor":
        return "Player 2 Won"
    elif player1_choice == "scissor" and player2 == "rock":
        return "Player 2 Won"
    elif player1_choice == player2:
        return "Tie"
    else:
        return "Player 1 Won"

if __name__ == "__main__":
    player1_input = input("Select Rock, Paper, or Scissor: ").lower()
    result = play_rock_paper_scissors(player1_input)
    print(result)
