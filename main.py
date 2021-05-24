import random
rock = '''
   Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
   Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors.")

user_choose = input("""Make your choice
1 for Rock
2 for Paper
3 for Scissors\n""")
user_choice = options[int(user_choose) - 1]
comp_choose = random.randint(1,3)
comp_choice = options[comp_choose - 1]
score = ""


if user_choice == comp_choice:
    score = "Draw"
elif (user_choose == "1" and comp_choose == 3) or (user_choose == "2" and comp_choose == 1) or (user_choose == "3" and comp_choose == 2):
    score = "You win"
else:
    score = "You lose"


print(f"You chose\n{user_choice}")
print(f"Comp chose \n{comp_choice}")
print(score)

