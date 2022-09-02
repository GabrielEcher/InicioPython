"""
Programa que leia 6 números inteiros e mostre:
- números pares digitados
- a soma do números pares
- números impares
- a quantidade de números impares
"""

lista = []
pares = []
impares = []
count = 1

while len(lista) < 6:
    ent_l = int(input(f"Digite os números para a lista {count}/6:\n"))
    lista.append(ent_l)
    count += 1

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Números pares:\n{pares}")
print(f"A soma dos números pares: {(sum(pares))}\n")

print(f"Números impares:\n{impares}")
print(f"Quantidade de números impares: {(len(impares))}\n")


    