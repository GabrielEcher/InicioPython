"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento
"""

salario = float(input("Digite seu salário: "))

def calculo_salario_menos_280(salario):
    percentual = 20
    aumento = (salario * percentual) / 100
    salarionovo = salario + aumento
    
    print(f'SALÁRIO ANTES DO REAJUSTE: R${salario}')
    print(f'PERCENTUAL DE AUMENTO APLICADO: {percentual}')
    print(f'VALOR DO AUMENTO: R${aumento}')
    print(f'NOVO SALÁRIO: R${salarionovo}')

def calculo_salario_menor_700(salario):
    percentual = 15
    aumento = (salario * percentual) / 100
    salarionovo = salario + aumento
    
    print(f'SALÁRIO ANTES DO REAJUSTE: R${salario}')
    print(f'PERCENTUAL DE AUMENTO APLICADO: {percentual}')
    print(f'VALOR DO AUMENTO: R${aumento}')
    print(f'NOVO SALÁRIO: R${salarionovo}')

def calculo_salario_maior_700(salario):
    percentual = 10
    aumento = (salario * percentual) / 100
    salarionovo = salario + aumento
    
    print(f'SALÁRIO ANTES DO REAJUSTE: R${salario}')
    print(f'PERCENTUAL DE AUMENTO APLICADO: {percentual}')
    print(f'VALOR DO AUMENTO: R${aumento}')
    print(f'NOVO SALÁRIO: R${salarionovo}')

def calculo_salario_maior_1500(salario):
    percentual = 5
    aumento = (salario * percentual) / 100
    salarionovo = salario + aumento
    
    print(f'SALÁRIO ANTES DO REAJUSTE: R${salario}')
    print(f'PERCENTUAL DE AUMENTO APLICADO: {percentual}')
    print(f'VALOR DO AUMENTO: R${aumento}')
    print(f'NOVO SALÁRIO: R${salarionovo}')
    
if salario <= 280:
    calculo_salario_menos_280(salario)

elif salario > 280 and salario <= 700:
    calculo_salario_menor_700(salario)

elif salario > 700 and salario <= 1500:
    calculo_salario_maior_700(salario)
    
elif salario > 1500:
    calculo_salario_maior_1500(salario)
 