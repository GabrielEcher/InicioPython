"""
Fazer uma interseção entre duas listas de 10, criar um vetor para 
a interseção sem números repetidos, apenas os números que estão em ambos
os vetores
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

print("Aqui estão as duas listas:\n")
print(lista1)
print(lista2)

vetor_interseccao = list(set(lista1).intersection(lista2))
print(f"A intersecção das duas listas é:\n{vetor_interseccao}")