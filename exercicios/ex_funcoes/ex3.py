"""
Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
sobre vendas expressa em porcentagem e custo, 
que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
venda = float(input("Digite o valor da venda: "))

def somaImposto(venda):
    if venda <= 2000:
        taxaImposto = venda * (5/100)
        total_venda_imposto = venda - taxaImposto
        return f'VENDA: R${venda:.2f} \n \
            VENDA COM IMPOSTO DESCONTADO:{total_venda_imposto:.2f} \
            \nVALOR DESCONTO: R${taxaImposto:.2f}'

    elif venda > 2000 or venda <= 4000:
        taxaImposto = venda * (8/100)
        total_venda_imposto = venda - taxaImposto
        return f'VENDA: R${venda:.2f} \nVENDA COM IMPOSTO DESCONTADO:{total_venda_imposto:.2f} \nVALOR DESCONTO: R${taxaImposto:.2f}'
        
    elif venda > 4000:
        taxaImposto = venda * (10/100)
        total_venda_imposto = venda - taxaImposto
        return f'VENDA: R${venda:.2f} \nVENDA COM IMPOSTO DESCONTADO:{total_venda_imposto:.2f} \nVALOR DESCONTO: R${taxaImposto:.2f}'
        
print(somaImposto(venda))