"""

Tipo String

-Um dado é sempre considerado string quando está entre aspas duplas ou simples, independente do conteúdo
 dentro das aspas
-\n em string pula uma linha do conteúdo
"""
nome = "Gabriel Echer"
# print(nome.upper())
# print(nome.lower())
# print(nome.split())  # Transforma em uma lista de strings

# G A B R I E L   E C H   E   R
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# print(nome[0:7])  # Ultimo numero não está incluido ao localizar o indice
# print(nome.split()[0])
# print(nome.split()[1])

# print(nome[9]) # Printa o valor 9 dentro da string


# Inverter os indices dentro de uma string
# [::-1] começa no indice 1 até o ultimo invertendo
print(nome[::-1])

print(nome.replace("e", "R"))
