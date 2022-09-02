"""
Programa que imprima na tela os valores negativos de um vetor e faça a soma dos números positivos
"""

numeros = []
pos, neg = 0, 0

for n in range(10):
    ent = int(input("Digite 10 números:\n"))
    numeros.append(ent)
for num in numeros:
    if num >= 0:
        pos += num  # += soma e atribuição de valor
    else:
        neg += 1

print(f"Números negativos na lista:{neg}")
print(f"Soma dos números positivos da lista:{pos}")