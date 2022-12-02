"""
Mapas -> Conhecidos em Python como Dicionários
Dicionários em python são representados por {}


#ITERAR SOBRE DICTS

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f"{chave} : {receita[chave]}")

#ACESSANDO AS CHAVES
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#ACESSANDO OS VALORES

print(receita.values())

for valor in receita.values():
    print(valor)

#DESEMPACOTAMENTO DE DICIONÁRIOS

for chave, valor in receita.items():
    print(f'chave:{chave} e valor={valor}')


#SOMA, VALOR MÁX, VALOR MÍN, LEN
#Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)





















