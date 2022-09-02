"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia dois valores x e y correspondentes a duas posições
no vetor, o programa deverá escrever a soma do x e y
"""

lista = []
count = 1

for n in range(8):
    ent = int(input(f"Digite 8 números - {count}/8: "))
    lista.append(ent)
    count += 1

print(lista)

x = int(input("Digite a posição do primeiro valor que deseja somar: "))
y = int(input("Digite a posição do segundo valor que deseja somar: "))

soma = lista[x] + lista[y]

print(f"A soma dos valores é: {soma}")
