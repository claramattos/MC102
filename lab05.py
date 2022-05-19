def conta_minusculas (endereco):
    '''Conta quantas letras minúsculas existem em um endereço'''
    n_de_minusculas = 0
    for k in range (len(endereco)):
        if endereco[k].islower() == True:
            n_de_minusculas += 1 
    return n_de_minusculas
    
def conta_maiusculas (endereco):
    '''Conta quantas letras maiúsculas existem em um endereço.'''
    n_de_maiusculas = 0
    for k in range (len(endereco)):
        if endereco[k].isupper() == True:
            n_de_maiusculas += 1 
    return n_de_maiusculas

def conta_letras (endereco):
    '''Conta quantas letras do alfabeto existem em um endereço.'''
    n_de_letras = 0
    for k in range (len(endereco)):
        if endereco[k].isalpha () == True:
            n_de_letras += 1 
    return n_de_letras

def conta_palavras (endereco):
    '''Conta quantas palavras (isto é, uma sequência de letras e/ou números separada por espaços em branco) existem em um endereço.'''
    n_de_palavras = len(endereco.split (' ')) 
    return n_de_palavras

def conta_somaASCII (endereco):
    '''Soma os valores ASCII de todos os caracteres de um endereço (incluindo os caracteres que são espaços em branco).'''
    soma_ASCII = 0
    for k in range (len(endereco)):
        soma_ASCII += ord(endereco[k])
    return soma_ASCII

entrada_lista = (input()).split (' ')
dia = entrada_lista[0]
lista = []

for k in range (int(entrada_lista[1])):
    lista.append(input())
   
if dia == 'Segunda':
    lista = sorted(lista, key=conta_minusculas)
elif dia == 'Terca':
    lista = sorted(lista, key=conta_maiusculas, reverse=True)
elif dia == 'Quarta':
    lista = sorted(lista, key=conta_letras)
elif dia == 'Quinta':
    lista = sorted(lista, key=conta_palavras)
elif dia == 'Sexta':
    lista = sorted(lista, key=conta_somaASCII, reverse=True)

for k in range (len(lista)):
    print (lista[k])