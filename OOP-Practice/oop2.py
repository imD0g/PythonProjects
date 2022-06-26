# In this program we will learn about classes and objects for OOP

class Dog: # This is a class, and we are creating a class called Dog.
    species = "Canis familiaris" # Class variables - these are variables that are shared by all objects under the same class

    def __init__(self, name, age):
        self.name = name 
        self.age = age  

    # This used to be the "Description" method, but we renamed it to "__str__" to make it more readable.
    def __str__(self):
        return f"{self.name} is {self.age} years old" 

angus= Dog("Angus", 3)        # Create an instance of the class
# Now when we print the object, we will get the output of the __str__ method.
print(angus)





