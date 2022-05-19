def le_matriz (matriz, ordem_matriz):
    '''Converte uma matriz inserida via input() para uma matriz no Python.'''
    for n in range (ordem_matriz):
        matriz.append((input()).split (' '))

fim_da_entrada = False

# Enquanto a entrada não for "0 0", que representa o fim da entrada, serão calculadas as dimensões da supermatriz comum de duas matrizes a serem inseridas.
# Para isso, será necessário encontrar as dimensões da matriz interseção das duas matrizes originas.
while fim_da_entrada == False:
    matriz1, matriz2, matriz_intersecao = [], [], []
    ordem_matrizes = input ()
    if ordem_matrizes != '0 0':
        ordem_matriz1, ordem_matriz2 = int((ordem_matrizes.split (' ')) [0]), int((ordem_matrizes.split (' ')) [1])
        # As matrizes, até então armazenadas como strings via input(), são convertidas para matrizes no Python.
        le_matriz (matriz1, ordem_matriz1)
        le_matriz (matriz2, ordem_matriz2)
            # A partir daqui, calcula-se qual a dimensão da matriz interseção. 
            # Para toda linha das matrizes originais, será produzido um conjunto para verificar caso exista interseção entre as linhas. 
        for n in range (ordem_matriz2):
            conjunto_matriz1, conjunto_matriz2 = set(), set ()
            for elemento in matriz2[n]:
                conjunto_matriz2.add (elemento)
            for z in range (ordem_matriz1):
                for elemento in matriz1[z]:
                    conjunto_matriz1.add (elemento)
            # Caso haja interseção entre uma linha de uma matriz e uma linha da outra matriz, o conjunto interseção é inserido na lista matriz_intersecao.
            # Dessa forma, é feita uma lista de conjuntos cujo tamanho igual é ao número de linhas da matriz interseção e numero de componentes dos conjuntos igual ao número de colunas.
            if conjunto_matriz1.intersection(conjunto_matriz2):
                matriz_intersecao.append (conjunto_matriz1.intersection(conjunto_matriz2))
        # Portanto, a supermatriz comum terá a dimensão da soma das dimensões das matrizes originais subtraída das dimensões da matriz interseção. 
        print (str(ordem_matriz1+ordem_matriz2 - len(matriz_intersecao)) + ' x ' + str(ordem_matriz1+ordem_matriz2- len(matriz_intersecao[0])))
    else:
        fim_da_entrada = True