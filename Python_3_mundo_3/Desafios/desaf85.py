'''num = []
par = []
imp = []
count =1
for c in range(0,7):
    num.append(int(input(f'Digite o {count}° valor: ')))
    count +=1
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
        par.sort()
    else:
        imp.append(v)
        imp.sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {imp}')'''

#Guanabara
num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
