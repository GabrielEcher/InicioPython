"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
import numpy
vetor = []

for i in range(5):
    vetor.append(float(input("Digite o " + str(i+1) +"º valor: ")))
    
mult = numpy.prod(vetor)
soma = sum(vetor)

print(f'Lista: {vetor}')
print(f'Multiplicação dos valores do vetor:\n{mult:.0f}')
print(f'Soma dos valores da lista:\n{soma:.0f}')