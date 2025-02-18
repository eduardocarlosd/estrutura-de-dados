import numpy as np

array = np.array([-1,-5,-6,-2,-5,4])
maior_numero = array[0]


for i in range(len(array)):
    if array[i] > maior_numero:
        maior_numero = array[i]

print("O maior número é:",maior_numero)