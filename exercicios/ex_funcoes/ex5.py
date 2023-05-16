"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar 
até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""

def valor_pagamento(valor_prestacao, dias_atraso):
    conta_a_pagar = valor_prestacao
    prestacoes_pagas = 0
    valor_total_pago = 0
    
    while valor_prestacao != 0:
        if dias_atraso == 0:
            valor_total_pago += valor_prestacao
            conta_a_pagar -= valor_prestacao
            print(f'VALOR PAGO: R${valor_prestacao:.2f} - VALOR RESTANTE À PAGAR: R${conta_a_pagar:.2f}')
            prestacoes_pagas += 1
        
        elif dias_atraso > 0:
            multa = conta_a_pagar * 3 / 100
            juros = conta_a_pagar * 0.1 * dias_atraso
            valor_prestacao_e_multa = valor_prestacao + multa + juros
            valor_total_pago += valor_prestacao_e_multa
            conta_a_pagar -= valor_prestacao_e_multa
            
            print(f'VALOR PAGO: R${valor_prestacao_e_multa:.2f} (R${valor_prestacao:.2f} + multa R${multa:.2f} + juros R${juros:.2f}) - VALOR RESTANTE À PAGAR: R${conta_a_pagar:.2f}')
        
        valor_prestacao = float(input("Digite o valor da prestação a ser pago (ou 0 para sair): "))
        dias_atraso = int(input("Informe os dias em atraso: "))
    
    print(f'TOTAL DE PRESTAÇÕES PAGAS: {prestacoes_pagas}')
    print(f'VALOR TOTAL PAGO: R${valor_total_pago:.2f}')

valor_prestacao = float(input("Digite o valor da prestação a ser pago (ou 0 para sair): "))
dias_atraso = int(input("Informe os dias em atraso: "))

valor_pagamento(valor_prestacao, dias_atraso)