def torre (i, j, tabuleiro):
    ''' Função que determina os possíveis movimentos para a peça torre. '''
    # Todos os componentes da linha e da coluna da peça são marcados.
    for numero in range (dimensao+1):
        tabuleiro[i][numero], tabuleiro[numero][j] = 'x', 'x'

def bispo (i, j, tabuleiro): 
    ''' Função que determina os possíveis movimentos para a peça bispo. '''
    # São construídas as quatro diagonias, uma por vez (achei necessário criar 4 vaiáveis pois elas são alteradas dentro dos loops e independem umas das outras).
    j_novo = j + 1
    for i_novo in range (i-1, -1, -1):
        if 0<=j_novo < dimensao+1 and 0<=i_novo < dimensao+1:
            tabuleiro[i_novo][j_novo] = 'x'
            j_novo+=1
    j_novo2 = j - 1
    for i_novo in range (i-1, -1, -1):
        if 0<=i_novo < dimensao+1 and 0<=j_novo2 < dimensao+1:
            tabuleiro[i_novo][j_novo2] = 'x'
            j_novo2-=1
    i_novo = i + 1
    for j_novo in range (j+1, dimensao +1):
        if 0 <= i_novo < dimensao+1 and 0 <= j_novo < dimensao+1:
            tabuleiro[i_novo][j_novo] = 'x'
            i_novo += 1
    i_novo2 = i + 1
    for j_novo in range (j-1, -1, -1):
        if 0 <= i_novo2 < dimensao+1 and 0 <= j_novo < dimensao+1:
            tabuleiro[i_novo2][j_novo] = 'x'
            i_novo2 += 1

def dama (i, j, tabuleiro):
    ''' Função que determina os possíveis movimentos para a peça dama. '''
    # São combinadas as funções do bispo e da torre.
    j_novo = j + 1
    for i_novo in range (i-1, -1, -1):
        if 0<=j_novo < dimensao+1 and 0<=i_novo < dimensao+1:
            tabuleiro[i_novo][j_novo] = 'x'
            j_novo+=1
    j_novo2 = j - 1
    for i_novo in range (i-1, -1, -1):
        if 0<=i_novo < dimensao+1 and 0<=j_novo2 < dimensao+1:
            tabuleiro[i_novo][j_novo2] = 'x'
            j_novo2-=1
    i_novo = i + 1
    for j_novo in range (j+1, dimensao +1):
        if 0 <= i_novo < dimensao+1 and 0 <= j_novo < dimensao+1:
            tabuleiro[i_novo][j_novo] = 'x'
            i_novo += 1
    i_novo2 = i + 1
    for j_novo in range (j-1, -1, -1):
        if 0 <= i_novo2 < dimensao+1 and 0 <= j_novo < dimensao+1:
            tabuleiro[i_novo2][j_novo] = 'x'
            i_novo2 += 1
    for numero in range (dimensao+1):
        tabuleiro[i][numero], tabuleiro[numero][j] = 'x', 'x'

def rei (i, j, tabuleiro):
    ''' Função que determina os possíveis movimentos para a peça rei. '''
    # Constrói um quadrado de lado 3 em torno da posição i j na qual o rei se localiza.
    for coluna in range (dimensao+1):
        for linha in range (dimensao+1):
            if i-(3//2)<=linha<=i+(3//2) and j-(3//2)<=coluna<=j+(3//2):
                tabuleiro[linha][coluna] = 'x'

def cavalo (i, j, tabuleiro):
    ''' Função que determina os possíveis movimentos para a peça cavalo. '''
    # Confere caso as posições a serem marcadas fazem parte do tabuleiro e, caso positivo, as marca.
    if 0 <= i-1 <= dimensao:
        if 0 <= j-2 <= dimensao:
            tabuleiro[i-1][j-2] ='x'
        if 0 <= j+2 <= dimensao:
             tabuleiro[i-1][j+2] = 'x'
    if 0 <= i-2 <= dimensao:
        if 0 <= j-1 <= dimensao+1:
            tabuleiro[i-2][j-1] ='x'
        if 0 <= j+1 <= dimensao:
            tabuleiro[i-2][j+1] = 'x'
    if 0 <= i+1 <= dimensao:
        if 0 <= j-2 <= dimensao:
            tabuleiro[i+1][j-2] ='x'
        if 0 <= j+2 <= dimensao:
            tabuleiro[i+1][j+2] = 'x'
    if 0 <= i+2 <= dimensao:
        if 0 <= j-1 <= dimensao:
            tabuleiro[i+2][j-1] ='x'
        if 0 <= j+1 <= dimensao:
            tabuleiro[i+2][j+1] = 'x'

def peao (i,j,tabuleiro):
    ''' Função que determina os possíveis movimentos para a peça peão. '''
    # Única peça que, dependendo de sua posição no tabuleiro, sua regra de movimentação é alterada. 
    # Caso a peça esteja nas primeiras 2 linhas do tabuleiro, ela possui 2 movimentações possíveis.
    if i>= dimensao-2:
        tabuleiro[i-1][j], tabuleiro[i-2][j] = 'x', 'x'
    else:
        tabuleiro[i-1][j] = 'x'

fim_da_entrada = False
# Loop para computar diferentes entradas.
while fim_da_entrada == False:
    dimensao = int(input ())

    if dimensao == 0:
        fim_da_entrada = True

    else:
        # Cria-se um tabuleiro de '-' com 1 linha e coluna a mais, onde serão inseridos os números e letras.
        tabuleiro = [['-' for x in range (dimensao+1)] for y in range(dimensao+1)]
        linha = dimensao
        letra = 97
        peca = (input()).split(' ')

        print ('Movimentos para a peca '+ peca[0]+ ' a partir da casa ' + peca[1]+peca[2]+'.')
        # É chamada a função correspondente à peça.
        # Como o tabuleiro é invertido (as matrizes tem linhas contadas de cima para baixo e, os tabuleiros, de baixo para cima, são feitas as conversões da notação letra-número para como o Python lê i-j).
        if peca[0] == 'Torre':
           torre (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)
        elif peca[0] == 'Bispo':
            bispo (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)
        elif peca[0] == 'Dama':
            dama (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)
        elif peca[0] == 'Rei':
            rei (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)
        elif peca[0] == 'Cavalo':
            cavalo (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)
        elif peca[0] == 'Peao':
            peao (dimensao-int(peca[2]), ord(peca[1])-96, tabuleiro)

        # São inseridos os números e as letras no tabuleiro.
        for numero in range (linha):
            tabuleiro[numero][0] = linha
            linha -= 1
        for coluna in range (1,dimensao+1):
            tabuleiro[dimensao][coluna] = chr(letra)
            letra += 1
        tabuleiro[dimensao][0] = ' '

        # o i-j da peça é marcado com 'o'.
        tabuleiro[dimensao-int(peca[2])][ord(peca[1])-96] = 'o'

        # É impresso o tabuleiro.
        for line in tabuleiro:
            print (' '.join(map(str, line)))
        print ('')