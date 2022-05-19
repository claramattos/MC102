from math import sqrt

def desenha_quadrado(i, j, lado, vezes_que_rodou):
    ''' Função recursiva que desenha um quadrado a partir de seu centro e do valor de seu lado. '''
    # A função é chamada, primeiramente, para o centro do quadrado. A partir dele, o quadrado vai se "espalhando", chamando a função para os 8 pontos que envolvem o ponto pintado.
    # O parâmetro "lado" é sempre passado diminuído em 1 unidade, o que determina até quando o quadrado pode se propagar.
    # O parâmetro "vezes_que_rodou" consiste em uma lista que indica quantas vezes uma certa posição da matriz já passou pela função de desenhar quadrados. 
    # Caso esse valor exceda o valor do perímetro do quadrado (número máximo de vezes que uma coordenada deve passar pela função para formar o quadrado desejado), a função é retornada. 
    if lado == 0 or -1 < i < linhas and -1 < j < colunas and vezes_que_rodou[i][j] > (lado-1)*4:
        return 
    # Caso contrário, e ij fizer parte da matriz "quadro", a posição é pintada.
    elif -1 < i < linhas and -1 < j < colunas:
        quadro[i][j] = 'x'
        vezes_que_rodou[i][j] += 1
        # A função é chamada para os 8 pontos que envolvem o ponto pintado.
        return desenha_quadrado(i-1, j-1, lado-1, vezes_que_rodou), desenha_quadrado(i-1, j, lado-1, vezes_que_rodou), desenha_quadrado(i-1, j+1, lado-1, vezes_que_rodou), desenha_quadrado(i, j-1, lado-1, vezes_que_rodou), desenha_quadrado(i, j+1, lado-1, vezes_que_rodou), desenha_quadrado(i+1, j-1, lado-1, vezes_que_rodou), desenha_quadrado(i+1, j, lado-1, vezes_que_rodou), desenha_quadrado(i+1, j+1, lado-1, vezes_que_rodou)   

def desenha_circuloooo (i, j, raio, i_circulo, j_circulo, true_or_false):
    ''' Função recursiva que desenha um círculo a partir de seu centro e do valor de seu raio. '''
    # As diferenças da função de círculos e de quadrados são os parâmetros i_circulo e j_circulo, nunca alterados, utilizados para calcular a distância de um ponto qualquer do centro do círculo.
    # Assim, a função para desenhar círculos só precisa passar uma vez por cada ponto e, por isso, a matriz vezes_que_rodou pode ser substituída por outra "true_or_false", que somente informe caso um ponto já tenha sido processado.
    if -1 < i < linhas and -1 < j < colunas and true_or_false[i][j] == True:
        return 
    elif -1 < i < linhas and -1 < j < colunas and sqrt(((i-i_circulo)**2)+(j-j_circulo)**2) <= raio:
        quadro[i][j] = 'x'
        true_or_false[i][j] = True
        return desenha_circuloooo(i-1, j, raio, i_circulo, j_circulo, true_or_false), desenha_circuloooo(i, j-1, raio, i_circulo, j_circulo, true_or_false), desenha_circuloooo(i, j+1, raio, i_circulo, j_circulo, true_or_false), desenha_circuloooo(i+1, j, raio, i_circulo, j_circulo, true_or_false)

dimensoes = input()
numero_de_formas = int(input())
formas = []

linhas = int((dimensoes.split(' '))[0])
colunas = int((dimensoes.split(' '))[1])

# Aqui, desenha-se um "quadro em branco" com as dimensões informadas.
quadro = [['-' for x in range(colunas)] for y in range(linhas)]

# Cria-se uma matriz cujas listas contám informações sobre cada forma a ser desenhada.
for forma in range (numero_de_formas):
    formas.append(input().split(' '))

# Para cada elemento da  matriz de formas, é chamada a função correspondente e as matrizes vezes_que_rodou e true_or_false são restauradas (para não conflitarem com outras formas que têm interseção com aquelas já desenhadas).
for forma in range (len(formas)):
    if formas[forma][0] == 'quadrado':
        vezes_que_rodou = [[0 for x in range(colunas)] for y in range(linhas)]
        desenha_quadrado (int(formas[forma][1]), int(formas[forma][2]), int(formas[forma][3])//2 + 1, vezes_que_rodou)
    elif formas[forma][0]== 'circulo':
        i_circulo, j_circulo, raio = int(formas[forma][1]), int(formas[forma][2]), int(formas[forma][3])
        true_or_false = [[False for x in range(colunas)] for y in range(linhas)]
        desenha_circuloooo (i_circulo, j_circulo, raio, i_circulo, j_circulo, true_or_false)

# Finalmente, imprime-se o quadro desejado.
for line in quadro:
        print (' '.join(map(str, line)))