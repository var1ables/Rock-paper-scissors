#importing random number generator
import random

#pictures
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

#Defining variables
draw = "You drew with the computer"
win = "Congratulations you won"
loss = "Sorry you lost :("
snark = "You have to pick 0, 1 or 2 to play. You lost by default."

#Listing pictures which will be called pictures
pictures = [rock, paper, scissors]

#creating user choice
choice = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

#making user an integer
choice = int(choice)

#first of choice string
if choice >=3 or choice < 0: 
    print(snark) #snarking at a user choice
else:
    opponent = random.randint(0,2) #generating opposition choice

    print(pictures[choice])

    print(f"Computer chose {opponent}")
    print(pictures[opponent])

#defining how the game is decided
    if choice == 0 and opponent == 2:
        print(win)
    elif choice > 2 and choice < 0:
        print(snark)
    elif choice == 2 and opponent == 0:
        print(loss)
    elif opponent > choice: 
        print(loss)
    elif opponent < choice: 
        print(win)
    elif opponent == choice:
        print(draw)
    else: 
        print(snark)
    