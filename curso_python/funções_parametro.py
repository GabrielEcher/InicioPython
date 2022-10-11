"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processadas dentro da mesma;

Se a gente pensar em um programa qualquer temos:

entrada -> processamento -> saída

Se pensarmos em função algumas:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado_de_7(numero):
    #return numero * numero
    return numero ** 2

print(quadrado_de_7(7))
print(quadrado_de_7(8))
print(quadrado_de_7(2))
print(quadrado_de_7(3))

#Refatorando a função

def cantar_parabens(aniversariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print(f"Viva o {aniversariante}")

cantar_parabens('Gabriel')

# Funções podem ter n parâmetros de entrada, podemos receber quantos
# parâmetros forem necessário, separados por vírgula

# Exemplos

def soma(a, b):
    return a + b
print(soma(15, 30))


def multiplica(num1, num2):
    return num1 * num2
print(multiplica(2, 9))


def outra(num1, b, msg):
    return(num1 + b) * msg
print(outra(3, 2, "Gabriel"))
print(outra(3, 2, "Echer"))


# OBS: Se for informado um número errado de parâmetro ou argumento terá type error
# Seja passando argumentos a mais ou a menos


# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"

print(nome_completo('Gabriel', 'Echer'))

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;
# A ordem dos parâmetros importa

#Argumentos nomeados (Keyword Arguments)
# Caso utilizarmos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem.

nome = 'Gabriel'
sobrenome = 'Echer'

print(nome_completo(nome='Gabriel', sobrenome='Echer'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Defante', nome='Diogo'))


# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total
    
lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
"""

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':   
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
