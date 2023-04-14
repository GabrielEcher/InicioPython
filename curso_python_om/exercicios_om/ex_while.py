"""
Iterando strings com while
"""

nome = 'Gabriel Echer'
index = 0
novo_nome = ''


while index < len(nome):
    letra = (nome[index])
    novo_nome += f'*{letra}'
    index += 1
    
print(novo_nome)