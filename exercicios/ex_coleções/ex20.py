"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um
vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares do 
primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
from random import random

vetor = []
vetor_impar = []
v = 0

for i in range(10):
    n = int(random() * 50)  # número randômico gerado entre [0, 50]
    if n % 2 == 1:
        vetor_impar.append(n)
    vetor.append(n)

print(f'Vetor: {vetor}')
print(f'Vetor ímpar: {vetor_impar}')

tamanho_impar = len(vetor_impar)

for i in range(10):
    if i < tamanho_impar:
        print(f' |{vetor[i]}|      |{vetor_impar[i]}|')
    else:
        print(f' |{vetor[i]}|')