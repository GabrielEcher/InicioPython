"""
Funções - partes de códigos que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar saída de dados;
- Uteis para executar procedimentos similares por repetidas vezes;

OBS: Se voce escrever uma função que realiza várias tareas, é bom fazer uma 
verificação para que a função seja simplificada

"""

#Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

#Função integradas (Built-in), já existentes no python
#print(cores)

#curso = 'Programação em Python'
#print(curso)

#cores.append('roxo')
#print(cores)

#DRY - Don1t Repeat Yourself - Não repita seu código

#Como definir funções:

"""
Forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
parametros_de_entrada -> Opcionais onde tendo mais de um, cada um separado por vírgula
podendo ser opcionais ou não

bloco_da_funcao -> Chamado também de corpo da função ou implementação, é onde o processamento
da função acontece, PODE TER OU NÃO RETORNO DA FUNÇÃO

"""
#Definição
def diz_oi():
    print("OI!")
    
"""
OBS:

1 - Dentro das funções podemos utilizar outras funções
2 - A função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi
3 - Esta função não recebe nenhum parametro de entrada
4 - Esta função não retorna nada

#Utilizando funções
#Chamada de execuções
diz_oi()

#Exemplo 2

def cantar_parabens():
    print('PARABENS PRA VOCE')
    print('NESTA DATA QUERIDA')
    print('BLABALBALBLA')

#Utilizando range com funções
#for n in range(5):    
    #cantar_parabens()

#Em Python podemos criar variaveis do tipo de uma função e executar essa função
#através da variavel 

canta = cantar_parabens
canta()
"""

