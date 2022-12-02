"""
POO - Atributos

Atributos -> Representam as características do objeto, conseguimos representar
computacionalmente os estados de um objeto

Em python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos

# Atributos de Instância: São atributos declarados dentro do método construtor.

#OBS: Método construtor: É um método especial utilizado para a construção do objeto.

Em Python por convenção, ficou estabelecido que, todo atributo de uma classe é publico, 
ou seja pode ser acessado em todo o projeto.
Caso eu queira demonstrar que determinado atributo deve ser tratado como privado, ou seja
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se
__ duplo no inicio de seu nome.

# Atributos de instância:

- Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos

# Isso é apenas uma convenção, ou seja a linguagem não vai impedir que façamos acesso
# aos atributos sinalizados como privados fora da classe

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email) # AtributeError

print(user._Acesso__senha) # Temos acesso. Mas não deveriamos fazer esse acesso (Name Mangling)

user.mostra_email()

# Atributos de Classe



# Atributos de classes, são atributos que são declarados diretamente na classe, ou seja fora do construtor
# Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe.
# Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de
# instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo

# Refatorar a classe produto

class Produto:
    
    # Atributo de classse
    imposto = 1.05 # 0.05% de imposto
    contador = 0
    
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
        
        
p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'VideoGame', 4000) 

print(p1.valor)  # Acesso possível mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível mas incorreto de um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classse


print(p1.id)
print(p2.id)
"""


# Classes com atributo de instância publico
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
        
        
class ContaCorrente:
    
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        
class Produto:
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
        
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha
    
    def mostra_email(self):
        print(self.__senha)
    
    def mostra_email(self):
        print(self.__email)





# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução

# OBS: O atributo dinâmico será exclusivo da instância que o criou.


class Produto:
    
    # Atributo de classse
    imposto = 1.05 # 0.05% de imposto
    contador = 0
    
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
        
        
p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'

print(f'PRODUTO: {p2.nome},\nDescrição: {p2.descricao}, \nValor: {p2.valor}, \nPeso: {p2.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso # Deleta

print(p1.__dict__)
print(p2.__dict__)