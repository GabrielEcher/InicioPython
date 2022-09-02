"""
Programa que lê um número inteiro positivo n e em seguida imprima
n linhas do chamado triangulo de pascal
"""

from math import factorial
n = int(input())

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end = " ")

print()