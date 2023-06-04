import random 

secret_number = random.randint(1, 10)
print(secret_number)
chances = 3


while chances != 0:
    
    user_guess = input("What do you think the number is from 1 to 10: ")
    
    if not user_guess.isdigit():
        print("try again it's not a number")
        chances -=1
        continue
    user_guess = int(user_guess)
   
    if user_guess == secret_number:
        print("You found the number. You win!")
        break

    elif user_guess > secret_number:
        print("Take a guess lower!")
        chances -= 1
        
    else:
        print("Take a guess higher")
        chances -= 1
if chances == 0:
    print("You lost. You wasted all of your chances.")