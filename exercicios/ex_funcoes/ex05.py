"""
Função para o cálculo do volume de uma esfera, sendo que o raio é passado por parâmetro
V = 4/3 * pi * R ao cubo
"""

num = int(input("Digite o valor para calcular o volume da esfera: "))

def calculo_volume(num):
    volume = 4/3 * 3.14 * num ** 3
    return f'O volume da esfera é de {round(num)}m³'

print(calculo_volume(num))