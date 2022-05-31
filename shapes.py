import numpy as np

# con la funcion shape podemos saber la forma de un arreglo

arr = np.random.randint(1,10,size=(2,3))
print("La matriz es \n", arr)
print("La forma de esta matriz es= ", arr.shape)

# igualmente se puede cambiar la forma del array siempre y cuando se respeten todos os valores

arr_1 = np.random.randint(1,10,size=(2,3))

print("La matriz es \n", arr_1)
print("La forma de esta matriz es= ", arr_1.shape)
arr_reshape=np.reshape(arr_1,(3,2),'A')
print("La matriz ha cambiado su forma a \n",arr_reshape)
print("La forma de esta matriz es= ", arr_reshape.shape)