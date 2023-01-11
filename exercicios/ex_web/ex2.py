"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

print("O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:")
print("                     Até 5 Kg           Acima de 5 Kg")
print("File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg")
print("Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg")
print("Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg")




carne = int(input('Digite o número à frente da carne que desejará comprar:\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha\n'))
quantidade = int(input('Escolha quantos kg: '))
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))


if carne == 1:
    
    tipo = 'Filé Duplo'
    valor_carne = 4.90   
    
    if quantidade <= 5:
        valor_kg = valor_carne * quantidade
        
    else:
        valor_kg = 5.80 * quantidade
          
elif carne == 2:
    
    tipo = 'Alcatra'
    valor_carne = 5.90   
    
    if quantidade <= 5:
        valor_kg = valor_carne * quantidade
        
    else:
        valor_kg = 6.80 * quantidade
       
elif carne == 3:
    
    tipo = 'Picanha'
    valor_carne = 6.90   
    
    if quantidade <= 5:
        valor_kg = valor_carne * quantidade
          
    else:
        valor_kg = 7.80 * quantidade
    
if resposta == 1:
    r = "SIM"

    desconto = ((valor_kg * 5) / 100)
    total = valor_kg - desconto
else:
    r = "NÃO"
    total = valor_kg

print("============CUPOM FISCAL===================")
print(f"CARNE=========================-{tipo}") 
print(f"TOTAL=========================R${valor_kg}") 
print(f"PAGAMENTO CARTÃO=============={r}")
print(f'VALOR A PAGAR================={total}')
print(f"==========================================")    

        

    