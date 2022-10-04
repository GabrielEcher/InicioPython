"""
Reversed

Funciona com qualquer iterável

Sua função é inverter o iterável

Retorna um iterável chamado List Reverse Iterator
"""

# Exemplos




lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)

# Podemos converter o elemento retornado para uma lista, tuple ou conjunto

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed('Gabriel Echer'):
    print(letra, end='')
    

# Podemos fazer o mesmo sem o uso do for

print(''.join(list(reversed('Gabriel Echer'))))

# Slice de strings
print('Gabriel Echer'[::-1])

# Podemos fazer um loop reverso
for n in reversed(range(0, 10)):
    print(n)