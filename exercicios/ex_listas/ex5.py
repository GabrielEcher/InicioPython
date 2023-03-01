"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

lista = []
par = []
impar = []
numero = 0

for i in range(20):
    lista.append(int(input('Número ' + str(i+1) + ': ')))
    numero = lista[i]

    if (numero % 2 == 0):
        par.append(numero)
    else:
        impar.append(numero)
    
print(lista)
print(f'Lista dos números pares:\n{par}')
print(f'Lista dos números ímpares:\n{impar}')