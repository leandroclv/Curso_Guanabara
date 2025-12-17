dista = float(input('Qual a distância de sua viagem? '))
if dista <= 200:
    preco = dista * 0.50
else:
    preco = dista * 0.45
print('Você está prestes a começar uma viagem de {}km.\nE o preço da sua passagem será de R${:.2f}'.format(dista, preco))
#preco = dista * 0.50 if dista <= 200 else dista * 0.45 // forma simplificada de fazer o if e else
