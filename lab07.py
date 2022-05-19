def codifica_LinhaImpar (mensagem):
    LinhaImpar_codificada = ''
    for i in range (len(mensagem)):
        hex_mensagem = hex(ord(mensagem[i]))
        hex_mensagem = hex_mensagem.upper()
        LinhaImpar_codificada += hex_mensagem[2:(len(hex_mensagem))].zfill(enxerto)
    return LinhaImpar_codificada

def codifica_LinhaPar (mensagem):
    LinhaPar_codificada = ''
    mensagem = mensagem[::-1]
    for i in range (len(mensagem)):
        oct_mensagem = (oct(ord(mensagem[i]))).upper()
        LinhaPar_codificada += oct_mensagem[2:(len(oct_mensagem))].zfill(enxerto)
    return LinhaPar_codificada

def decodifica_LinhaImpar (codigo):
    LinhaImpar_separada = []
    LinhaImpar_decodificada = ''
    for i in range (0,len(codigo)-enxerto+1,enxerto):
        LinhaImpar_separada.append(codigo[i:i+enxerto])
    for z in range (len(LinhaImpar_separada)):
        LinhaImpar_decodificada += chr(int(LinhaImpar_separada[z],16))
    return LinhaImpar_decodificada

def decodifica_LinhaPar (codigo):
    LinhaPar_separada = []
    LinhaPar_decodificada = ''
    for i in range (0,len(codigo)-enxerto+1,enxerto):
        LinhaPar_separada.append(codigo[i:i+enxerto])
    for z in range (len(LinhaPar_separada)):
        LinhaPar_decodificada += chr(int(LinhaPar_separada[z],8))
    return LinhaPar_decodificada[::-1]

especificacoes = (input()).split (' ')
modo = int(especificacoes[0])
enxerto = int (especificacoes[1])
n_de_linhas = int(especificacoes[2])

for k in range (n_de_linhas):
    string = input()
    if modo == 1: 
        if (k+1)%2 == 0:
            print (codifica_LinhaPar(string))
        else:
            print (codifica_LinhaImpar(string))
    elif modo == 2:
        if (k+1)%2 == 0:
            print (decodifica_LinhaPar(string))   
        else:
            print (decodifica_LinhaImpar(string))