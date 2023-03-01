"""
O bloco with

Passo para se trablahar com arquivos

# 1 - Abrir o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with.

"""

# O bloco with

with open('texto.txt', encoding='UTF-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

#print(arquivo.read()) # ValueError pois o with fecha automaticamente o arquivo após manipulá-lo

print(arquivo.closed)