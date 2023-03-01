"""
and, or, not, is

Operadores unários: not
Operadores binários: and , or , is

--Regras de funcionamento--
!! Para o 'and' todos os valores precisam ser True !!
!! Para o 'or' um ou outro valor precisa ser True !!
!! Para o 'not' o valor do booleano é invertido, ou seja se for True vira False e vice-versa !!
!! Para o 'is' o valor é comparado com um segundo !!
"""
ativo = True
logado = True

"""
if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta(cheque seu e-mail)")
"""
"""
if not ativo: ##Jeito pythonico
    print("Você precisa ativar sua conta(cheque seu e-mail)")
else:
    print("Bem-vindo usuário!")

print(not False)
print(not True)
"""
if ativo is False:
    print("Você precisa ativar sua conta(cheque seu e-mail)")
else:
    print("Bem-vindo usuário!")



