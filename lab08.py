def expresao_aritmetica (lista, indice): 
    ''' Função que realiza todas as expressões aritméticas da entrada.'''  
    for numero in range (indice, len(lista)):
        if lista[numero] == '+':
            # Após a expressão da lista ter sido resolvida, o valor obtido é inserido e a expressão inicial é removida da lista.
            lista.insert(numero+2, int(lista[numero-1])+ int(lista[numero+1]))
            lista.pop (numero-1), lista.pop (numero-1), lista.pop (numero-1)
            # Como a função envolve dar pop em elementos, o tamanho da lista é alterado e, ao ser rodado como 'range' no 'for', obtemos IndexError para os últimos valores de i (pois o tamanho da lista diminuiu e tais índices não existem mais). 
            # Dessa forma, assim que se um operador é encontrado, o loop é encerrado e a função é chamada novamente.
            expresao_aritmetica(lista, indice)
            break
        elif lista[numero] == '-':
            lista.insert(numero+2, int(lista[numero-1])- int(lista[numero+1]))
            lista.pop (numero-1), lista.pop (numero-1), lista.pop (numero-1), expresao_aritmetica(lista, indice)
            break

def booleanas_simples (lista, indice):
    ''' Função que realiza todas as expressões booleanas simples da entrada.'''
    for numero in range (indice, len(lista)):
        if lista [numero] != '==' and lista [numero] != '!=' and lista [numero] != '<' and lista [numero] != '>' and lista [numero] != '<=' and lista [numero] != '>=':
            pass
        else:
            # Ao inserir uma booleana simples na função int(), retorna-se 0 para False e 1 para True.
            if lista[numero] == '==':
                lista.insert(numero+2, int(int(lista[numero-1]) == int(lista[numero+1])))
            elif lista[numero] == '!=':
                lista.insert(numero+2, int(int(lista[numero-1]) != int(lista[numero+1])))
            elif lista[numero] == '<':
                lista.insert(numero+2, int(int(lista[numero-1]) < int(lista[numero+1])))
            elif lista[numero] == '>':
                lista.insert(numero+2, int(int(lista[numero-1]) > int(lista[numero+1])))
            elif lista[numero] == '<=':
                lista.insert(numero+2, int(int(lista[numero-1]) <= int(lista[numero+1])))
            elif lista[numero] == '>=':
                lista.insert(numero+2, int(int(lista[numero-1]) >= int(lista[numero+1])))

            lista.pop (numero-1), lista.pop (numero-1), lista.pop (numero-1), booleanas_simples(lista, indice)
            break

def booleanas_compostas (lista, indice):
    ''' Função que realiza todas as expressões booleanas simples da entrada.'''
    for numero in range (indice, len(lista)):
        if lista[numero] != 'AND' and lista[numero] != 'OR':
            pass
        else:
            if lista[numero] == 'AND':
                lista.insert(numero+2, int(int(lista[numero-1]) and int(lista[numero+1])))
            elif lista[numero] == 'OR':
                lista.insert(numero+2, int(int(lista[numero-1]) or int(lista[numero+1])))

            lista.pop (numero-1), lista.pop (numero-1), lista.pop (numero-1), booleanas_compostas(lista, indice)
            break

def cria_variaveis (lista):
    '''Função que cria as variáveis e as acrescenta ao dicionário 'variaveis' assim que inicializadas.'''
    global variavel_criada, erro_sintaxe
    # Caso o segundo elemento da entrada seja o caracter '=', a entrada está, obrigatoramente, definindo uma variável.
    if lista[1] == '=':
        # Verifica-se se o nome inserido para a variável é permitido (se o primeiro caractere é uma letra e se todos os caracteres são alfanuméricos).
        if lista[0][0].isalpha() and lista[0].isalnum():
            # Procura-se alguma outra variável na expressão.
            verifica_variaveis(lista, 2)
            # Caso todas as variáveis na expressão já tenham sido definidas, resolvem-se as expressões após o símbolo de '=' e a variável e seu valor são adicionadas ao dicionário.
            if not erro_referencia:
                variavel_criada = True
                # As funçoes sempre serão chamadas nesta ordem de solução.
                expresao_aritmetica(lista, 2), booleanas_simples (lista, 2), booleanas_compostas(lista, 2)
                variaveis[lista[0]] = lista[2]  
        else:
            # Caso o nome da vaiável não seja permitido, o programa informa o usuário.
            print ('Erro de sintaxe: ' + lista[0] + ' nao e um nome permitido para uma variavel.')
            erro_sintaxe = True

