"""
POO - Heranca (Inheritance)

A ideia de herança é a de reaproveitar código. Mas também extender nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe, que passa a
herdar atributos e métodos da classe herdada

Existe alguma entidade generica o suficiente para encapsular os atributos e metodos comuns a outras
entidades?


OBS: Quando uma classe de outra classe, ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;
    
Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Especifica;


Sobrescrita de metodos, ocorre quando reescrevemos um método presente na classe em classes filhas

"""
class Pessoa:
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    
class Cliente(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    def nome_completo(self):
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa.__nome}'
    
# Sobrescrita de Métodos (Overriding)


cliente1 = Cliente('Gabriel', 'Echer', '03505631019', 50000)
funcionario1 = Funcionario('Joao', 'Gomes', '39021320193', 1234)


print(funcionario1.nome_completo())