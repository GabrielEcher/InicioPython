"""
Utilizando Lambdas

São funções sem nome, ou seja funções anônimas

# Função em python:
def soma(a, b):
    return a + b

# Expressão lambda

lambda x: 3 * x + 1 # X é o parâmetro e o resto é a execução da função

# Como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# strip() remove os espaços do inicio e fim de uma string

um = lambda x: 3 * x + 1

dois = lambda x, y: (x * y) ** 3

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z) * 10

print(um(10))
print(dois(7, 9))
print(tres(5, 10, 15))

# SE PASSARMOS MAIS ARGUMENTOS DO QUE PARÂMETROS ESPERADOS TEREMOS TypeError

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradburry', 'Robert Heinlein', 'Arthur C. Clarke', 'Travis Scott']

# Ordenação pelo sobrenome

autores.sort(key=lambda sobrenome: sobrenome.split('  ')[-1].lower())

print(autores)
"""

# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5) # Declarando os valores de a, b, c

print(teste(1)) # Declarando o valor de x
print(teste(2))
print(teste(3))

# DECLARANDO DIRETO
print(geradora_funcao_quadratica(2, 3, 6)(2))
