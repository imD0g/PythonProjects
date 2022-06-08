#input the data
with open(r"Z:\VSC-repo\AOC\advent2.txt.") as fin:
      data = [i for i in fin.read().strip().split("\n")] # Takes the data from the file and puts into array                                           
#print(data[0])
def partOne():
      position=0
      depth=0
      for i in data: # Loop through array and get horizontal position and depth
            movement=i[:-2] # gets the movement for each input in the array e.g forward back etc
            distance=int(i[-1]) # gets the number value
            if movement=="forward":
                  position=position+distance
            elif movement=="up":
                  depth=depth-distance
            elif movement=="down":
                  depth=depth+distance
      ans=(position*depth)
      print(position)
      print(depth)
      print(ans)

def partTwo():
      print("hi")


partOne()
partTwo()
