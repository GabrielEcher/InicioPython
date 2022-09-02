"""
Crie um programa que leia 6 valores de uma lista e imprima-os na ordem inversa
"""

lista = []
count = 0

for n in range(6):
    val = int(input(f"Digite os números para armazenar na lista {count}/6 \n"))
    count += 1
    lista.append(val)

print(f"A lista digitada é:\n {lista}")
inverso = lista.reverse()
print(f"A lista em ordem inversa fica:\n {lista}")