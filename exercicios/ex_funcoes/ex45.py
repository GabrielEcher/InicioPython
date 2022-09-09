"""
Função que calcula o desvio padrão de um vetor V contendo N números
"""
import numpy as np
import random

vetor = [random.randint(1, 20)for n in range(20)]

def desvio_padrao(vetor):
    print(np.std(vetor))
    
desvio_padrao(vetor)
