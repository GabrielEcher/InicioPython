"""
Default Parameters

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print("CONTEUDO")
print()

# Exemplo de função onde a passagem de parâmetro é obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())


# Parametro padrao 

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 3)) # Eleva à potencia informada pelo usuario

print(exponencial(3)) # Por padrão eleve ao quadrado 

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro número
# E será calculado o quadrado deste número
# Se o usuário passar 2 argumentos, será calculado normal

# OBS: Em funções python, os parametros default devem sempre estar ao final da declaração

def teste(num=2, potencia)
    #ERRO 

def soma(num1, num2):
    return num1 + num2

print(soma(5, 10))
print(soma()) # Type ERROR
print(soma(4)) # Type ERROR

# Exemplo mais complexo

def mostra_informação(nome='Gabriel', instrutor=False):
    if nome == 'Gabriel' and instrutor:
        return 'Bem vindo Gabriel'
    elif nome == 'Gabriel':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informação())
print(mostra_informação(instrutor=True)) # Se passar apenas True o valor será atribuido ao primeiro parametro
print(mostra_informação('Joao'))
print(mostra_informação(nome='Celso'))

# Porque utilizar parametros com valor default?

# - Permite ser mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default nos params?

- Qualquer tipo:
    - Números, strings, floats, booleans, etc

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais


instrutor = 'Geek' #Variavel Global

def diz_oi():
    instrutor = 'Python' #Variável local
    return f"Oi {instrutor}"

print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia

def diz_oi():
    prof = 'Geek' # Variavel local
    return f'Olá {prof}'

print(diz_oi())
print(prof) #ERROR

# Se puder evitar variaveis globais evite

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError - variavel nao iniciada
    return total

print(incrementa())

# METODO FUNCIONAL

total = 0

def incrementa(): 
    global total # Avisando que teremos a preferencia pela variavel global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial
# de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador # Dizemos que queremos utilizar a variavel da função de cima
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
print(fora())

print(dentro()) #DESCONHECIDA #NAME ERROR






