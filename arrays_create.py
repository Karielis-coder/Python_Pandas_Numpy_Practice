import numpy as np

list(range(0,10)) #esto no es un objeto de numpy 
#para crearlo con numpy se de be hacer:

arr1=np.arange(0,20,2)
print(arr1)

#una funcion muy utilizada es zero, cuya funcion es solo colocar de zeros una matriz
# en este caso se hara un amatriz 10 x 10

tensor_10 = np.zeros((10,10))
print("Este es un tensor zero de 10 dimensiones= \n", tensor_10)

#esto mismo se puede realizar con unos
tensor_10 = np.ones((10,10))
print("Este es un tensor ones de 10 dimensiones= \n", tensor_10)

# uso de linspace para crear datos de forma normalizada

arr_lins = np.linspace(0,20,10)
print("Este es un array creado con linspace con 10 datos en un rango de 0 a 20= \n", arr_lins)


#Igual podemos crear una matriz identidad con la funcion eye

arr_id = np.eye(4)
print("Esta es una matriz identidad 4x4= \n", arr_id)

#para generar listas  aleatorias se usa random ran

random_scalar = np.random.rand()
random_vector = np.random.rand(4)
random_matrix = np.random.rand(4,4)

print("Este es un escalar aleatorio= \n", random_scalar)
print("Este es un vector con 4 datos aleatorio= \n", random_vector)
print("Esta es una matrix 4x4 con datos aleatorio= \n", random_matrix)

# Igualmente podemos crear numeros aleatorios en un rango con randint

randomint_scalar = np.random.randint(1,15)
randomint_vector = np.random.randint(5, size=4)
randomint_matrix = np.random.randint(1,100,size=(4,4))

print("Este es un escalar aleatorio dentro del rango 1 a 15= \n", randomint_scalar)
print("Este es un vector con 4 datos aleatorio entre 0 a 5= \n", randomint_vector)
print("Esta es una matrix 4x4 con datos aleatorio entre 1 a 100= \n", randomint_matrix)