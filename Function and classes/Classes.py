# Classes

"""Syntax for defining Class
   class classname:
        code block...
"""
# properties that every class object should contain are defined in __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Objects
hemant=Person("Hemant",20)
print(hemant.description())
