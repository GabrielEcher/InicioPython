"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
no sistema

Em python dividimos os métodos em 2 grupos: Métodos de instância e Métodos de Classe

# Métodos de Instância

# O método __init__ é um método especial chamado de construtor, sua função é construir o objeto a partir da classe


p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(20))       

print(Produto.desconto(p1, 40)) #self, desconto

user1 = Usuario('Gabriel', 'Echer', 'gabrielecher14@gmail.com', '270504')
user2 = Usuario('Ana Luiza', 'Toigo', 'analuiza@gmail.com', '2808005')

#print(user1.nome_completo())
#print(user2.nome_completo())

print(f'Senha User1: {user1._Usuario__senha}')
print(f'Senha User1: {user2._Usuario__senha}')

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirmacao = input('Confirme sua senha: ')

if senha == confirmacao:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(42)
    
    
print('Usuário criado com sucesso')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')
    
print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso errado

# Métodos de classe em Python são conhecidos como métodos estáticos em outras linguagens

# Métodos de Classe

user = Usuario('Gabriel', 'Echer', 'gabrielecher14@gmail.com', '270504')

Usuario.conta_usuarios() # Forma correta

"""

class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
        
class ContaCorrente:
    
    contador = 4999
    
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero
        
class Produto:
    
    contador = 0
    
    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    
    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp
       
class Usuario:
    
    contador = 0
    
    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')
    
    @staticmethod
    def definicao():
        return 'UX23240'
    
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16) # round - embaralhamento da senha, salt_size - tamanho da senha
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario__()}')
        
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'   
    
    def checa_senha(self, senha): # Verifica se a senha informada é igual a senha salva no banco
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario__(self):
        return self.__email.split('@')[0] # Separa o @ do email retornando uma lista com as duas partes do email separadas
    
    
user = Usuario('Gabriel', 'Echer', 'gabrielecher14@gmail.com', '12345')

# Método Estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('GABRI', 'HED', 'gabi@gmail.com', '3123809')

print(user.contador)

print(user.definicao())