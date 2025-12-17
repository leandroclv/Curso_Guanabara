from random import randint
count = 0
print('=-'*15)
print('Vamos jogar par ou ímpar')
print('=-'*15)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end = ' ')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar' )
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            count += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {count} vezes.')
