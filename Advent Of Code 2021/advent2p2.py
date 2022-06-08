#input the data
with open(r"Z:\VSC-repo\AOC\advent2pt2.txt.") as fin:
      data = [i for i in fin.read().strip().split("\n")] # Takes the data from the file and puts into array 
#print(data)

"""
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
"""
def func():
      aim=0
      hor=0
      depth=0
      ans=0
      for i in data: # Loop through array and get horizontal position and depth
            movement=i[:-2] # gets the movement for each input in the array e.g forward back etc
            distance=int(i[-1]) # gets the number value
            if movement=="down":
                  aim=aim+distance
            elif movement=="up":
                  aim=aim-distance
            elif movement=="forward":
                  hor=int(hor+distance)
                  depth+=aim*distance
      ans=hor*depth
      print('The answer is',ans)
func()
