# Rahil
# This game is a script of Rock, Paper, Scissors
#
from random import randint
        
print("Welcome to RPS")

user_input = input ("Choose rock, paper, or scissors \n")

def RPSGame(user_input):

    options = ["rock", "paper", "scissors"]
    random_number = randint(0,2)
    computers_choice = options[random_number]


    if user_input != options[0] and user_input != options[1] and user_input != options[2]:
        user_input == input ("Invalid input, please try again, (lowercase only)")
        
    print("Computer chooses " , computers_choice)
    print("User chooses " , user_input)
        
    if user_input == options[0] and computers_choice == options[2] or user_input == options[1] and computers_choice== options[0] or user_input == options[2] and computers_choice == options[1]:
        print("You win")
    elif user_input == computers_choice:
        print("Tie")
    else:
        print("You lose")

RPSGame("rock")