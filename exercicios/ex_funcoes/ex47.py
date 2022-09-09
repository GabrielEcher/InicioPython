"""
Função que recebe uma matriz 4x4 e informe quantos números maiores que 10 possem nela
"""
import random
 
 
def matriz4x4(*args):
    count = 0
 
    for lin in range(len(args)):
        for col in range(len(args)):
            if args[lin][col] > 10:
                count += 1
 
    return f'Na matriz existem {count} valores maiores que 10'
 
 
matriz = [[], [], [], []]
 
for linha in range(4):
    for coluna in range(4):
        matriz[linha].append(random.randint(0, 20))
 
for l in range(4):
    for c in range(4):
        print(f'[{matriz[l][c]:^5}]', end=' ')
 
    print()
 
print(matriz4x4(*matriz))