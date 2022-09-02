"""
Leia um vetor de 10 posições, contar e escrever quantos valores pares ele possui
"""

lista1 = []
lista_pares = []
qtd = 0

for n in range(10):
    entrada = int((input("Digite os números da lista abaixo:\n")))
    lista1.append(entrada)
print(f"A lista que você escreveu é:\n{lista1}")

for valor in lista1:
    if valor % 2 == 0:
        lista_pares.append(valor)
    qtd += 1

print(f"Os números pares da lista são:\n{lista_pares}")
print(f"A lista acima tem: {qtd} números pares")



















