"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps).
Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

print("====CALCULADORA DE DOWNLOAD====")

tamanho_arq = float(input("Qual o tamanho do arquivo que deseja baixar? "))
link_net = int(input("Qual a velocidade do link da sua internet? "))

def calcula_tempo():
    tempo = tamanho_arq / (link_net / 8)
    print(f'O tempo aproximado para o download terminar é de: {tempo} segundos')
    
calcula_tempo()