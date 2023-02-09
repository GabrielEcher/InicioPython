"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

lista = []
qtd = 3

for i in range(qtd):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    

lista.sort(reverse= True) #Ordena os elementos e depois faz o reverso para obter o decrescente

print(lista)