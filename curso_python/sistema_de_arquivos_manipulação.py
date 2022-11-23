"""
Sistema de arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe
# Paths relativos
print(os.path.exists('frutas.txt')) # True
print(os.path.exists('curso_python')) # True

# Diretório
# Paths Absolutos
print(os.path.exists('curso_python//.idea'))
]
# Criando arquivos

# Forma 1
open('arquivoss.txt', 'w').close()

# Forma 2
open('arquivoss.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Criando diretórios

os.mkdir('templates') # Cria um diretório caso ele não exista

# Criando multidiretórios

os.makedirs('templates//geek//university')

# Renomear arquivos e diretórios

os.rename('templates', 'templates2')

# DELETE - Ao deletarmos um arquivo ou diretório, ele não vai para a lixeira, eles somem.

os.remove('arquivo-teste3.txt') # Serve para remover arquivos

# Se eu usar o remove para remover diretórios teremos IsDirectoryError

# Removendo diretórios

os.rmdir('templates2') # REMOVENDO DIRETÓRIOS VAZIOS

# Podemos remover uma arvore de diretórios vazios

os.removedirs('templates2//geek//university')

# Para enviarmos arquivos para a lixeira é preciso instalar uma bibilioteca externa, para podermos utilizar uma lixeira

from send2trash import send2trash

send2trash('novo.txt')

import tempfile

# Trabalhando com arquivos e diretórios temporários

# Criando um diretório temporario

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Gabriel\n')
    input() # Segura o código para o arquivo não ser excluído

# Criando uma arquivo temporario

with tempfile.TemporaryFile() as tmpf:
    tmpf.write(b'gabriel') # o B tranforma a string em bits
    tmpf.seek(0)
    print(tmpf.read())
"""
import os
import tempfile















