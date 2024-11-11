lista = []
while True:
    number = int(input('Digite um valor: '))
    cont = str(input('Quer continuar? [S/N] ')).split()[0]
    lista.append(number)
    if cont in 'nN':
        break
    #elif cont != str or cont not in 'sS':
        #print('Valor errado tente novamente')
    elif number in lista:
        print('Valor duplicado! Não vou adicionar ...')
    else:
        lista.append(number)
print(f'Você digitou os valores {lista.sort()}')