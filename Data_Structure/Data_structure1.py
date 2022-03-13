# List

# creating a list
weight=[15,10,40,60,25]

# Indexing list elements
print(weight[0])
print(weight[1])
print(weight[2])
print(weight[3])
print(weight[4])

# Modification in list
weight[0]=35
print(weight)

# SLicing the list
#list[start:end:increment]
print(weight[1:len(weight)])

# Add and removing list elements
  
#append will add element in last of list
weight.append(80)

#insert will insert the value at given index
weight.index(1,70)

#sorting list elements
print(sorted(weight))#This will print sorted list in ascending order
print(sorted(weight,reverse=True))#This will print sorted list in descending order

# List Comprehesion
pass_weight = 50
weight_new = [w for w in weight if w > pass_weight]
print(weight_new)
