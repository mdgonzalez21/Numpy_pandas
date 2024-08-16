import  numpy as np

# Generamos numeros aleatorios entre 1 y 10 con una estrucutura de 3x2 
arr = np.random.randint(1,10, size=(3,2))
print("Forma original:", arr.shape)
print(arr)

# Cambiamos la forma del arreglo a una forma de (1,6) 
arr_reshape = arr.reshape(1,6)

# Imprimimos el arreglo despues del cambio 
print("Forma reshape:", arr_reshape.shape)
print(arr_reshape)