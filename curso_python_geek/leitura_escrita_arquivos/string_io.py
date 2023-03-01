"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional, o software precisa de permissão:
- Permissão de leitura 
- Permissão de escrita


StringIO -> utilizado para ler e criar arquivos em memória

"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'String normal'

# Podemos criar um arquivo em memória já com uma string inserida, ou vazio

arquivo = StringIO(mensagem)

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos

print(arquivo.read())

arquivo.write('\nOUTRO TEXTO')

print(arquivo.read())

