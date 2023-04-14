"""
while

condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair' or nome == 'SAIR':
        break
"""

cont = 0

while cont < 100:
    cont += 1
    print(cont)
    
print('END')