"""
Funções com retorno


numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f"Retorno de pop: {ret_pop}")

ret_pr = print(numeros)

print(f"Retorno de print: {ret_pr}")


OBS: Em Python, quando uma função nao retorna nenhum valor, o retorno é None

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(ret) #NONE / NÃO RETORNA A FUNÇÃO SÓ IMPRIME

OBS: O return faz a função retornar o valor

OBS: Não precisamos criar uma variavel para receber o retorno de uma função
podemos passar a execução da função para o print ou para outras funções

#Refatorando a função para ela retornar o valor

def quadrado_de_7():
    return 7 * 7

print(f"Retorno:{quadrado_de_7()}") 

#Refatorando a primeira função

def diz_oi():
    return 'OI'

print(diz_oi())


alguem = 'Gabi'

print(diz_oi() + alguem)


OBS: Sobre a palavra return

1 - Finaliza a função, ou seja, ela sai da execução da função;

#Exemplo 1 - #APÓS O RETURN NADA É EXECUTADO

def diz_oi():
    return
    print('Executando depois do return...')
2 - Podemos ter em uma função, diferentes returns;

#Exemplo 2

def nova_funcao():
    var = False
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'

print(nova_funcao())

3 - Podemos, em uma função retornar qualquer tipo de dado e até mesmo múltiplos

#Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4) #Desempacota a Tuple

print(outra_funcao()) #Retorna Tuple
valores;


# Função jogar a moeda

from random import random

def joga_moeda():
    #Gera um número pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

#Codificação desnecessária nas funções;

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    #ELSE DESNECESSÁRIO POIS EXISTEM APENAS 2 POSSIBILIDADES
    return False
    
print(eh_impar())

"""



