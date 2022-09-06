"""
Função que recebe um vetor e retorna quantos valores pares ele possui
"""

lista = [12, 15, 3, 4, 66, 98, 10, 120, 32]

def verif_pares(lista):
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1           
    return f'A lista possui {pares} números pares'

print(verif_pares(lista))
    