# Function to find the next perfect square
import math
def find_sqrt(sq):
    if (math.sqrt(sq)).is_integer() == True:
        print("The input is a perfect square(", sq, ")")
        print("Attempting to find the next perfect square")
        number+=1
        found = False
        while found == False:
            if (math.sqrt(number)).is_integer() == True:
                return("The next perfect square is", number)
                found = True
            else:
                number+=1
    else:
        print("The input is not a perfect square")
        return -1
