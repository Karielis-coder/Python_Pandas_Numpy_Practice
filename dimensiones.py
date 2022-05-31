import numpy as np

scalar=np.array(42)
print(scalar.ndim)
vector=np.array([1,2,3])
print(vector.ndim)
matriz=np.array([[1,2,3],[4,5,6]])
print(matriz.ndim)
tensor=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(tensor.ndim)
#print(tensor)
#agregar o eliminar dimensiones

vector=np.array([1,2,3], ndmin=10)
print(vector.ndim)
print(vector)

#para expandir sin definirlo

expand=np.expand_dims(np.array([1,2,3]),axis=0)
print(expand)