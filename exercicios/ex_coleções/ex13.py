"""
Programa que lê 5 valores e mostra a posição do maior e do menor valor
"""

lista = []
count = 0

for n in range(5):
    ent_lista = int(input(f"Digite os valores {count}/5\n"))
    lista.append(ent_lista)
    count += 1

indice_ma = lista.index(max(lista))
indice_me = lista.index(min(lista))

print(f"A posição do maior número é:{indice_ma}")
print(f"A posição do menor número é:{indice_me}")