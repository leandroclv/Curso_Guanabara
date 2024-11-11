try:
    numb1 = int(input('Digite um número inteiro: '))
    numb2 = int(input('Digite outro número inteiro: '))
    if numb1 > numb2:
        print('O primeiro valor é maior!')
    elif numb1 < numb2:
        print('O segundo valor é maior!')
    else:
        print('Não existe valor maior, os dois são iguais')
except:
    print('Valor errado, tente novamente!')
