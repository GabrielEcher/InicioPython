"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados dos dois outros vetores.
"""

lista1 = []
lista2 = []
lista_intercalada = []

while len(lista1) < 10 and len(lista2) < 10:
    entrada_l1 = int(input("Digite números inteiros para a primeira lista: "))
    entrada_l2 = int(input("Digite números inteiros para a segunda lista: "))
    lista1.append(entrada_l1)
    lista2.append(entrada_l2)
    
lista_intercalada.extend(lista1)
lista_intercalada.extend(lista2)

print(f'Lista com os 10 elementos das duas listas juntos:\n{lista_intercalada}')

print(len(lista_intercalada))