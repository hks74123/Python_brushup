# Classes

"""Syntax for defining Class
   class classname:
        code block...
"""
# properties that every class object should contain are defined in __init__()
class Person:
    # The self parameter is a reference to the class itself, and is used to access variables
    # that belongs to the class. It does not have to be named self , you can call it
    # whatever you like, but it has to be the first parameter of any function in the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Objects
hemant=Person("Hemant",20)
print(hemant.description())
