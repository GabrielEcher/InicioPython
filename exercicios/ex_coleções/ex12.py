"""
Programa que lê 5 valores de um vetor, e printa o maior o menor e a media de todos os valores
"""

lista = []
count = 1

for n in range(5):
    ent_lista = int(input(f"Digite os valores para lista - {count}/5:\n"))
    lista.append(ent_lista)
    count += 1

maxi = max(lista)
mini = min(lista)
media = sum(lista) / 5

print(f"O maior valor da lista é o:{maxi}")
print(f"O menor valor da lista é o:{mini}")
print(f"A média dos valores é:{media}")