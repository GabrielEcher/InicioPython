"""
Generator

# Generators
nomes = ['Carlao', 'Caio', 'Claudio', 'Cael', 'André']
print(any(nome[0] == 'C' for nome in nomes))

#List Comprehension
res = [nome[0] == 'C' for nome in nomes]

# Generators (mais performático)
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual a utilidade? Retorna a quantidade de bytes em memória do elemento passado como parâmetro

from sys import getsizeof
print(getsizeof(['Geek']))
from sys import getsizeof

# Gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma set de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma dict de números com dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com generators
gen_comp = getsizeof(x * 10 for x in range(1000))
print('Para fazer a mesma tarefa gastamos em memória:')

print(f'list comprehension: {list_comp}')
print(f'set comprehension: {set_comp}')
print(f'dict comprehension: {dict_comp}')
print(f'Generator expression:{gen_comp}')
"""



# Como iterar com o generator expressions

gen_comp = (x * 10 for x in range(1000))

for num in gen_comp:
    print(num)