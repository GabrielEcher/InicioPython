"""
Ler um vetor com 10 números reais, ordenar os elementos, e no final escrever
os elementos do vetor ordenado
"""

lista = []
count = 1

for n in range(10):
    ent_lista = float(input(f"Digite 10 valores para a lista {count}/10:\n"))
    lista.append(ent_lista)
    count += 1
    
print(f"Aqui está a lista formada:\n{lista}")

lista.sort()
print(f"Aqui está a lista ordenada:\n{lista}")
