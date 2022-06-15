#import the data set
with open(r"Z:\VSC-repo\AOC\advent3.txt.") as fin:
      data = [i for i in fin.read().strip().split("\n")] # Takes the data from the file and puts into array

#calculate the gamma rate (for each number in each binary string then average 1 and 0 to get most common value)
#calculate the epsilon rate (inverse of gamma)
def partone(data):
      count1=0
      count0=0
      epsilon=""
      gammastring=""
#----------------------------------------------------------------------------------------------------------------------
      
      for i in range(0, len(data[0])): # for each number in the binary string
            count1=0
            count0=0
            for j in range(0, len(data[0])): #for each number in the binary string and each value in the binary string
                  if data[i][j]=="1": # if the number is 1
                        count1=count1+1 # add 1 to the count of 1s
                  else:
                        count0=count0+1 # add 1 to the count of 0s
            if count1>count0: # if the count of 1s is greater than the count of 0s
                  gammastring=gammastring+"1" # add "1" to the gamma string
                  epsilon=epsilon+"0" # add "0" to the epsilon string
            else:
                  gammastring=gammastring+"0" # add "0" to the gamma string
                  epsilon=epsilon+"1" # add "1" to the epsilon string
      print("The gamma is:",gammastring) # print the gamma string
      print("The Epsilon is:",epsilon) # print the epsilon string

#----------------------------------------------------------------------------------------------------------------------
#calculate the power consumption (gamma rate * epsilon rate)
#Convert the binary string to decimal
#----------------------------------------------------------------------------------------------------------------------
     # I used an online calculator to change the binary strings to decimal and then mulitplied
#----------------------------------------------------------------------------------------------------------------------
#call functions
partone(data)
