def retira_maior_quadrado (altura, largura):
    '''Função recursiva que, dadas as dimensões de uma área, retira o maior quadrado de lado potência de 2 possível contido na área e retorna duas outras áreas para a função.'''
    # Caso a altura ou a largura sejam 0, não existe área.
    if altura == 0 or largura == 0:
        return
    # Ao se deparar com um quadrado de lado 1, soma-se um ao número de submagias de nível 0, pois 2^0 = 1.
    # Caso ainda não exista essa chave no dicionário, ela é criada.
    elif altura == largura == 1:
        if numero_de_submagias.get(0, False) == False:
            numero_de_submagias[0] = 0
        numero_de_submagias [0] +=  1
        return
    # Criam-se duas váriaveis x e y, tal que y sempre recebe o menor valor entre as duas dimensões.
    elif altura >= largura:
        x, y = altura, largura
    elif largura > altura:
        x, y = largura, altura
    # Calcula-se qual a maior potência de 2 possível menor ou igual ao menor lado da área e, daí, retira-se da área o quadrado de lado igual a potência calculada.
    # Soma-se um ao um ao número de submagias de nível igual à maior potência encontrada e retorna-se a função para as duas áreas restantes sem o quadrado retirado (dado que, caso o y seja igual à maior potência encontrada, uma delas será 0).
    if numero_de_submagias.get(nivel_da_submagia (y,0), False) == False:
        numero_de_submagias[nivel_da_submagia (y,0)] = 0
    numero_de_submagias [nivel_da_submagia (y,0)] +=  1
    retira_maior_quadrado (x - 2**(nivel_da_submagia (y,0)), y), retira_maior_quadrado (2**(nivel_da_submagia (y,0)), y - 2**(nivel_da_submagia (y,0)))

def nivel_da_submagia (numero, k):
    '''Função que encontra a maior potência de base 2 possível menor ou igual ao número fornecido.'''
    # O valor k inicial passado sempre será 0.
    while 2**k <= numero:
        k += 1
    return k - 1

# O dicionário numero_de_submagias armazena a quantidade de vezes que cada submagia foi conjurada.
numero_de_submagias = {}
total_pm, total_submagias = 0, 0
dimensoes = (input ()).split (' ')
altura, largura = int(dimensoes[0]), int(dimensoes[1])

# É chamada a função de retirar maior quadrado com as dimensões inicias fornecidas pelo usuário
retira_maior_quadrado (altura, largura)

print ("---\nGrimorio de Teraf L'are\n---")
for chave in sorted(numero_de_submagias):
    # São somados os valores de PM e total de submagias de todas as submagias conjuradas.
    total_submagias += numero_de_submagias[chave]
    total_pm += 2**chave * numero_de_submagias[chave]
    # São impressos o número de submagias conjuradas para cada nível, o total de submagias conjuradas e o total de PM gasto.
    print (str(numero_de_submagias[chave]) + ' submagia(s) de nivel ' + str(chave))
    
print ('---\nTotal de submagia(s) conjurada(s): ' + str(total_submagias) + '\n' + 'Total de PM gasto: ' + str(total_pm) + '\n---')