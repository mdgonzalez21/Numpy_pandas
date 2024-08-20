import numpy as np

# Definir numeros aleatorios del1 al 20 en un vector 
arr = np.random.randint(1,20, size=(10))
print(arr)

print('------------------------------------')
# Llevarlo a una estrucutura matricial
matriz = arr.reshape(2,5)
print(matriz)
print('------------------------------------')

# Con max traer el numero mas grande que tenga el array 
maximo = arr.max()
print('Valor máximo array:', maximo)
maximo = matriz.max()
print('Valor máximo matriz:', maximo)

print('------------------------------------')
# Crear array de 2 dimensiones 
a = np.array([[1, 2],[3, 4]])
b = np.array([[5, 6]])

# Que pasa cuando quieres unir el array b con el a 
# Con el comando contenate se hara la union de ambos array 
c = np.concatenate((a,b), axis=0)
print(c)