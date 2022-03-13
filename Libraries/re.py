"""
The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

"""
import re

# findall finds all occurence of the given string
txt = "This is hemant here"
x = re.findall("ma", txt)
print(x)

#The split() function returns a list where the string has been split at each match: 
x = re.split("\s", txt, 1)
print(x) 