import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
chose=int(input("what do you want to choose? type 0 for rock, 1 for paper or 2 for scissors"))
if chose==0:
    print(rock)
if chose==1:
    print(paper)
if chose==2:
    print(scissors)
rock==0
paper==1
scissors==2
choice=[0,1,2]
print("computer chose")
computer_chose=random.randint(0,2)
if computer_chose==0:
    print(rock)
if computer_chose==1:
    print(paper)
if computer_chose==2:
    print(scissors)
# print(computer_chose)
if chose==0 and computer_chose==2:
    print("You won")
elif chose==2 and computer_chose==1:
    print("You won")
elif chose==1 and computer_chose==0:
    print("You won")
elif chose==computer_chose:
    print("its draw")
else:
    print("You lose")
     