"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""
def menu():
    
    print('BEM VINDO AO CALCULADOR DE MULTAS!')
    print('DIGITE 1 PARA ADICIONAR KG DE PEIXES!')
    print('DIGITE 2 PARA SAIR DO PROGRAMA!')
    
def calcula_multa(entrada_kg):
    
    if entrada_kg < 50:
        print('PESAGEM NÃO RESULTARÁ EM MULTAS')
    
    elif entrada_kg > 50:
        
        diferenca_kg = entrada_kg - 50
        multa = diferenca_kg * 4.00
        
        print(f'HOUVE UM EXCEDENTE DE {diferenca_kg} KG, MULTA À PAGAR: R${multa:.2f}')


if __name__ == '__main__':
    menu()
    escolha = int(input('DIGITE O VALOR PARA A AÇÃO QUE DESEJA FAZER: '))
    
    if escolha == 1:
        entrada_kg = float(input("DIGITE OS KG DE PEIXE: "))
        calcula_multa(entrada_kg)
    
    elif escolha == 2:
        quit()
        
    else:
        print("VALOR INVALIDO")
