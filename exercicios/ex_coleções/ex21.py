"""
Programa que recebe 2 vetores A e B do usuário, e cria um vetor C, calculando C = A - B, imprimir na tela o
o valor do vetor C
"""
import enum
import random

vetor_A = []
vetor_B = []
vetor_C = []

for _ in range(10):
    vetor_A.append(int(random.randint(0, 100)))
    vetor_B.append(int(random.randint(0, 100)))

for i, _ in enumerate(vetor_A):
    n = vetor_A[i] - vetor_B[i]
    vetor_C.append(n)

print(vetor_A)
print(vetor_B)
print(vetor_C)