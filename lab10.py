suspeito, evidencias = {}, {}
dossie, principais_suspeitos = [], [] 
tem_suspeito,  fim_do_dossie, fim_das_evidencias = False, False, False

# Cria-se a base de dados (dossiê e evidencias).
while fim_do_dossie == False:
    caracteristica = input()
    if caracteristica == '-':
        dossie.append (suspeito)
        suspeito = {}
    # Aqui, começa a ser criado o dicionário de evidências.
    elif caracteristica == '--':
        dossie.append (suspeito)
        while fim_das_evidencias == False:
            caracteristica = input ()
            if caracteristica != '---':
                evidencias[(caracteristica.split(':'))[0]] = (caracteristica.split(':'))[1]
            else:
                fim_das_evidencias = True
                fim_do_dossie = True
    else:
        suspeito[(caracteristica.split(':'))[0]] = (caracteristica.split(':'))[1]

# Verifica-se se o conteúdo do dicionário de evidências está contido em algum dos dicionários do dossiê e, caso não, é impresso que não existem suspeitos identificados.
for k in range (len(dossie)):
    if set(evidencias.items()).issubset((dossie[k]).items()) :
        tem_suspeito = True
        principais_suspeitos.append (((dossie[k])['Nome']).strip())
    elif k == (len(dossie)-1) and tem_suspeito == False:
        print ('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).') 

# Caso existam suspeitos, sâo impressos em ordem alfabética.
if len(principais_suspeitos) > 1:
    print ('Suspeitos(as): \n' + '\n'.join(suspeito for suspeito in (sorted(principais_suspeitos))))
elif tem_suspeito==True:
    print ('Suspeito(a): \n' + principais_suspeitos[0]) 