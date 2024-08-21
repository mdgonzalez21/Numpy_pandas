import numpy as np

arr = np.arange(0,11)
print(arr)

trozo_de_arr = arr[0:6]
print(trozo_de_arr)

# A todo el array quitar todo los valores y dejarlo vacio 
trozo_de_arr[:]=0
print(trozo_de_arr)

# Si se imprime arr los valores a cambiado 
print(arr)

# Para solucionar lo anterior se usa el comando copy 
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)