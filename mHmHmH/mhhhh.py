import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("\nEnter Rock, Paper or Scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please choose between rock, paper or scissors")
        return

    computer_choice = random.choice(choices)

    print(f"\nyou chose {player_choice}, the computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("\nTie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
         print("\nYou Win!")
    else:
        print("\nLoser :DDD")

def main():
    while True:
        play_game()
        play_again = input("\nDo you wanna play again? (yes/no): ").lower()
        if play_again != "yes":
            print("bitch")
            break 
        print("\nthanks for playing ig")

main()