"""
POO - Polimorfismo


"""

class Animal(object):
    
    def __init__(self, nome):
        self.__nome = nome
        
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
    
    def comer(self):
        print(f'{self.__nome} está comendo...')
        


class Cachorro(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self._Animal__nome} faz auauuau')

class Gato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        print(f'{self._Animal__nome} faz miau')
        
class Rato(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo')

# Teste

gato = Gato('ivar')
gato.comer()
gato.falar()

dog = Cachorro('dog')
dog.comer()
dog.falar()

mickey = Rato('mickey')
mickey.comer()
mickey.falar()