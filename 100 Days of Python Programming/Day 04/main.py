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

print("Welcome to Rock, Paper, Scissors!")
user_input = int(input("For Rock Enter '1', for Paper Enter '2', for Scissors Enter '3': "))

if user_input <= 3:
    if user_input == 1:
        print(rock)
    elif user_input == 2:
        print(paper)
    else:
        print(scissors)

    computer_input = random.randint(1, 3);

    if computer_input == 1:
        print(rock)
    elif computer_input == 2:
        print(paper)
    else:
        print(scissors)

    if user_input == computer_input:
        print("Draw!")
    elif user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
        print("You Lose")
    else:
        print("You Win")

elif user_input == 0 or user_input > 3:
    print("Invalid Input!")





