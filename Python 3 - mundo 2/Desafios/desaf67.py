while True:
    number = int(input('Quer ver a tabuada de qual valor (digite um número negativo para sair): '))
    print('-' * 30)
    if number < 0:
        break
    for c in range(1, 11):
        print(f'{number} x (c) = {number * c}')
    print('-'*30)
print('Programa tabuada encerrado. Volte sempre!')
