# Python program to demonstrate encapsulation

class base:
      def __init__(self):
            self._a = 10 # private variable

class derived(base):
      def __init__(self):
            super().__init__() # calling base class constructor, super() calls the parent class
            print("Calling the protected variable of base class:", self._a)

            self._a = 20 # overriding the private variable
            print("Overriding the protected variable of base class:", self._a)

object = derived()
object2 = base()

# Calling the protected variable of base class: 10
print("Calling the protected variable of base class:", object._a)

# Accessing the protected variable outside the class
print("Accessing the protected variable outside the class:", object2._a)
            
            