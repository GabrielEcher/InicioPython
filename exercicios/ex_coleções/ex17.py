"""
Ler um vetor de 10 posições e atribuir o valor zero para os números negativos
"""

lista = []
count = 0

for n in range(10):
    ent_lista = int(input(f"Digite os valores para o vetor - {count}/10\n"))
    lista.append(ent_lista)
    count += 1
    
for num, valor in enumerate(lista):
    if valor < 0:
        lista[num] = 0

print("Os valores negativos foram substituídos pelo valor 0")        
print(lista)        