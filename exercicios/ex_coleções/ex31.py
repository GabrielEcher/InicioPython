"""
Ler duas listas de 10 números criar um vetor que seja a uniao entre os 2,
sem numeros repetidos
"""

lista1 = []
lista2 = []
count_l1 = 1
count_l2 = 1

for n in range(1, 11):
    ent_l1 = int(input(f"Digite os valores para a primeira lista {count_l1}/10:\n"))
    lista1.append(ent_l1)
    count_l1 += 1
    
for n in range(1, 11):
    ent_l2 = int(input(f"Digite os valores para a segunda lista {count_l2}/10:\n"))
    lista2.append(ent_l2)
    count_l2 += 1
    
uniao_listas = list(set(lista1).union(lista2))
print(f"A união das duas listas é:\n{uniao_listas}")