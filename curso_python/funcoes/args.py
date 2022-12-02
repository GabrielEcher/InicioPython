"""
Entendendo o *args

- O *args é um parâmetro, como qualquer outro, isso significa que voce
poderá chamar de qualquer coisa, desde que começe com *

Exemplo:

*xis

Por convenção utilizamos o:

*args

Mas oque é o *args?

O parâmetro utilizado em uma função, coloca os valores extras informados como entrada
em  um tuple. Então desde já lembre-se que tuplas são imutáveis

# Exemplos args

#Modo não simplificado

#def soma_todos_numeros(*args):
    #total = 0
    #for numero in args:
        #total = total + numero
    #return sum(args)

# Modo simplificado

def soma_todos_numeros(nome, email, *args):
    return sum(args)  
    
print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Gabriel' in args and 'Echer' in args:
        return f'Bem-vindo usuário! '
    return 'Eu não tenho certeza de quem é você...'

print(verifica_info())
print(verifica_info(1, True, 'Gabriel', 'Echer'))
print(verifica_info(1, 'Gabriel', 3.14))

def soma(*args):
    print(args)
    return sum(args)

num = {1, 2, 3, 4, 5, 6, 7}

print(soma(*num)) # O asterisco serve para informar ao PY, que estamos passando uma coleção com argumento
# Desta forma ele desmpacotará os dados
# FUNCIONA PARA SET, TUPLE E LISTA
"""




