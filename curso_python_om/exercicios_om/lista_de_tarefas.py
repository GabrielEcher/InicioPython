import os


tarefas = []
tarefas_refazer = []

def add_task(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    
def print_task(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('TAREFAS:')
    print()
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
    
def remove_last_task(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa} removida na lista de tarefas.')
    tarefas_refazer.append(tarefa)
    
def redo(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
   
    



while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou um comando: ')
    
    if tarefa == 'listar':
        print_task(tarefas)
        continue
    
    elif tarefa == 'desfazer':
        remove_last_task(tarefas, tarefas_refazer)
        print_task(tarefas)
        continue
    
    elif tarefa == 'refazer':
        redo(tarefas, tarefas_refazer)
        print_task(tarefas)
        continue
    
    elif tarefa == 'clear':
        os.system('clear')
        continue
     
    else:
        add_task(tarefa, tarefas)
        print_task(tarefas)
        continue