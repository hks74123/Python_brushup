# Set

#creating of sets
cities = {"Madras", "Delhi", "Bombay", "Calcutta", "Madras"}
print(cities)

# Set Operations
a = {1, 2, 3, 4}
b = {4, 5, 6}
# Set Union
print(a | b)
# Set Intersection
print(a & b)
# Set Difference
print(a - b)
# Symmetric Difference
print(a ^ b)

# Adding and removing set elements
a.add(7)
print(a)
a.remove(7)
print(a)