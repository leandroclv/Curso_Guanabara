soma_preco = menor_preco = prod_mil = count = 0
barato = ''
print('-*-' * 4 + 'Loja Super Baratão' + '-*-' * 4)
while True:
    produto = str(input('Produto: '))
    preco = float(input('Qual o preço: R$'))
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    count += 1
    soma_preco += preco
    if preco > 1000:
        prod_mil += 1
    if count == 1 or preco < menor_preco:
        menor_preco = preco
        mais_barato = produto
    if cont == 'N':
        break
print('-*-' * 4 + 'Fim do Programa' + '-*-' * 4)
print(f'O total da compra foi R${soma_preco:.2f}')
print(f'Temos {prod_mil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi \033[0;31m{mais_barato}\033[m que custa R${menor_preco:.2f}')
