"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def positivo_negativo():
    valor = int(input('Digite o valor: '))
    arg = valor
    if arg > 0:
        return 'P'
    return 'N'


print(positivo_negativo())