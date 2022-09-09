"""
Faça uma matriz 3x3, e calcule a soma dos elementos que estão acima da 
diagonal principal
"""

import random

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(random.randint(0, 20))
            
def matriz3x3(matriz):
    for linha in range(3):
        for coluna in range(3):
            print(f"{[matriz[linha][coluna]]}", end="")
        print()
    soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
    return soma
 
print(matriz3x3(matriz))
  

    


matriz3x3(matriz)