"""
Função que desenha uma linha na tela usando vários simbolos, ex: ======, a função
deverá receber por parametro quantos sinais de igual serão mostrados
"""

def desenha_linha(simbol, qnt):
    return simbol * qnt
        
        
simbol = str(input("Digite um símbolo: "))
qnt = int(input("Digite a quantidade de vezes que o programa deve digitar o símbolo: "))

print(desenha_linha(simbol, qnt))
        