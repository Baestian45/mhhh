import random
import string

def computer():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
         computer_move = "rock"
    elif computer_choice == 2:
        computer_move = "paper"
    elif computer_choice == 3:
        computer_move = "scissors" 
    return computer_move
    
print("\nlets play rock, paper, scissors!")
user_choice = input("what do u choose?: ")
computer_move = computer()

def user(user_choice):
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("choose a valid option (rock, paper, scissors)")

user
print(f"{user_choice}")
print(f"{computer_move}")