import numpy as np

array = np.array([-1,-5,-6,-2,-5,4])
maior_numero = array[0]
array_ordenado = np.sort(array)
array_ordenado_decrescente = np.sort(array)[::-1]

for i in range(len(array)):
    if array[i] > maior_numero:
        maior_numero = array[i]

print("O maior número é:",maior_numero)
print("Array ordenado:", array_ordenado)
print("Array ordenado em ordem decrescente:", array_ordenado_decrescente)