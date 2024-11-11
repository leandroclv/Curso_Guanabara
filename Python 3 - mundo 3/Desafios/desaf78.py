'''number = []
cont = 0
while cont < 5:
    num = int(input(f'Digite um valor para a posição {cont}: '))
    number.append(num)
    cont += 1
maior = max(number)
menor = min(number)
print('=-' * 30)
print(f'Você digitou os valores {number}. \nO maior valor digitado foi o {maior} nas posições {number.index(maior)} \nO menor valor digitado foi o {menor} na posição {number.index(menor)}.')'''

#Guanabara
listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai=men=listanum[0]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*50)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi o {mai} nas posições', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {men} nas posições', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
