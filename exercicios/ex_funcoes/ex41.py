"""
Função que recebe um vetor de inteiros e retorne o maior valor
"""

lista = [12, 15, 3, 4, 66, 98, 10, 120, 32]

def maior_lista(lista):
    for n in lista:
        maior = max(lista)
    print(f'O maior valor da lista é: {maior}')

maior_lista(lista)