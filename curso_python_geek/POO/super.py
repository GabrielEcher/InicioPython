"""
O método super()

Se refere à super classe.

"""

class Animal:
    
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
        
    def faz_som(self, som):
        print(f'O {self.__nome} faz o som: {som}')
    
class Gato(Animal):
    
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca
        

mima = Gato('MIMA', 'Felino', 'Vira-Lata')

mima.faz_som('miau')