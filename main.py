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
selection = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')
number = random.randint(0,2)
choices = ['Rock', 'Paper', 'Scissors']
player_choice = choices[int(selection)]
cpu_choice = choices[number]
if player_choice == 'Rock':
  print(rock)
elif player_choice == 'Paper':
  print(paper)
elif player_choice == 'Scissors':
  print(scissors)
print('Computer chose: \n')
if cpu_choice == 'Rock':
  print(rock)
elif cpu_choice == 'Paper':
  print(paper)
elif cpu_choice == 'Scissors':
  print(scissors)

if player_choice == cpu_choice:
  print('Draw')
elif player_choice == 'Paper' and cpu_choice == 'Scissors':
  print('You Lose')
elif player_choice == 'Rock' and cpu_choice == 'Paper':
  print('You Lose')
elif player_choice == 'Scissors' and cpu_choice == 'Rock':
  print('You Lose')
else:
  print('You Won')
