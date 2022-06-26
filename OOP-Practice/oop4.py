# Now we will be looking at inheritance. Inheritance is the process of creating a new class from an existing class.
# Think of it like genetics, where you take a parent class and create a child class from it.
# This will inherit all the methods and variables from the parent class.

# We will create a dog park for this example

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Now we want to create child classes from the parent class.
# We will create a subclass called Labrador, Poodle and Bulldog from the parent class Dog.
# This is inheritance, and they will inherit all the methods and variables from the parent class.

class Labrador(Dog): # This is a subclass, and we are creating a subclass called Labrador from the parent class Dog.
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"

class Poodle(Dog):
    pass

class Bulldog(Dog):
    pass


# Now we can create instances of these new classes.
# We will create instances of the Labrador class, Poodle class, and Bulldog class.

buddy= Labrador("Buddy", 3)
angus= Poodle("Angus", 2)
teddy= Bulldog("Teddy", 1)

# We can see that these new classes inherit all the methods and variables from the parent class.

print(buddy.species) # This will return "Canis familiaris" as the Labrador class inherits the species variable from the parent class.
print(angus.name) # This will return "Angus" as the Poodle class inherits the name variable from the parent class.
print(teddy.age) # This will return "Teddy" as the Bulldog class inherits the age variable from the parent class.

# To determine which class a given object belongs to, you can use the built-in type():
print(type(buddy)) # This will return "<class '__main__.Labrador'>"

# What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance():
print(isinstance(buddy, Dog)) # This will return True as buddy is also an instance of the Dog class.

print(isinstance(buddy, Poodle)) # This will return false as buddy is not a Poodle class.

print(buddy.speak())
