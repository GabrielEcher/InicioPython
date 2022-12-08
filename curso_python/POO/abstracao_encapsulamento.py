"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
classes

Encapsular -> Cápsula

Exemplo acessando elementos privados fora da classe

instancia._Pessoa__nome (não recomendavel)

# Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário

# Testando

conta1 = Conta('Gabriel', 1500, 2000)

print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print(conta1.numero)

conta1.extrato()
"""

class Conta:
    
    contador = 400
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
            
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')
            
    def tranferir(self, valor, conta_destino):
        
        if self.__saldo < valor:
            print('TRANSFERÊNCIA NEGADA: Saldo menor que o valor de transferência')
        
        elif valor < 0.1:
            print('O valor de tranferência precisa ser maior que 1')
            
        elif self.__saldo >= valor:
            if valor > 1000:
                self.__saldo -= 15
                conta_destino.__saldo += valor 
    
       
               



conta1 = Conta('Gabriel', 3000, 2000)
conta1.extrato()

conta2 = Conta('Fernando', 300, 10000)
conta2.extrato()


conta1.tranferir(1500, conta2)

conta1.extrato()
conta2.extrato()
