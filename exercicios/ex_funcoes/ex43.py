"""
Função que receba um vetor e o preencha com números inteiros aleatórios sem repetição
"""
import random


tamanho = int(input("Digite quantos valores a lista deverá conter: "))
vetor = []

def preencher_vetor(vetor):
    while tamanho > len(vetor):
        vetor = random.sample(range(1, 101), tamanho)
        return f'{vetor}'
        
    
print(preencher_vetor(vetor))

        