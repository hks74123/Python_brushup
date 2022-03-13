# Continue and break
"""Break

The break statement terminates the loop containing it. 
Control of the program flows to the statement immediately after the body of the loop.

Syntax:
    for condition:
        if condition:
            break
        code block...

"""

"""Continue

The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
Loop does not terminate but continues on with the next iteration.

Syntax:
    for condition:
        if condition:
            continue
        code block...

"""
#break
for val in "hemant":
    if val == "a":
        break
    print(val)

print("The end")

# continue
for val in "hemant":
    if val == "e":
        continue
    print(val)

print("The end")