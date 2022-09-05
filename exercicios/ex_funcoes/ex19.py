"""
Função que retorne o maior fator primo de um número
"""

def maior_fator_primo(numero):
    aux = 0
    mult = []
    for i in range(2, numero):
        if numero % i == 0:
            mult.append(i)
            aux += 1
    if aux == 0:
        return print(f'{numero} é primo\n{numero} é o maior fator primo!')
    return print(f"Tem {aux} múltiplos acima de 2 e abaixo de {numero}"
                 f"\nMultiplos: {mult}\n{max(mult)} é o maior fator primo do número {numero}.")
 
 
maior_fator_primo(int(input('Entre com o número que deseja saber o maior fator primo: ')))