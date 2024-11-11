from random import randint
tupla = []
count = 0
while count < 5:
    list = randint(0, 10)
    tupla.append(list)
    count += 1
tup = tuple(tupla)
print(f'Os valores sorteados foram = {tup}')
print(f'O maior valor sorteado foi o {max(tup)}')
print(f'O menor valor sorteado foi o {min(tup)}')


#Guanabara sem a repetição
'''from random import randint
number = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in number:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(number)}')
print(f'O menor valor sorteado foi {min(number)}')'''



