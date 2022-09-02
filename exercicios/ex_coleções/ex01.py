"""
Faça um programa que possua um vetor denominado A que armazene 6 númeors
inteiros, deve executar os seguintes passos

1 - atribuir os valores ao vetor: 1, 0, 5, -2, -5, 7
2 - Armazenar em uma variável inteira a soma entre os valores A[0]
A[1] e A[5] do vetor e mostrar na tela essa soma
3 - Modificar o vetor na posição 4, atribuindo a esta posição o valor 100
4 - Mostrar na tela cada valor do vetor A, um em cada linha
"""

A = [1, 0, 5, -2, 7]
print(A)

soma = (sum(A))
print(soma)

A[4] = 100
print(A)