"""
Higher Order Functions - HOF

Significado -> 

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que 
retornam outras funções como resultado ou  mesmo que podemos passar funções como argumentos
para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas

- Em python as funções são Cidadões de primeira classse, First Class Citizen

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuit(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Teste das funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuit))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))
]
# Nested Functions - Funções Aninhadas


Em python podemos ter também funções dentro de funções, que são conhecidas por Nested Funtions
ou também Inner functions (funções internas) 


from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto de tu '))
    return humor() + pessoa 

# Teste

print(cumprimento('Bepi'))

# Retornando funções de outras funções

from random import choice

def risada():
    def rir():
        return choice(('hahhaha', 'kkkkkkkkkkkk', 'jajaja'))
    return rir

# Teste

rindo = risada()
print(rindo())
"""

# Inner Functions podem acessar o escopo de funções mais externas


from random import choice

def risada2(pessoa):
    def dar_risada():
        r = choice(('ahaha', 'kkkkk', 'jajaja'))
        return f'{r} {pessoa}'
    return dar_risada

rindo = risada2('Gabriel ')

print(rindo())
print(rindo())
print(rindo())