def verifica_variaveis (lista, indice):
    '''Função que verifica as variáveis existentes em uma expressão a partir de um certo índice, atribuindo o valor correspondente àquelas que já foram definidas e informando o usuário caso alguma ainda não tenha sido definida.'''
    global erro_referencia
    for numero in range (indice, len(lista)):
        # Caso um elemento da lista tenha seu primeiro algarismo como letra e o elemento não seja 'OR' ou 'AND', ele com certeza será uma variável.
        # Desse modo, caso a variável seja uma chave do dicionário de variáveis, seu nome na lista é substituído por seu valor armazenado no dicionário.
        if lista[numero][0].isalpha() and lista[numero] != 'AND' and lista[numero] != 'OR' and lista[numero] in variaveis:
            lista[numero] = variaveis[lista[numero]]
        # Caso a variável não seja uma chave do dicionário e não tenha ocorrido um erro de sintaxe anteriormente (pois a mensagem do erro de sintaxe tem preferência sobre a mensagem de erro de referência), é exibida a mensagem de erro de referência. 
        elif lista[numero][0].isalpha() and lista[numero] != 'AND' and lista[numero] != 'OR' and  lista[numero] not in variaveis and erro_sintaxe == False:
            print ('Erro de referencia: a variavel '+ lista[numero] +' nao foi definida.')
            erro_referencia = True
            return

# É criado o dicionário onde serão armazenadas as variáveis e seus respectivos valores. 
variaveis = {}          

while True:
    try:
        # A entrada é armazenada em lista e as booleanas recebem seus valores iniciais.
        entrada = (input()).split(' ')
        variavel_existente = True
        variavel_criada, erro_sintaxe, erro_referencia = False, False, False

        # Caso a entrada tenha somente um componente, esse será obrigatóriamente o nome de uma variável. 
        if len(entrada) == 1:
            # É chamada a função verifica_variaveis e, caso a variável inserida seja conhecida (não tenha ocorrido um erro de referência), é impresso seu valor.
            verifica_variaveis(entrada, 0)
            if not erro_referencia:
                print (entrada[0])
                
        else:
            # Caso a entrada não seja o nome de uma variável, é chamada a função cria_variáveis para averiguar se uma variável está sendo criada.
            cria_variaveis (entrada)
            # Caso uma variável não estiver sendo criada, não tivermos obtido um erro de sintaxe nem um de referência, chamamos a função verifica variáveis para toda a entrada.
            if variavel_criada == False and not erro_sintaxe and not erro_referencia:
                verifica_variaveis(entrada, 0)
            # Caso a função verifica variáveis não tenha retornado um erro de referência, resolvemos as equações (obrigatoriamente nessa ordem).
            if variavel_criada == False and not erro_sintaxe and not erro_referencia:
                    expresao_aritmetica(entrada, 0)
                    booleanas_simples(entrada, 0)
                    booleanas_compostas(entrada, 0)
            # Uma vez resolvidas as expressões da entrada, é impresso o resultado final.
            if len(entrada) == 1 and not erro_referencia and not erro_sintaxe:
                print (entrada[0])
            
    except EOFError:
        # Assim que finda a entrada, é impressa a mensagem de tchau.
        print("Encerrando... Bye-bye.")
        break 