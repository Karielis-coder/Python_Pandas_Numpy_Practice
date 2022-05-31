import numpy as np

#creando arrays de diferentes dimensiones

scalar = np.array(51, dtype=np.int16)
vector = np.array([1,2,3,4,5])
matriz = np.array([[1,2],[3,4],[5,6]])
tensor_3 = np.array([[[1,2],[3,4],[5,6]]])
print("This is a scalar= \n", scalar)
print("This is a vector (1D)= \n",vector)
print("This is a Matrix (2D)= \n", matriz)
print("This is a Tensor (3D)= \n", tensor_3)

#para saber el num de dim

print("Dimensions for scalar= ",scalar.ndim)
print("Dimensions for vector= ",vector.ndim)
print("Dimensions for matriz= ",matriz.ndim)
print("Dimensions for tensor= ",tensor_3.ndim)

# se puede agregar la cantidad de dimensiones del array directamente 

tensor_10 = np.array([1,2,3], ndmin=10)
print("This is a Tensor (10D)= \n", tensor_10)
print("Dimensions for tensor= ",tensor_10.ndim)

#igualmente podemos aumentar una dimension con la funcion expand

expand_tensor = np.expand_dims(tensor_10,axis=0)  #axis decide si expandir filas o columnas
print("This is a Tensor (10D)= \n", expand_tensor)
print("Dimensions for tensor= ",expand_tensor.ndim)

#por ultimo podemos remover o comprimir dimensiones que no estan siendo utilizadas con squeeze
# por ejemplo para tensor 10 tenemos 10 dimensiones pero solo estamos ocupando un espacio
# con datos, por lo tanto squeeze no quitara las otras 9 para tener una sola dimension

comp_tensor = np.squeeze(tensor_10)
print("This is the outcome for compressed tensor_10= \n", comp_tensor)
print("New Dimension for compressed tensor_10= ",comp_tensor.ndim)