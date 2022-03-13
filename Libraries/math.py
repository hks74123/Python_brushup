"""Math module

Math module is useful as many math functions are already implemented and optimized.

"""
import math
import random
import statistics

#The math module gives access to the underlying C library functions for floating point math.
print(math.cos(math.pi / 4))
print( math.log(1024, 2))

#The random module provides tools for making random selections.
random_options = [10, 5, 4]
random_choice = random.choice(random_options)
print(random_choice)

"""
The statistics module calculates basic statistical properties (the mean, median,
variance, etc.) of numeric data.
 
"""

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
statistics.median(data)
