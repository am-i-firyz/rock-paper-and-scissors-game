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

user = int(input("Choice one: rock - 0, paper - 1, scissors - 2. \n"))

choice = [rock, paper, scissors]
choice2 = ["rock", "paper", "scissors"]
computer = random.randint(0,2)

print(f"You choosed {choice2[user]}.\n{choice[user]}")
print(f"Computer choosed {choice2[computer]}.\n{choice[computer]}")

if user == 0 and computer == 0 or user == 1 and computer == 1 or user == 2 and computer == 2:
  print("Draw!")
elif user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
  print("You won!")
elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
  print("You lose!")
