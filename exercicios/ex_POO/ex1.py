"""
Crie uma classe para representar uma pessoa com os atributos privados
de nome idade e altura. Crie métodos publicos necessarios para imprimir os dados de uma pessoa

"""

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    
    def set_nome(self, nome):
        self.__nome = nome        
    
    def get_nome(self):
        return self.__nome
    
    
    def set_idade(self, idade):
        self.__idade = idade
        
    def get_idade(self):
        return self.__idade
    
    
    def set_altura(self, altura):
        self.__altura = altura
        
    def get_altura(self):
        return self.__altura


    def get_all(self):
        return f'NOME: {self.__nome} \
                 IDADE: {self.__idade} \
                 ALTURA: {self.__altura}'
                 
    
pessoa = Pessoa(input('DIGITE O NOME: '), int(input('DIGITE A IDADE: ')), float(input('DIGITE A ALTURA: ')))

print(pessoa.get_all())
         
