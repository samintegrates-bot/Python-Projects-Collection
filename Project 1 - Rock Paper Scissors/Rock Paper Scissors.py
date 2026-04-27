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
choices = [rock, paper, scissors]
comp = random.choice(choices)
game=int(input("Enter Rock (1) Paper (2) or Scissors (3):  "))
if game == 1:
    print(rock)
    if comp == choices[0]:
        print("Computer Chose" + '\n' + comp)
        print("Tie")
    elif comp == choices[1]:
        print("Computer Chose" + '\n' + comp)
        print("You Lose!")
    elif comp == choices[2]:
        print("Computer Chose" + '\n' + comp)
        print("You Win!")
elif game == 2:
    print(paper)
    if comp == choices[0]:
        print("Computer Chose" + '\n' + comp)
        print("You Win!")
    elif comp == choices[1]:
        print("Computer Chose" + '\n' + comp)
        print("Tie!")
    elif comp == choices[2]:
        print("Computer Chose" + '\n' + comp)
        print("You Lose!")
elif game == 3:
    print(scissors)
    if comp == choices[0]:
        print("Computer Chose" + '\n' + comp)
        print("You Lose!")
    elif comp == choices[1]:
        print("Computer Chose" + '\n' + comp)
        print("You Win!")
    elif comp == choices[2]:
        print("Computer Chose" + '\n' + comp)
        print("Tie!")