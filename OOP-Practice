# In this program we will learn about classes and objects for OOP

class Dog: # This is a class, and we are creating a class called Dog.
    species = "Canis familiaris" # Class variables - these are variables that are shared by all objects under the same class

    def __init__(self, name, age): # Defining the constructor, this is the first method called when an object is created
        self.name = name # Instance variables - these are variables that are unique to each object, this is the only way to access them
        self.age = age # You can access the class variables from the instance methods using the self keyword followed .name or .age 

    # Instance method
    def description(self): # This is a method, and it is called on an instance of the class
        return f"{self.name} is {self.age} years old" # This is a string interpolation, and it is called on an instance of the class

    # Another instance method
    def speak(self, sound): 
        return f"{self.name} says {sound}"

# The above code allows you to call these methods on an instance of the class to return the outputs for the object.
# If you created a new object, you can call the methods on that object. For example: Dog("Fido", 3).description()
# This would return "Fido is 3 years old"

angus= Dog("Angus", 3)        # Create an instance of the class
print(angus.description())    # This would return "Angus is 3 years old".
print(angus.speak("Woof"))    # This would return "Angus says Woof"

# Now lets look at printing "Angus", we would expect to be able to just print the object, but this is not possible.
print(angus)      # This would return "<__main__.Dog object at 0x000002F8D8F8B8F8>"
# This is because the object is not a string, it is an object.
# To print the object, in a friendly way, we would have to change the description method to return a string.

# Now look at OOP2.py 




