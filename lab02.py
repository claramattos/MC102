nome_canal = input()
n = int(input ())
l2018 = []
l2019 = []
l2020 = []

for i in range (n):
    data = input ()
    visualizacoes = int(input ())
    data_separada = data.split ('-')
    if data_separada[0] == '2018':
        l2018.append (visualizacoes)
    if data_separada[0] == '2019':
        l2019.append (visualizacoes)
    if data_separada[0] == '2020':
        l2020.append (visualizacoes)

soma_2018 = sum (l2018)
soma_2019 = sum (l2019)
soma_2020 = sum (l2020)
total_de_views = soma_2020+soma_2019+soma_2018

if total_de_views == 0:
    media_visualiizacoes = 0
else:
    media_visualiizacoes = total_de_views/(len(l2018) + len (l2019) + len(l2020))

print ('Canal: ' + nome_canal)
print ('Total de views do trienio: ' + str(total_de_views))
print ('Media de views do trienio: %.2f' %media_visualiizacoes)

print('\n' + '2018' + '\n' + "Total: " + str(soma_2018))
if total_de_views == 0:
    print ('Porcentagem das views do trienio: indeterminada')
else:
    print('Porcentagem das views do trienio: %.2f' %(soma_2018*100/total_de_views))
print ('Media: %.2f' %(soma_2018/len(l2018)))

print('\n' + '2019' + '\n' + "Total: " + str(soma_2019))
if total_de_views == 0:
    print ('Porcentagem das views do trienio: indeterminada')
else:
    print('Porcentagem das views do trienio: %.2f' %(soma_2019*100/total_de_views))
print ('Media: %.2f' %(soma_2019/len(l2019)))

print('\n' + '2020' + '\n' + "Total: " + str(soma_2020))
if total_de_views == 0:
    print ('Porcentagem das views do trienio: indeterminada')
else:
    print('Porcentagem das views do trienio: %.2f' %(soma_2020*100/total_de_views))
print ('Media: %.2f' %(soma_2020/len(l2020)))