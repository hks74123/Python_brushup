"""Numpy

numPy is python library used for working with array
syntax to import:
import numPy as np 

"""

import numPy as np 

#creating an array
arr = np.array([1, 2, 3, 4, 5])

# crearting a tuple
tpl=np.array((1, 2, 3, 4, 5))

# SLicing the array
#array[start:end:increment]
print(arr[1:len(arr)])

# data type
# dtype is used to define/get data type of an array
arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr1.dtype)  

# Copy and View

#Copy is used to make duplicate of array any changes will not effect the original one
arr2 = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr2[0] = 42
print(x) 

# View not only duplicate but also make the changes that are made in original
arr3 = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr3[0] = 42   
print(x)  