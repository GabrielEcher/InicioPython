"""
Levantando os próprios erros com o raise

Para simplificar o raise é util para que possamos criar nossas próprias
exceções e mensagens

raise ValueError('Valor incorreto')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    
    print(f'O texto {texto} será impresso na cor {cor}')
    
colore('Geek', 'SAD')
"""
def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    
    if cor not in cores:
        raise ValueError('A cor precisa ser uma entre: {cores}')
    
    print(f'O texto {texto} será impresso na cor {cor}')
    
colore('Geek', 'vs')




