"""
Utilizamos esses blocos para tratar erros que podem ocorrer no nosso código, 
Prevenindo que o programa pare de funcionar e o usuaário receba mensagens de erros
inesperados
try:
    //execução problema
except:
    //oque deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico
try:
    print(dadadasd3)
except:
    print('Deu problema!!') # Alternativa em caso de erro

# OBS: O ideal é tratar erros de forma específica, no caso dos erros genéricos

# Exemplo 2 - Tratando um erro especifico
try:
    print(dadadasd3)
except TypeError: # É preciso ser executado o tratamento de erro correto
    print('Deu problema!!') # Alternativa em caso de erro

# Exemplo 3 - Tratando um erro especifico com detalhes do erro
try:
    print(dadadasd3)
except NameError as ERR: 
    print(f'A aplicação gerou o seguinte erro: {ERR}') 

# Podemos tratar diversos tipos de erro em um mesmo bloco try 

try:
    print('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Gabi'}

print(pega_valor(dic, 'game'))