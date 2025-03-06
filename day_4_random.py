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
game= [ rock , paper, scissors ]

pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

my_choice= game[pick]
computer = random.randint(0, len(game) - 1)

computer_choice= game[computer]

if my_choice == computer_choice:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n It is a tie")
elif my_choice == rock and computer_choice == paper:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Lose")
elif my_choice == rock and computer_choice == scissors:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Win")
elif my_choice == paper and computer_choice == rock:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Win")
elif my_choice == paper and computer_choice == scissors:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Lose")
elif my_choice == scissors and computer_choice == rock:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Lose:")
elif my_choice == scissors and computer_choice== paper:
    print(f"my choice\n{my_choice}\n computer choice\n {computer_choice}\n You Win")
