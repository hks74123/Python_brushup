# Loops

# For loop
""" Syntax
For ELEMENT in SEQUENCE:
    code block...
"""

list=[10,20,30,40,50]

for i in list:
    print('Marks :',i)

for i in range(len(list)):
    print('Marks:',list[i])

# While Loop

""" Syntax
While condition:
    code block
"""

jj=0
while(jj<len(list)):
    print('Marks:',list[jj])
    jj+=1

