"""Multiple Inheritance

When a class is derived from more than one base class it is called multiple Inheritance. 
The derived class inherits all the features of the base case.

Syntax:
    class A:
        code block...
    class B:
        code block...
    class C(A,B):
        code block...
    
"""
# Base class1
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def get_name(self):
        return f"{self.name}"
    def get_age(self):
       return f"{self.age}" 

# Base class2
class college:
    def clg(self):
        return "SMVDU"
# inhertitence class
class childrenclass(person, college):
    pass

obj=childrenclass("Hemant",19)
print(obj.get_name())
print(obj.get_age())
print("Currently "+obj.get_name()+" is in "+obj.clg()+" University.")