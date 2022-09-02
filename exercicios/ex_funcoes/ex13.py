"""
Função que recebe 2 valores númericos e um símbolo.
Se o símbolo for + = adição
- = subtração 
/ divisão
* multiplicação
"""


print("CALCULO DOS VALORES\n")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
simb = str(input("Digite:\n+ para soma\n- para subtração\nx para multiplicação\n / para divisão\n"))

def calculo(num1, num2, simb):
    if simb == '+':
        soma = num1 + num2
        return f'Soma dos valores: {soma}'
    elif simb == '-':
        subtr = num1 - num2
        return f'A subtração dos valores: {subtr}'
    elif simb == 'x':
        mult = num1 * num2
        return f'A multiplicação dos valores é: {mult}'
    elif simb == '/':
        divs = num1 / num2
        return f'A divisão dos valores é: {divs}'
    else:
        return 'VALORES INVÁLIDOS'

print(calculo(num1, num2, simb))
        
    