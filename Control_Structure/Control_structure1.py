# If Else 

""" Syntax
if CONDITION:
    code block 1
elif CONDITION:
    code block 2
...
else:
    code block n
"""

score = 80
grade = None
if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 70:
    grade = "C"
elif score > 60:
    grade = "D"
elif score > 50:
    grade = "E"
else:
    grade = "F"
print("Grade: " + grade)

