# imports 
import random

# Variables
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

choices = [rock, paper, scissors]
random_choice = random.randint(0, 2)

# Greeting
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Catch invalid input
if choice >=3 or choice < 0:
    print("You typed an invalid number, you lose!")
# Continue if correct
else:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

    print(f"Computer chose: {choices[random_choice]}")


    if choice == 0 and random_choice == 0:
        print("You Draw")
    elif choice == 0 and random_choice == 1:
        print("You Lose")
    elif choice == 0 and random_choice == 2:
        print("You Win")
    elif choice == 1 and random_choice == 0:
        print("You Win")
    elif choice == 1 and random_choice == 1:
        print("You Draw")
    elif choice == 1 and random_choice == 2:
        print("You Lose")
    elif choice == 2 and random_choice == 0:
        print("You Lose")
    elif choice == 2 and random_choice == 1:
        print("You Win")
    else:
        print("You Draw")
