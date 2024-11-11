from time import sleep
number1 = int(input('Primeiro valor: '))
number2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opção: '))
    if opção == 1:
        soma = number1 + number2
        print(f'A soma entre {number1} + {number2} é {soma}')
    elif opção == 2:
        multi = number1 * number2
        print(f'A multiplicação entre {number1} X {number2} é {multi}')
    elif opção == 3:
        maior = max(number1, number2)
        print(f'Entre o número {number1} e o {number2} o maior número é o {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        number1 = int(input('Primeiro valor: '))
        number2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')