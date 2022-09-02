"""
Programa que leia 20 valores de um vetor, e remover os valores que são iguais
"""

lista = []
count = 0

for n in range(20):
    lista.append(int(input(f"Digite os valores - {count}/20:\n ")))
    print(lista)
    count += 1

n_repetidos = set(lista)
print(n_repetidos)