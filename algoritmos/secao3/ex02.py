"""
Faça um algoritmo para calcular o estoque médio de uma peça, sendo que:
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
"""
qtmi = int(input("Informe a quantidade mínima do produto: "))
qtmx = int(input("Informe a quantidade máxima do produto: "))

soma = qtmi + qtmx
media = soma / 2

print(f"A média de estoque do produto é: {media}")
