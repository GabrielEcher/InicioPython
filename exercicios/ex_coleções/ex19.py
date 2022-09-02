"""
Faça com que um vetor preenchido em 50 com o seguinte valor (i+5*i)%(i+1), sendo i a posição do elemento no vetor
"""

lista = []

for i in range(0, 50):
    a = (i+5*i) % (i+1)
    lista.append(a)

print(lista)