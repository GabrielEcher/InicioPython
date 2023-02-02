"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

print('Iremos calcular a média das suas 4 notas bimestrais!')

def media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return f'A média dos 4 bimestres foi: {media}'

nota1 = int(input('INFORME A NOTA DO 1º BIMESTRE: '))
nota2 = int(input('INFORME A NOTA DO 2º BIMESTRE: '))
nota3 = int(input('INFORME A NOTA DO 3º BIMESTRE: '))
nota4 = int(input('INFORME A NOTA DO 4º BIMESTRE: '))

print(media(nota1, nota2, nota3, nota4))
