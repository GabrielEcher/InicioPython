"""
Módulo Collections - Ordered dict

#Em um dicionario a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

É um dicionario que nos garante a ordem de inserção dos elementos

#PRECISO IMPORTAR

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""

from collections import OrderedDict

#Diferença entre Dict e Ordered Dict

#Dicts comund

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  #True -> Já que a ordem dos elementos não importa para o Dict

#Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  #False -> Já que a ordem dos elementos importa para o Ordered Dict