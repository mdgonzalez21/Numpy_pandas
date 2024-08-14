import numpy as np
#Cero dimensiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
#Una dimensión
vector = np.array([1,2,3])
print(vector)
print(vector.ndim)
#Dos dimensiones 
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz) #imprime la matriz
print(matriz.ndim)
#Más de dos dimensiones
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)
#Agregar o eliminar dimensiones
vector = np.array([1,2,3],ndmin=10)
print(vector)
print(vector.ndim)
#Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0)
print(expand)
print(expand.ndim)
#Eliminar dimensiones que no estás usando
print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector.ndim)
#new_item para crear archivos desde powershell
