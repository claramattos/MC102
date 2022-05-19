entrada = input ()
senha = entrada.split (' ')
n_tentativas = int(senha[1])
senha_correta = False

def semelhanca_senhas (senha1, senha2):
    ''' Indica o número de algarismos iguais em mesma posição de duas strings '''
    soma = 0
    z = 0
    while z < len (senha1):
        if int(senha1[z]) == int(senha2[z]):
            soma += 1
        z += 1
    return soma 

def comprimentos_iguais (tentativa, k):
    ''' Usada quando o número de algarismos da senha esperada e da senha inserida é igual, a função indica que a senha não está correta, mostrando a semelhança entre a senha inserida e a desejada '''
    print ('Senha incorreta')
    print ('Semelhanca: ' + str(semelhanca_senhas(tentativa, senha[0])))
    print ('Tentativas restantes: '+ str(k)+ '\n')

def comprimentos_diferentes (k):
    ''' Avisa o usuário que a quantidade de algarismos das duas senhas é diferente e indica a quantidade de tentativas restantes '''
    print ('Senha incorreta' + '\n' + 'Semelhanca: Erro: quantidade de digitos incongruente' + '\n' + 'Tentativas restantes: '+ str(k) + '\n')

for k in range (n_tentativas-1, -1,-1):
    tentativa = input ()
    if int(senha[0]) == int(tentativa):
        print ('Senha reconhecida. Desativando defesas...' )
        senha_correta = True
        break
    elif len(senha[0]) == len (tentativa):
        comprimentos_iguais (tentativa,k)
    else:
        comprimentos_diferentes (k)
    if k == 0 and senha_correta == False:
        print ('Tentativas esgotadas. Acionando defesas...')