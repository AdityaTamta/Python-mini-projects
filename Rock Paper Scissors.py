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
import random
list = [rock,paper,scissors]

user_choice = int(input('Choose 0 for rock, 1 for paper, 2 for scissors'))

if user_choice > 0 and user_choice <= 2:
    print(f"User's choice is {list[user_choice]}")

comp_choice = random.randint(0,2)
print(f"computers choice is {list[comp_choice]}")

if user_choice > 3 or user_choice < 0:
    print("Invalid input. you loose")
if user_choice == comp_choice:
    print("It is a tie")
elif user_choice  == 2 and comp_choice == 0:
    print("You Loose")
elif user_choice > comp_choice:
    print("You Win")
elif user_choice == 0 and comp_choice == 2:
    print("You Win")
elif user_choice < comp_choice:
    print("You Loose")






