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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("Invalid input. Retry......")

print("Computer's Hand....")
a = (0, 1, 2)
user1 = random.choice(a)

if user1 == 0:
    print(rock)
elif user1 == 1:
    print(paper)
elif user1 == 2:
    print(scissors)


if user == user1:
    print("Draw match")
elif (user == 0 and user1 == 2) or (user == 1 and user1 == 0) or (user == 2 and user==1):
    print("You defeated Computer...")
else:
    print("Computer defeated You...")
