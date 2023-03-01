"""
São utilizados para gerar sequencias numericas não de forma aleatória mas sim de maneira especificada

Formas de utilização:

range(valor_de_parada) OBS: valor_de_parada não conta (inicio  padrão 0, e passo de 1 em 1

#forma 1:
for num in range(11):
    print(num)

#forma 2
range(valor_de_parada) OBS: valor_de_parada não conta (inicio  especificado, e passo de 1 em 1
for num in range(1, 11):
    print(num)

#forma 3
range(valor_de_inicio , valor_de_parada, passo)
OBS: valor_de_parada não conta (inicio  especificado, e passo especificado
for num in range(5, 50, 5):
    print(num)

#forma 4 (inversa)
range(inicio, valor_de_parada, passo)
for num in range(10, -1, -1):
    print(num)

"""