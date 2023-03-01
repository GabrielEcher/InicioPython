"""
Try, Except, Else, Finally
# Dica de quando tratar um código:
- TODA ENTRADA DE DADOS DO DEVE SER TRATADA!
## A FUNÇÃO DO USUÁRIO É DESTRUIR SEU SISTEMA ## 
# Else:
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')   
else:
    print(f'Você digitou: {num}')
# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido!')
else:
    print(f'Você digitou o número: {num}')
finally:
    print('Executando o finally')
    
# OBS: O bloco finally é sempre executado. Independentemente se houve exceção ou não

# O finally é utilizado geralmente para fechar ou desalocar recursos

# Exemplo mais complexo ERRADO
def dividir(a, b):
    return a / b
num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser númerico')
try:
    print(dividir(num1, num2))
except ValueError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'
           
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# Exemplo mais complexo (semi-genérico)

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema:'
           
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
"""