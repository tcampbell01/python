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
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
if player_choice == '0': 
  print("You chose rock!")
  print(rock)
elif player_choice == '1':
  print("You chose paper!")
  print(paper)
else:
  print("You chose Scissors!")
  print(scissors)

computer_choice = ["0", "1", "2"]
random = random.choice(computer_choice)
print(random)
if random == '0':
  print("The computer chose Rock!")
  print(rock)
elif random == '1':
  print("The computer chose Paper!")
  print(paper)
else: 
  print("The computer chose Scissors")
  print(scissors)

if player_choice == "0" and random == "0":
  print("Player chose rock and Computer chose rock. Draw!")
elif player_choice == "0" and random == "1":
  print("Player chose rock and Computer chose paper. Computer wins!")
elif player_choice == "0" and random == "2":
  print("Player chose rock and Computer chose scissors. Player wins!")
elif player_choice == "1" and random == "0":
  print("Player chose paper and Computer chose rock. Computer wins!")
elif player_choice == "1" and random == "1":
  print("Player chose paper and Computer chose paper. Draw!")
elif player_choice == "1" and random == "2":
  print("Player chose paper and Computer chose scissors. Computer wins!")
elif player_choice == "2" and random == "0":
  print("Player chose scissors and Computer chose rock. Computer wins!")
elif player_choice == "2" and random == "1":
  print("Player chose scissors and Computer chose paper. Player wins!")
else: 
  print("Player chose scissors and Computer chose scissors. Draw!")



