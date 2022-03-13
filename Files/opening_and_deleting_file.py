"""File Opening

Python has a built-in open() function to open a file. This function returns a file object, 
also called a handle, as it is used to read or modify the file accordingly.

Syntax:
    open("test.txt",encoding='utf-8')    # open file in current directory

We can specify the mode while opening a file. 
In mode, we specify whether we want to read r, write w or append a to the file

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

"""

# Opening File
f=open("text.txt", mode='r',encoding='utf-8')
read_data = f.read()#read is used to read the data of the opened file
print(read_data)


"""Closing FIle

Closing a file will free up the resources that were tied with the file. 
It is done using the close() method available in Python.
Syntax:
    f=open("test.txt",encoding='utf-8')
    f.close()
"""

#Closing File
f.close()

