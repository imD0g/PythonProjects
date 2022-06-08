nameList = ["cam"]
duplicate = False
username = input("What is your name?: ")
nameList.append(username)
# for username in nameList: 
if(nameList.count(username) > 1):
    duplicate = True
    removename = input("We have found your name in the list already, do you want it removed? (Y/N): ")
    if (removename == "Y"):
        nameList.remove(username)
        print ("Your name has been removed from the list, thank you, ", username)
    else:
            print ("Your username has not been removed from the list, here are all entries in the list: ", nameList)
                    
else:
                print ("We have not found your name in the list, so we have added it, here is all entries in the list: ", nameList)
            


            
            
