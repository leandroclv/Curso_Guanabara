number = int(input('Digite um número: '))
u = number // 1 % 10 #pego o número divido inteiro por 1 e depois divido por 10 e pego o resto do número
d = number // 10 % 10 #pego o número divido inteiro por 10 e depois divido por 10 e pego o resto do número
c = number // 100 % 10 #pego o número divido inteiro por 100 e depois divido por 10 e pego o resto do número
m = number // 1000 % 10 #pego o número divido inteiro por 1000 e depois divido por 10 e pego o resto do número
#o número pode ser fatiado e colocado no programa
print('O número digitado foi: {}'.format(number))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))