# make fucntions for each D(X) dice (6,20?)
import random
howmany=int(input("How many dice would you like to roll? (1-5): "))
loop=True
diceroll=[]

while loop is True:
      for i in range(howmany):
            diceroll.append(random.randint(1,6))
             
      for l in diceroll:
            if l == 1:
                  print("""
                  -----
                  |   |
                  | o |
                  |   |
                  -----""")
            elif l==2:
                  print("""
                  -----
                  |o  |
                  |   |
                  |  o|
                  -----""")
            elif l==3:
                  print("""
                  -----
                  |o  |
                  | o |
                  |  o|
                  -----""")
            elif l==4:
                  print("""
                  -----
                  |o o|
                  |   |
                  |o o|
                  -----""")
            elif l==5:
                  print("""
                  -----
                  |o o|
                  | o |
                  |o o|
                  -----""")
            elif l==6:
                  print("""
                  -----
                  |o o|
                  |o o|
                  |o o|
                  -----""")   


            

      check=input("Do you want to roll again? (Y/N): ")
      check=check.lower()

      if check == "y":
            loop=True
            diceroll=[]
            print("--------------------------------")
      else:
            loop=False
            diceroll=[]
            print("--------------------------------")









#def dice():
 #     num=int(input("How many dice would you like to roll? (1-5): "))
 ##     print(num)
#
#dice()
# Ask the user how many sides they want.
# rolling
# display
