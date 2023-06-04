import random

computer = random.choice(["paper", "rock", "scissors"])

user_move = input("enter your move: ")

if user_move == computer:
    print("its a tie")
elif user_move == 'paper' and computer == 'rock':
    print('you win')
elif user_move == 'rock' and computer == "scissors":
    print("you win")
elif user_move == "scissors" and computer == "paper":
    print("you win")
else:
    print('compter win')

    
    