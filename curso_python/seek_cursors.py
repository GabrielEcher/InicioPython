"""
Seek e Cursors

seek() -> Utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt', encoding='UTF-8')

#print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(3) # Lê do caractere indicado pra frente
print(arquivo.read()) 

arquivo = open('texto.txt', encoding='UTF-8')

# readline() -> Função que lÊ o arquivo linha a linha

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#readlines()
linhas = arquivo.readlines()
print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo 
no disco do pc e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os 
trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt', encoding='UTF-8')

# 2 - Trabalhar com o arquivo;
print(arquivo.read())

print(arquivo.closed) #  False - Verifica se o arquivo está aberto ou fechado
                      # False 
# 3 - Fechar o arquivo;
arquivo.close()
arquivo.closed # True arquivo fechado

# OBS: se tentarmos manipular um arquivo depois de seu fechamento, teremos ValueError;

arquivo = open('texto.txt', encoding='UTF-8')

# Podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(4))
"""




