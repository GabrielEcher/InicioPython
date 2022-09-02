"""
Programa que verifica se na lista tem valores repetidos e imprime eles na tela
"""
lista = [1, 1, 23, 45, 56, 77, 77, 8, 100, 101, 101]
lista_n_rep = set(lista)
lista_v = []

for n in lista:
    if lista.count(n) > 1:
        lista_v.append(n)

print(f'Os valores repetidos são esses:{lista_v}')