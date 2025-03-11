import numpy as np

global not_found
not_found = -1

arr = np.array([1, 6, 2, 5, 4])

def find (alist, key):
    for i in range(0,len(alist)):
        if key == alist[i]:
            return i
    return not_found


chave = int(input("Digite a chave: "))

array_ordenado = np.sort(arr)


print(find(arr, chave))
print("Array ordenado:", array_ordenado)

