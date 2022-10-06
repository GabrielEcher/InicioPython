"""
Modulo ranodm e oque são modulos?

RANDOM -> Possui várias funções para geração de números pseudo-aleatórios


# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Não recomendado

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes
# e propriedades que ele tiver ficarão disponíveis em memória


# Forma 2 - RECOMENDADA

# importando uma função específica

from random import random


for i in range(10000):
    print(random())

# uniform() -> Gerar um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(1, 10)) #ULTIMO NUMERO NÃO É INCLUÍDO (não inteiros)

# randint() -> Gera valores pseudo-aleatórios inteiros entre os valores estabelecidos

# Gerador de apostas para a megasena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')


from random import choice
# choice() -> Mostra um valor aleatório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle


cartas = ['k', '2', '3', 'J', '4', '5', '6']
print(cartas)

shuffle(cartas)
print(cartas)



