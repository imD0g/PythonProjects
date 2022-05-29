from ast import Break
import random 

name=input("Hello, welcome to the guessing game! Please tell me your name: ")
print(name+", right? Nice to meet you")
x=int(input ("Please set your max range for the random number you want me to pick: "))
maxguess=int(input("Please enter the number of guesses you would like to have: "))
numofguess=0
num=random.randint(1,x)
print("Okay! I have my guess, are you ready? Here we go!")


while numofguess < maxguess:
      
      guess=int(input("Please try and guess my number: "))
      numofguess +=1
      #range1= range(1,x,1)
     # if guess in range1:
       #     print(guess,"Is a valid input, let me check if your guess was right")
     # else:
     #       print(guess,"IS NOT A VALID INPUT *EXPLODES*")
     #       quit()
      if guess < num:
            print("Your guess was too low! Try again")
      if guess > num:
            print("Your guess was too high! Try again")
if guess == num:
      print("Well done! You guessed my number in ",numofguess,"tries!")
else:
      print("You ran out tries, my number was: ",num)