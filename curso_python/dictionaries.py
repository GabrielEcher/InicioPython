"""
Dicionários

OBS: SÃO COLEÇÕES DO TIPO CHAVE/VALOR

Dicionários são representados por chaves {}
print(type({}))

OBS: Sobre dicts
    - Chave e valor são separados por dois pontos 'chave':'valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

#CRIAÇÃO DE DICTS

#Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}

print(paises)
print(type(paises))

#Forma 2 (Menos comum)
paises = dict(br="Brasil", eua="Estados Unidos")

#ACESSANDO ELEMENTOS

# Forma 1 - Acessando via chave, da mesma forma que lista/tuple
#print(paises['br'])
#print(paises['eua'])

# Forma 2 - Acessando via get - *recomendado*

print(paises.get("br"))
print(paises.get("ru"))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}

pais = paises.get('br')

if pais:
    print(f"Encontrei o país {pais}")
else:
    print("Não encontrei o país")

#PODEMOS DEFIINIR UM VALOR PADRÃO CASO NÃO ENCONTRAMOS O OBJETO COM A CHAVE INFORMADA
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}

pais = paises.get('br', 'Não encontrado')

print(f"Encontrei o país {pais}")

#VERIFICA SE AS CHAVES INFORMADOS ESTÃO NO DICT, RETORNANDO TRUE OR FALSE
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#PODEMOS UTILIZAR QUALQUER TIPO DE DADO (int, float, string, boolean, inclusive lists, tuples, dicts
#TUPLAS SÃO RECOMENDADAS PARA USAR EM CHAVES DE DICTS
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em NY',
    (37.2113, 23.0098): 'Escritório em SP'
}

#ADICIONAR ELEMENTOS EM UM DICIONÁRIO

# Forma 1 -
receita = {'jan': 100, 'fev': 120, 'mar': 300}

receita['abr'] = 350

print(receita)

# Forma 2 - MAIS COMUM
novo_dado = {'mai': 500}

receita.update(novo_dado)  #ou receita.update({'mai': 500})
print(receita)

#ATUALIZANDO DADOS EM UM DICT

# Forma 1 -
receita['mai'] = 550
print(receita)

# Forma 2 -
receita.update({'mai': 600})
print(receita)

#EM DICIONÁRIOS NÃO PODEMOS TER CHAVES REPETIDAS

#REMOVER DADOS DE UM DICIONÁRIO
print(receita)

# Forma 1 - MAIS COMUM
#PRECISAMOS SEMPRE INFORMAR A CHAVE, CASO NÃO ENCONTRE: KeyError
ret = receita.pop('mar')
print(ret)

print(receita)
#RETORNA O VALOR REMOVIDO

# Forma 2
del receita['fev']
print(receita)
#NESTE CASO O VALOR REMOVIDO NÃO É RETORNADO

#CARRINHO DE COMPRAS COM DICTS

carrinho = []

produto1 = {
    'nome': 'Mouse', 'quantidade': 1, 'preço': 80.00
}
produto2 = {
    'nome': 'Teclado', 'quantidade': 1, 'preço': 120.00
}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Desta forma facilmente adicionamos ou removesmo produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação dos produtos

#MÉTODOS DE DICIONÁRIOS
d = dict(a=1, b=2, c=3)
d.clear()

#COPIANDO UM DICIONÁRIO PARA OUTRO
# Forma 1 - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

#MÉTODO NÃO CONVENCIONAL
outro = {}.fromkeys('a', 'b')

print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

#O MÉTODO FROMKEYS RECEBE DOIS PARÂMETROS: UM ITERAVEL E UM VALOR
#ELE VAI GERAR PARA CADA VALOR ITERÁVEL UMA CHAVE E IRÁ ATRIBUIR À ESTA CHAVE O VALOR INFORMADO


veja = {}.fromkeys('teste', 'valor')
print(veja)

veja1 = {}.fromkeys(range(1, 11), 'novo')
print(veja1)
"""





















