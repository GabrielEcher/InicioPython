"""
Função que receba como parametro um valor inteiro e gere como saída
n linhas com pontos de exclamação
"""
 
n = int(input("Digite um número: "))

def printar_exclamação(n):
    for i in range(1, n + 1):   
        print("!" * i)
    
printar_exclamação(n)