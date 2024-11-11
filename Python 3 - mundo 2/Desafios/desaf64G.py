number = 0
cont = 0
soma = 0
#number = cont = soma = 0
number = int(input('Digite um número [999 para parar]: '))
while number != 999:
    soma += number
    cont += 1
    number = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
