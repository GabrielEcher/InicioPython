"""
Decorators

Definição Decorators ->

- São funções;
- Envolvem outras funções e aprimoram seus comportamentos;
- São exemplos de HOF
- Decorators tem uma sintaxe propria, usando @ (Syntact Sugar)

# Decorators como funções (não recomendado , sem syntact sugar)

def fun1(funcao):
    def sendo():
        print("Foi um prazer te conhecer")
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem-vindo')
    
# Testando 1 

#teste = fun1(saudacao)

#teste()

def raiva():
    print("TE ODEIO")
    
    
raiva_educada = fun1(raiva)

raiva_educada()

# Decorators com Syntax Sugar

def seja_educado(funcao):
    def sendo_educado():
        print('Foi um prazer te conhecer')
        funcao()
        print('Tenha um excelente dia')
    return sendo_educado

@seja_educado
def apresentando():
    print('Meu nome é Gabriel')
    
apresentando()


@seja_educado
def dormir():
    print('Quero dormir....')
    
dormir()
"""

