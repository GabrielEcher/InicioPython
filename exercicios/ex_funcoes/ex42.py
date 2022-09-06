"""
Função que receba um vetor e retorne a média deles
"""

lista = [12, 15, 3, 4, 66, 98, 10, 120, 32]

def media_lista(lista):
    soma = sum(lista)
    qnt = len(lista)
    media = soma / qnt
    return print(f'A média da lista é:{media}')

media_lista(lista)
