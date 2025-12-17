money = float(input('Quanto dinheiro vc tem na carteira: R$'))
dolar = money / 3.27
print('Você pode converter seus R${:.2f} para US${:.2f}.'.format(money, dolar))