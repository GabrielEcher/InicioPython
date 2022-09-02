"""
Programa que preencha um vetor de tamanho 100 com os 100 primeiros numeros que não são 
multiplos de 7 ou que terminam em 7
"""


vetor7 = []
n = 1

while len(vetor7) < 100:
    if n % 7 != 0 and n % 10 != 7:
        vetor7.append(n)
    n += 1
print(vetor7)
        