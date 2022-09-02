"""
Leia 10 valores númericos e ordene por ordem crescente, ordenar assim que for digitado e 
mostrar os valores em ordem
"""

lista = []
count = 1

for n in range(1, 11):
    ent_user = int(input(f"Digite 10 valores {count}/10:\n"))
    count += 1
    lista.append(ent_user)
    lista.sort()

print(f"A lista digitada na ordem crescente fica:\n{lista}")
