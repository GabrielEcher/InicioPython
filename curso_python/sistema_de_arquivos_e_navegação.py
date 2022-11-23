"""
Sistema de arquivos e manipulação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso
do módulo OS

OS -> Operating System

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente

print(os.getcwd()) # Retorna o caminho absoluto do diretório

# Para mudar o diretório, podemos utilizar o chdir()


os.chdir('..') # Volta uma pasta dentro do diretório
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('C:\\Users\\gabriel\\PythonUdemyGit')) #(Windows)

# Podemos identificar o sistema operacional com o módulo os

print(os.name)

print(os.getcwd()) # C:\Users\gabriel\PythonUdemyGit

res = os.path.join(os.getcwd(), 'pythonProject') # C:\Users\gabriel\PythonUdemyGit

os.chdir(res)

print(os.getcwd())

# Podemos listar os arquivos e diretórios com o listdir()

print(len(os.listdir('C:\\Users\\gabriel\\PythonUdemyGit')))

print(os.listdir('C:\\Users\\gabriel\\PythonUdemyGit'))

print(os.listdir('C://'))
"""

import os

# Podemos listar diretórios com mais detalhes com o scandir()

scanner = (os.scandir('C://Users//gabriel//PythonUdemyGit'))
arquivos = list(scanner)
#print(arquivos)

#print(dir(arquivos[0]))

#print(arquivos[0].name) # Nome do arquivo

print(arquivos[0].inode())
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas sobre o arquivo

# OBS: Quando utilizamos a função scandir, precisamos fechá-la, assim como quando abrimos um arquivo

scanner.close()