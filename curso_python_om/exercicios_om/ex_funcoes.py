"""Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável."""


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return f'Resultado da multiplicação {total}'
    
mult = multiplica(3912, 321, 29, 312, 2)
#print(mult)


# Crie uma função que fala se um numero é par ou impar
# Retorne se o numero e par ou impar

def par_impar(numero):
    if numero % 2 == 0:
        return(f'O {numero} é par')
    return(f'O {numero} é impar')
        
print(par_impar(12))