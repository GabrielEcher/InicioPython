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
"""
import os







