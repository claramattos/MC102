from math import sqrt
fim_da_entrada = False

def calcula_maior_distancia (lista_de_esconderijos, Y):
    ''' Função que calcula a distância euclidiana de um ponto até seu esconderijo mais distante, dado o ponto e a lista que contém todos os esconderijos existentes. '''
    maior_distancia = sqrt((lista_de_esconderijos[0][0])**2 + (lista_de_esconderijos[0][1]- Y)**2)
    for k in range (1, len(lista_de_esconderijos)):
        if sqrt((lista_de_esconderijos[k][0])**2 + (lista_de_esconderijos[k][1]- Y)**2) > maior_distancia:
            maior_distancia = sqrt((lista_de_esconderijos[k][0])**2 + (lista_de_esconderijos[k][1]- Y)**2)
    return maior_distancia 

def busca_binaria ():
    ''' Função que utiliza a lógica da busca binária para encontrar o ponto com menor distância até seu esconderijo mais distante. '''
    # Ao plotarmos um gráfico de Y por o valor que "calcula_maior_distancia (lista_de_esconderijos, Y)" retorna, notaremos que a função construída sempre terá um ponto de mínimo, e os valores de Y próximos ao Y desejado terão valores menores que aqueles mais afastados (de forma semelhante a uma parabola).
    # Dessa forma, utiliza-se a lógica da busca binária para analisar o valor da função "calcula_maior_distancia" em um ponto, no ponto da sua esquerda e no ponto da sua direita, e o número de cálculos a serem realizados será minimizado.
    e = 0
    d = Yi-2
    while e <= d:
        m = (e + d) // 2
        # Caso o "e" e o "d" coincidam, ou caso um ponto seja confirmado como um ponto de mínimo na função, isso indica que foi encontrado o valor desejado.
        if e == d:
            return d + 1
        if calcula_maior_distancia(coordenadas_esconderijos, m) > calcula_maior_distancia(coordenadas_esconderijos, m+1) and calcula_maior_distancia(coordenadas_esconderijos, m+2) > calcula_maior_distancia(coordenadas_esconderijos, m+1):
            return m + 1
        # Na situação abaixo, as distâncias estão decresecendo conforme o vallor de m aumenta, o que indica que o Y ideal está para a direita. 
        elif calcula_maior_distancia(coordenadas_esconderijos, m) > calcula_maior_distancia(coordenadas_esconderijos, m+1) > calcula_maior_distancia(coordenadas_esconderijos, m+2):
            e = m + 1 
        # Na situação abaixo, as distâncias estão aumentando conforme o valor de m aumenta, o que indica que o valor do Y ideal está para a esquerda.
        elif calcula_maior_distancia(coordenadas_esconderijos, m) < calcula_maior_distancia(coordenadas_esconderijos, m+1) < calcula_maior_distancia(coordenadas_esconderijos, m+2):
            d = m - 1

# Aqui, são armazenadas as informações para todas as entradas enquanto a entrada for diferente de "0 0" (o que indica o fim das informações).
while fim_da_entrada == False:

    informacoes_basicas = input ()

    if informacoes_basicas != '0 0':
        numero_de_esconderijos, Yi = int((informacoes_basicas.split(' '))[0]), int((informacoes_basicas.split(' '))[1])
        coordenadas_esconderijos = []

        for k in range (numero_de_esconderijos):
            esconderijo = (input().split (' '))
            coordenadas_esconderijos.append([int(esconderijo[0]),int (esconderijo[1])]) 
            
        print (busca_binaria())

    else:
        fim_da_entrada = True