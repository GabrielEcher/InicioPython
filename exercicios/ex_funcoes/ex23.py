"""
Função que gera um triangulo lateral de altura 2*n-1 e n largura
"""
num = int(input("Digite um valor: "))

def triangulo_lateral(n):
    linha = ''
    for i in range(2 * n - 1):   
        if i < n:
            linha = linha + '*'*(i+1) + '\n'
        else:
            linha = linha + (2*n - (i+1)) * '*' + '\n'
    return linha

print(triangulo_lateral(num))