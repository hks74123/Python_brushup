# Tuple

# Creating a tuple
weight=(50,70,80,60,30)
print(weight)

 # Indexing tuple elements
print(weight[0])
print(weight[1])
print(weight[2])
print(weight[3])
print(weight[4])

# SLicing the Tuple
#tuple[start:end:increment]
print(weight[1:len(weight)])

# List Comprehesion
pass_weight = 50
weight_new = [w for w in weight if w > pass_weight]
print(weight_new)
