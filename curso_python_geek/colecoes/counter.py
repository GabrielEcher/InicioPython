"""
Módulo Collections - Counter (Contador)

Collections -> High performance Container DateTypes

Counter -> recebe um iteravel como parametros e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento

#EXEMPLO 1
#Podemos utilizar qualquer iterável
lista = [1, 1, 2, 2, 3,3,3, 3, 1, 1, 2, 4, 5, 6, 7, 7, 8, 9, 8, 9, 9]

#Utilizando o counter
res = Counter(lista)

print(type(res))

print(res)

#Counter({1: 4, 3: 4, 2: 3, 9: 3, 7: 2, 8: 2, 4: 1, 5: 1, 6: 1})
#Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

#EXEMPLO 2
print(Counter('Gabriel Echer'))
#Counter({'r': 2, 'e': 2, 'G': 1, 'a': 1, 'b': 1, 'i': 1, 'l': 1, ' ': 1, 'E': 1, 'c': 1, 'h': 1})
"""
from collections import Counter

#EXEMPLO 3
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob o 
princípio wiki.
 Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, que todos possam editar e melhorar. 
 O projeto é definido pelos princípios fundadores e o conteúdo é disponibilizado sob a licença Creative Commons BY-SA e 
 pode ser reutilizado sob a mesma licença, desde que respeitando os termos de uso. 
 Todos podem publicar conteúdo on-line desde que criem uma conta e sigam as regras básicas, como verificabilidade ou 
 notoriedade."""

palavras = texto.split()

res = Counter(palavras)
print(res)

#Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))