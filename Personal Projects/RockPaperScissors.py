#Import + greeting
import random
from urllib.parse import uses_relative
valid=False
print("Hello and welcome to a game of Rock, Paper, Scissors. You will be facing against the computer")

# Take the users input & validate the input
while not valid:
      userguess=input("Please enter your guess: ")
      userguess=userguess.lower()
      if userguess in ['rock', 'paper', 'scissors']:
            valid=True
      else:
            print("Error, please only enter either Rock, Paper or Scissors as your input")

# Make a random guess from 1-3 and assign them to R,P,S

rpsArray=['rock','paper','scissors']
compguess=random.choice(rpsArray)
print("The Computer has chosen",compguess," and you have chosen",userguess)

if userguess == compguess:
      print("The game is a tie!")
elif userguess== 'rock':
      if compguess == 'scissors':
            print("Rock smashes scissors! You win!")
      else:
            print('Paper covers rock, you lose!')
elif userguess== 'paper':
      if compguess== 'rock':
            print('Paper covers rock, you win!')
      else:
            print("Scissors cuts paper! You lose.")
elif userguess == "scissors":
    if compguess == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
