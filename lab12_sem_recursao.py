from math import sqrt
dimensoes = input()
numero_de_formas = int(input())
formas = []

linhas = int((dimensoes.split(' '))[0])
colunas = int((dimensoes.split(' '))[1])
matriz = [['-' for x in range(colunas)] for y in range(linhas)]

for k in range (numero_de_formas):
    formas.append(input().split(' '))

def desenha_circulo (matriz, i, j, raio):
    for w in range (colunas):
        for z in range (linhas):
            if sqrt(((i-z)**2)+(j-w)**2)<= raio:
                (matriz[z])[w] = 'x'
    return matriz

def desenha_quadrado(matriz, i, j, lado):
    for w in range (colunas):
        for z in range (linhas):
            if i-(lado//2)<=z<=i+(lado//2) and j-(lado//2)<=w<=j+(lado//2):
                matriz[z][w] = 'x'
    return matriz

for k in range (len(formas)):
    if formas[k][0] == 'quadrado':
        desenha_quadrado (matriz, int(formas[k][1]), int(formas[k][2]),int(formas[k][3]))
    if formas[k][0]== 'circulo':
        desenha_circulo (matriz, int(formas[k][1]), int(formas[k][2]),int(formas[k][3]))

for line in matriz:
        print (' '.join(map(str, line)))
