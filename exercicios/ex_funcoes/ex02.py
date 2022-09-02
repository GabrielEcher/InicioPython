"""
Função que recebe a data atual (dia, mes e ano) e exiba na tela 
o formato textual extenso. Ex: Data 01/01/2000, Imprimir: 1 de janeiro de
2000
"""
data = input(f'Digite a data atual no formato[00/00/0000]:')

vetor_data = data.split('/') 

dia, mes, ano = vetor_data

dia = int(dia)
mes = int(mes)
ano = int(ano)

def mes_extenso():
    meses_do_ano = ('janeiro', 'fevereiro', 'março', 'abril', 'maio',
                    'junho', 'julho', 'agosto', 'setembro', 'outubro',
                    'novembro', 'dezembro')
    mes_associado = meses_do_ano[mes - 1] 
    return mes_associado

if 0 < dia < 32 and 0 < mes < 13 and 2000 < ano < 3000:
    print(f'Hoje é dia {dia} de {mes_extenso()} de {ano}')
else:
    print('Insira valores válidos!')