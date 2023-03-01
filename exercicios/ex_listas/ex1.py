"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

lista = []

print("Informe os 5 números inteiros")

for i in range(5):
    lista.append(input('Número' + str(i+1) + ': '))

print(lista)