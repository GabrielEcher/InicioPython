"""
POO - Herança Multipla

Herança Multipla é a possibilidade de uma classe herdar de multiplas
classes

A herança multipla pode ser feita de duas maneiras:
 - Multiderivação Direta;
 - Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass
  
class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    
#OBS: Não importa se a derivação é direta ou indireta, a classe
que realizar a herança, herdará todos os atributos e métodos das superclasses

"""

class Animal:
    
    def __init__(self, nome):
        self.__nome = nome
        
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    

class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def nadar(self):
        return f'{self._Animal__nome} está nadando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'
    
class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{self._Animal__nome} está andando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'
    
class Pinguim(Aquatico, Terrestre, ):
    
    def __init__(self, nome):
        super().__init__(nome)   


# Teste

baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Betao')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())    # Method resolution order


# Objeto é instancia de...

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}') # TRUE
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}') # TRUE
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}') # TRUE
print(f'Tux é instancia de Object? {isinstance(tux, object)}') # TRUE
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}') # TRUE


