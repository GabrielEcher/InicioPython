"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> Meios de comunicações entre os serviços fornecidos por empresas (YT, Twitter, etc) e terceiros
(desenvolvedores)

import json

ret = json.dumps(['Produto', {'Playstation 4': ('2TB', 'Novo', '220v', 2340)}])

print(type(ret))

print(ret) # JSON faz a formatação para aspas duplas

import json

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
    
gatao = Gato('Joao', 'Vira-lata')

print(gatao.__dict__)

ret = json.dumps(gatao.__dict__)

print(ret)


# Integrando o JSON com o Pickle

# pip install jsonpickle

import jsonpickle

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
    
gatao = Gato('Joao', 'Vira-lata')

ret = jsonpickle.encode(gatao)

print(ret)

# Escrevendo o arquivo JSONPickle

import jsonpickle

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
    
gatao = Gato('Joao', 'Vira-lata')

with open('gatao.json', 'w') as arquivo:
    ret = jsonpickle.encode(gatao)
    arquivo.write(ret)
"""
# Lendo o arquivo json/pickle

import jsonpickle

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
    
gatao = Gato('Joao', 'Vira-lata')

with open('gatao.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
