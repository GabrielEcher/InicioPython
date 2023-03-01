"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se iterável esta vazio

# Exemplo all()

#print(all([ 1, 3, 4])) # TRUE

#print(all([0, 1, 3, 4])) # FALSE (por causa do 0)

#print(all([])) # TRUE

nomes = ['Joao', 'Gabriel', 'Maria']

print(all(nome[0] == 'G' for nome in nomes)) # Verifica se os usuarios da lista tem a letra G no inicio e retorna True or False

# OBS: Um iterável vazio convertido em boolean é false, mas o all o considera como True

print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8]if num % 2 == 0]))

any() -> Retorna True se qualquer um elemento do iterável for verdadeira. Se o iterável estiver vazio, retorna falso
"""

print(any([0, 1, 2, 3, 4])) #TRUE

print(any([0, 0, 0, (), [], False])) #FALSE