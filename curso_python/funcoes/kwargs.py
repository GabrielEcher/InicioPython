"""
**kwargs

Diferente do *args que coloca os valores extras em uma tuple,
o **kwargs exige que utilizamos parâmetros nomeados, e transforma
estes parametros extras em um dicionário

# Exemplo

def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    

cores_fav(marcos='verde', joao='azul', sergio='amarelo')


# OBS: Os params *args **kwargs não são obrigatórios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek'
    return 'Não tenho certeza de quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek= 'especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parametros obrigatorios;
- *args
- Parametros Default (não obrigatorios);
- **kwargs

def my_func(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome}, tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')

my_func(18, 'Gabriel')
my_func(50, 'Fernando', 12, 13, 14, solteiro=True)
my_func(34, 'Silvio', eu='Não', voce='vai')
my_func(11, 'DUDA', 9, 2, java=False, python=True)

# Entenda porque é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros:
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome ='University', cargo='Instrutor'))

# Função com a ordem incorreta de parâmetros:
def mostra_info(a, b,  instrutor='Geek', *args, **kwargs,):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome ='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Gabriel', 'sobrenome': 'Echer'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)
    
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

#OBS: Os nomes da chave em um dicionario devem ser o mesmo dos parametros da função
"""





