"""
Criando um acesso a uma conta bancária
"""

class Conta:
    
    def __init__(self, num_conta, cpf, senha, capital, limite):
        self.num_conta = 145989
        self.cpf = 0-3505631019
        self.senha = 270504
        self.capital = 1500
        self.limite = 3000
    
    def VisualizacaoConta(self):
        print('DADOS DA CONTA:')
        print(f'NÚMERO DA CONTA:{self.num_conta}')
        print("-----------------------------------")
        print(f'CPF: {self.cpf}\nSALDO: R${self.capital}\nLIMITE ATUAL: R${self.limite}')
        
    def login():
        num = input("DIGITE O NÚMERO DA CONTA: ")
        cpff = int(input("DIGITE O CPF: "))
        passw = int(input("DIGITE A SENHA DE ACESSO: "))
        if num != Conta.cpf:
            print("CPF INVÁLIDO PARA CONTA INFORMADA!")
    

Conta.login()    
        
        

