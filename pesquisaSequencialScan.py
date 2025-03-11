import numpy as np

global not_found
not_found = -1

arr = [1, 2, 4, 5, 6]

def scan(alist, key):
    n = len(alist)
    for i in range(0, n):
        if key == alist[i]:
            return i
        elif key < alist[i]:
            return not_found
    return not_found


chave = int(input("Digite a chave: "))


print(scan(arr, chave))
