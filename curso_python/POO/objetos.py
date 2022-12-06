"""
POO - Objetos

Objetos -> São instancias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua
representacao computacional, devemos poder criar quantos objetos foram necessários. Podemos pensar
nos objetos/instancias de uma classe como variaveis do tipo definido na classe

# Instancia de objetos

lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lampada está ligada? {lamp1.checa_lampada()}')

lamp1.ligar_desligar()

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Gabriel', 'Echer', 'gabrielecher14@gmail.com', '123456')
"""

class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True     

class ContaCorrente:
    
    contador = 4999
    
    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero
        self.__cliente = cliente
    
    def mostra_cliente(self):
        print(f'O nome do cliente é {self.__cliente._Cliente__nome}')

class Usuario:
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        
        
class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

cliente1 = Cliente('Gabriel', '03505631019')

cc = ContaCorrente(5000, 10000, cliente1)

print(cc.mostra_cliente())