# import the data  set assign it to an array
import numpy as np
data = np.loadtxt(r"Z:\VSC-repo\AOC\advent1.txt.", dtype=int)
count=0
# loop through the array and count if they number before it is lower, if it is, then add 1 to a count
for x in range(0, len(data)):
      if data[x-1] < data[x]:
            count=count+1   
# provide an answer
print(count)
