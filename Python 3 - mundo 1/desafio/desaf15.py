dia = int(input('Quantos dias alugados: '))
km = int(input('Quantos km rodados: '))
preco = dia * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(preco))