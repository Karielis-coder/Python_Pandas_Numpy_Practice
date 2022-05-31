import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

#redefiniendo el tipo de datos
arr1=arr.astype(np.float64)
print(arr1)
#ahora tipo string
arr2=arr.astype(np.str_)
print(arr2)
#ahora booleano
arr3=arr.astype(np.bool_)
print(arr3)