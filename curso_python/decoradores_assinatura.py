"""
Decorators com diferentes assinaturas

Utilizamos um padrão de projeto chamado Decorator Pattern


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# Testando

#print(saudacao('Gabriel'))

print(ordenar('Picanha', 'Batata frita'))

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

# Refatorando o código anterior com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# Testando

print(saudacao('Gabriel'))

print(ordenar('Picanha', 'Batata frita'))


@gritar
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
"""


# Decorator com argumentos

def verif_prim_arg(valor):
    def interna(funcao):
       def outra(*args, **kwargs):
           if args and args[0] != valor:
               return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
           return funcao(*args, **kwargs)
       return outra
    return interna

@verif_prim_arg('pizza')
def comida_favorita(*args):
    print(args)

@verif_prim_arg(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

#print(soma_dez(10, 12)) # 22

#print(soma_dez(1, 21)) # Valor incorreto o primeiro args tem que ser 10

print(comida_favorita('pizza', 'churrasco')) # Correto

print(comida_favorita('fruta', 'churrasco')) # Valor incorreto, pois o primeiro valor tem que ser pizza