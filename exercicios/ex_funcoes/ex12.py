"""
Função que recebe um número inteiro maior que zero e retorne a soma de todos os
seus algarismos, se o número lido não for maior que zero o programa terminará com 
a mensagem "Número inválido"
"""

num = int(input("Digite um número inteiro maior que zero: "))

def soma_algarismos(num):
    if num > 0:
        soma = 0 
        for i in str(num):
            soma += int(i)
        return soma
    else:
        return 'Número inválido'

print(soma_algarismos(num))   
        
    