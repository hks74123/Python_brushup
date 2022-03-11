# Functions

""" Syntax for function 
    def function_name(parameters):
        code block...
        return value
"""

# Defining the function
def area_of_square(length, breadth):
    area = length*breadth
    return area

# Calling the function
area_of_square(2, 3)

# Function with default arguments
def greet(name=""):
    print("Hello " + name)

greet("Harish")
greet()