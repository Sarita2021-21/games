import random
from art import logo 
print(logo)
print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
user_choice= (input("choose a difficulty. Type 'easy' or 'hard':")).lower()
if user_choice=="easy":
    # print("You have 10 attempts remaining to guess the number.")
    user_number= int(input("Make a guess"))
    computer_number=random.randint(1,100)
    # print(computer_number)
    attempts=10
    while attempts!=0:
        if user_number==computer_number:
             print(f"you got it! The answer is {computer_number}")
             break
        elif user_number< computer_number:
            print("Too low.")
            print("guess again!")
            attempts-=1
            print(f"You have attempts remaining {attempts}")
            user_number= int(input("Make a guess again!"))
        elif user_number>computer_number:
            print("too high.") 
            print("guess again!")
            attempts-=1
            print(f"You have attempts remaining {attempts}")
            user_number= int(input("Make a guess again!"))
    else:
        print("you have no more attempts remaining!")
    
elif user_choice=="hard":
    user_number= int(input("Make a guess"))
    computer_number=random.randint(1,100)
    # print(computer_number)
    attempts=5
    # print("You have 4 attempts remaining to guess the number.")
    while attempts!=0:
        if user_number==computer_number:
             print(f"you got it! The answer is {computer_number}")
             break
        elif user_number< computer_number:
            print("Too low.")
            print("guess again!")
            attempts-=1
            print(f"You have attempts remaining {attempts}")
            user_number= int(input("Make a guess again!"))
        elif user_number>computer_number:
            print("too high.") 
            print("guess again!")
            attempts-=1
            print(f"You have attempts remaining {attempts}")
            user_number= int(input("Make a guess again!"))
    else:
        print("you have no more attempts remaining!")
    
else:
    print("you typed a wrong input. try again!:-)")