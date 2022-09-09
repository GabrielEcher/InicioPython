"""
Função que receba um vetor X como parametro, dois vetores A e B.
O vetor A deve conter os números pares do vetor X
e o vetor B os números ímpares
"""
import random

x = [random.randint(1, 30)for n in range(30)]
print(f'Vetor formado aleatóriamente:\n{x}')
a = []
b = []

def return_pares(x):
    for n in x:
        if n % 2 == 0:
            a.append(n)
        else:
            b.append(n)
    return f'O os números pares do primeiro vetor:\n{a}\nOs números ímpares do segundo vetor:\n{b}'

print(return_pares(x))