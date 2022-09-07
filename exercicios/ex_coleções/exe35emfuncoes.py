def levariavel():
    var = int(input("Digite um valor menor que 10000: "))
    return var

def transforma_int_em_string(inteiro):
    return str(inteiro)

def converte_str_em_lista_de_inteiro(palavra):
    list = []
    for posicao in palavra:
        list.append(int(posicao))

    return list

def converte_lista_em_int(list):
    string = ""
    for pos in list:
        string += str(pos)

    if len(string)>0:
        return int(string)

    return -1

def inicia():
    #Primeira parte do programa
    a = levariavel()
    b = levariavel()
    
    str_a = transforma_int_em_string(a)
    str_b = transforma_int_em_string(b)
    
    list_a = converte_str_em_lista_de_inteiro(str_a)
    list_b = converte_str_em_lista_de_inteiro(str_b)
    
    #revertendo as listas
    
    list_a.reverse()
    list_b.reverse()
    
    #segunda parte do programa
    list_a.reverse()
    list_b.reverse()
    
    a = converte_lista_em_int(list_a)
    b = converte_lista_em_int(list_b)
    
    soma = a+b
    print("Soma final {0}".format(soma)) 

#inicia()

class Echer:
    def __init__(self, nome, tamanho_pinto, cor_do_rabo):
        self.nome = nome
        self.tamanho_pinto = int(tamanho_pinto)
        self.cor_do_rabo = cor_do_rabo
        
    def to_string(self):
        print("Esse Eche se chama {0}. Ele tem um pinto de {1} cm e a cor do rabo dele é {2}".format(self.nome, self.tamanho_pinto, self.cor_do_rabo))

novo_echer = Echer("Podre", 15, "Neon")
novo_echer.to_string()