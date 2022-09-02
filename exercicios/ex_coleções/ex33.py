"""
Programa que lê um vetor de 15 posições e o compacte, ou seja
elimine as posições com valor zero. Para isso, todos os elementos
à frente do valor zero precisam ser movidos uma posição para trás 
no vetor
"""

lista = []
count = 1


for n in range(1, 16):
    ent_l = int(input(f"Digite 15 números para a lista {count}/15:\n"))
    count += 1
    lista.append(ent_l)
    if ent_l == 0:
        lista.pop()

print(lista)