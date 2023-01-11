"""
POO - Properties

class Conta:
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
        
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
        
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
      
    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Gabriel', 2900, 5000)
conta2 = Conta('Ana', 2000, 3000)


soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos é: {soma}')
    
    
print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)
"""

class Conta:
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite    
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    @property
    def valor_total(self):
        return self.__saldo + self.__limite
    
    
    
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
        
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    

conta1 = Conta('Gabriel', 2900, 5000)
conta2 = Conta('Ana', 2000, 3000)   
    
    
soma = conta1.saldo + conta2.saldo
print(f'{soma}')

print(conta1.__dict__)
conta1.limite = 82382
print(conta1.__dict__)  
    
print(conta1.valor_total)
print(conta2.valor_total)