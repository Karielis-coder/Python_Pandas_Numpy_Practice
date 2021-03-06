import numpy as np


#crearemos una matriz aleatoria 4x4

matrix_4 = np.random.randint(1,25,size=(4,4))

print("La matriz 4x4 a utilizar es \n=", matrix_4)
print("-----------------------------------------------------------")
print("El dato más grande de esta matriz es= ", matrix_4.max())
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmax())
print("El dato más pequeño de esta matriz es= ", matrix_4.min())
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmin())
print("La diferencia ente el valor max y min es= ", matrix_4.ptp())
print("-----------------------------------------------------------")
print("El dato más grande de cada fila de esta matriz es= ", matrix_4.max(1))
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmax(1))
print("El dato más pequeño de cada fila de esta matriz es= ", matrix_4.min(1))
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmin(1))
print("La diferencia ente el valor max y min es= ", matrix_4.ptp(1))
print("-----------------------------------------------------------")
print("El dato más grande de cada fila de esta matriz es= ", matrix_4.max(0))
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmax(0))
print("El dato más pequeño de cada fila de esta matriz es= ", matrix_4.min(0))
print("La Ubicacion de este valor se encuentra en = ", matrix_4.argmin(0))
print("La diferencia ente el valor max y min es= ", matrix_4.ptp(0))
print("-----------------------------------------------------------\n\n")
print("La matriz ordenada por fila queda= \n", np.sort(matrix_4))
print("-----------------------------------------------------------")
print("El percentil 50 de los datos de la matriz es= ", np.percentile(matrix_4,50))
print("La mediana de los datos de la matriz es= ", np.median(matrix_4))
print("La mediana de las filas de la matriz es= ", np.median(matrix_4,1))
print("La mediana de las columnas de la matriz es= ", np.median(matrix_4,0))
print("-----------------------------------------------------------")
print("La desviacion estandar de los datos de la matriz es= ", np.std(matrix_4))
print("La desviacion estandar de las filas de la matriz es= ", np.std(matrix_4,1))
print("La desviacion estandar de las columnas de la matriz es= ", np.std(matrix_4,0))
print("-----------------------------------------------------------")
print("La varianza de los datos de la matriz es= ", np.var(matrix_4))
print("La varianza estandar de las filas de la matriz es= ", np.var(matrix_4,1))
print("La varianza estandar de las columnas de la matriz es= ", np.var(matrix_4,0))
print("-----------------------------------------------------------")
print("La media de los datos de la matriz es= ", np.mean(matrix_4))
print("La media de las filas de la matriz es= ", np.mean(matrix_4,1))
print("La media de las columnas de la matriz es= ", np.mean(matrix_4,0))
print("-----------------------------------------------------------")