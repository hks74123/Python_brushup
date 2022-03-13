"""Reading file

To read a file in Python, we must open the file in reading r mode.
We can user read() to read file and can also use read(size) method to read in 
the size number of data.

"""
#Opening the file
f=open("text.txt", mode='r',encoding='utf-8')
# reading the data
read_data = f.read()
print(read_data)

# Closing the file
f.close()

"""Writting file

In order to write into a file in Python, we need to open it in write w, 
append a or exclusive creation x mode.

"""
# writting file
f1=open("text.txt",'w',encoding = 'utf-8')
f1.write("my first file\n")

# Closing the file
f1.close()