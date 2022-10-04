"""
Erros mais comuns em python

É importante prestar atenção e ler as saídas de erros geradas pela execução
do código

Erros mais comuns

SyntaxError -> Ocorre quando é encontrado um erro de síntaxe, algo que o python
não reconhece como parte da linguagem

Exemplos SyntaxError

a) def funcao:
    print('G')

b) None = 1

Exemplos NameError -> Ocorre quando uma variável ou função não foi definida

a) print(geek)

b) a = 1

if a < 1:
    msg = 'dakdaçdkl'
    
print(msg)

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a) print(len(5))

b) print('sda' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo
de dado indexado utilizando um indice invalido

Exemplos IndexError

a) lista = ['Gabi']
print(lista[0][122])

ValueError -> Ocorre quando uma função/operação built-in recebe um argumento
com tipo correto mas valor inapropriado

Exemplos ValueError

print(int('Geek'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que 
não existe

a) Exemplos KeyError

dic = {}
print(dic['gabi'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função

Exemplos AttributeError

tupla = (11, 2, 33)

print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos a identação do python 

Exemplos: IdentationError

a) def nova():
            print('dlsajdl')
"""

# IndentationError 







