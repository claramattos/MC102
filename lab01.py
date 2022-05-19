def converteTemp (F):
    celsius = (5*F - 160)/9
    return celsius

material = input()
pFusao = float(input())
pEbulicao = float (input())
temp = float (input())
tempCelsius =  round(converteTemp(temp),2)

print ("Material: " + material)
print ("Ponto de fusao (Celsius): " + str("%.2f" %pFusao))
print ("Ponto de ebulicao (Celsius): " + str("%.2f" %pEbulicao))
print ("Temperatura atual (Celsius): " + str("%.2f" %tempCelsius))

if tempCelsius >=  pEbulicao:
    print ("Estado fisico do material: Gasoso")
else:
    if tempCelsius < pFusao:
        print("Estado fisico do material: Solido")
    else:
        print ("Estado fisico do material: Liquido")