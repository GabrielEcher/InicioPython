"""
Ler 10 números inteiros e armazenar em um vetor = v, criar dois novos vetores v1 e v2, 
adicionar no v1 os números pares do v e no v2 os números impares do v, no final escrever
os indices utilizados do v1 e do v2
"""

v = []
v1 = []
v2 = []
count = 1
while len(v) < 10:
    ent_v = int(input(f"Digite números para armazenar na lista {count}/10:\n"))
    count += 1
    v.append(ent_v)
print(f"Lista principal:\n{v}\n")

for n in v:
    if n % 2 == 0:
        v1.append(n)
    else:
        v2.append(n)
        
print(f"Lista de números pares da lista principal:\n{v1}")
print(f"Quantidade de números pares na lista:{(len(v1))}\n")


print(f"Lista de números ímpares da lista principal:\n{v2}")
print(f"Quantidade de números ímpares na lista:{(len(v2))}\n")    