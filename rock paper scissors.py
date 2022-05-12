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

#Write your code below this line 👇


player = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ')

if player == '0':
    print(rock)
elif player == '1':
    print(paper)
elif player == '2':
    print(scissors)
else:
    print('Invalid input.')
    exit()

computer_options = [rock, paper, scissors]
computer = computer_options[random.randint(0, 2)]

print('Computer chose:')

if computer == rock:
    print(rock)
elif computer == paper:
    print(paper)
elif computer == scissors:
    print(scissors)

if player == '0' and computer == paper:
    print('You lose.')
elif player == '1' and computer == scissors:
    print('You lose.')
elif player == '2' and computer == rock:
    print('You lose.')
elif player == '0' and computer == rock:
    print('Its a Draw.')
elif player == '1' and computer == paper:
    print('Its a Draw.')
elif player == '2' and computer == scissors:
    print('Its a Draw.')
else:
    print('You win!')

