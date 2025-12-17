preco = float(input('Qual o preço do produto: '))
desc = preco - (preco * 0.05)
print('O preço do produto (R${}) ficará R${:.2f} com 5% de desconto'.format(preco, desc))