tupla = []
par = []
count = 0
while count < 4:
    list = int(input('Digite um número: '))
    tupla.append(list)
    count += 1
tup = tuple(tupla)
print(f'Você digitou os valores {tup}')
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tup.index(3)+1}ª posição')
print(f'Os valores pares digitados foram ', end='')
for par in tup:
    if par % 2 == 0:
        print(par, end=' ',)


#Guanabara
'''num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''
