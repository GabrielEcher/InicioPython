"""
Crie um programa que leia 10 números inteiros os armazene em uma lista, imprima-a, imprima o maior elemento e a posição
em que ele se encontra
"""

lista = []
count = 0

for n in range(10):
    ent = int(input(f"Digite os números para armazená-los na lista: {count}/10\n"))
    count += 1
    lista.append(ent)

print(f"A lista é:\n{lista}")

maior = max(lista)
print(f"O maior elemento da lista é:{maior}")

indice = lista.index(max(lista))
print(f"O indice em que o maior número se encontra é:{indice}")