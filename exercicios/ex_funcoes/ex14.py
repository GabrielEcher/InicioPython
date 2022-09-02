"""
Função que receba uma distacia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela

CONSUMO   | KM/L | MENSAGEM
menor que |  8   | Venda o carro!
entre     |8 e 14| Economico!
maior que |  12  | Super economico

"""

km = int(input("Digite quantos km foram andados: "))
litros = int(input("Digite a quantidade de litros gastos: "))

def calculo_media_carro(km, litros):
    if km / litros < 8:
        return 'Venda o carro!'
    elif km / litros > 8 < 14:
        return 'Econômico!'
    elif km / litros > 12:
        return 'Super econômico!'
    
print(calculo_media_carro(km, litros))
    