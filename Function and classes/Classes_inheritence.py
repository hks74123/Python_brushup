"""Inheritence

Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that child classes are 
derived from are called parent classes.

Syntax:
    class parent:
        code block...
    
    class child(parent):
        code block...

"""

# Parent Class
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Child classes
class identity(person):
    pass # Pass is used to avoid error and to pass code which is yet to be written

class verifying(person):
    pass

identifier1 = identity("Hemant", 19)
ver = verifying("Tarun", 20)
print(identifier1.description())  
print(ver.description())