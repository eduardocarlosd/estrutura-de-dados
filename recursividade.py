def fatorial(n):
    # Caso base
    if n == 1 or n == 0:
        return 1
    # Passo recursivo
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
print(fatorial(5))  # Resultado será 120
