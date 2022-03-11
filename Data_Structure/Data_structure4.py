# Dictionary

# Creating dictionaries
student = {"name":"Hemant", "reg_no":"19bcs039", "course":"BTech"}
print(student)

#Accessing elements
print(student["course"])
for key, value in student.items():
    print("Key: %s ; Value: %s" % (key, value))

