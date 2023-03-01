"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela

"""

notas = []

for i in range(4):
    notas.append(float(input('Nota' + str(i+1) + ': ')))
    
soma = sum(notas)

media = soma / len(notas)

print(f"Notas do ano: {notas}")
print(f"Média das notas: {media}")