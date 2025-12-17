number = int(input('Digite um número: '))
tot = 0
for p in range(1, number + 1):
    if number % p == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{p}', end = ' ')
print(f'\n\033[mO número {number} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
