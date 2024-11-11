print('-x-' * 20)
print('{:^60}'.format('Banco CEV'))
print('-x-' * 20)
saque = int(input('Digite o valor que você quer sacar: R$'))
print('O caixa possui cédulas de R$50, R$20, R$10 e R$1.')
total = saque
nota = 50
total_nota = 0
while True:
    if total >= nota:
        total -= nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        if nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_nota = 0
        if total == 0:
            break    
print('-x-' * 20)
print('Volte sempre ao banco CEV!\nTenha um bom dia!')