"""
Entendendo iterators e iterables

Iterator ->
    - Objeto que pode ter iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;
    
Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.
    

nome = 'Gabriel'
numeros = [1, 2, 3, 4, 5]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))


print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
"""

    