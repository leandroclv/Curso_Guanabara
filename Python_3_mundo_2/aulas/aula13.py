for c in range (1, 6): #aqui o laço irá imprimir a palavra oi 5x
    print('oi')
print('Fim')

for c in range (1, 7): #aqui o laço irá imprimir do número 1 até o 6
    print(c)
print('FIM')

for c in range (6, 0, -1):#aqui o laço irá fazer contagem regressiva (-1 quer dizer que irá tirar 1 dos números) de 6 a 1
    print(c)
print('FiM')

for c in range (0, 7, 2):#aqui o laço irá imprimir do número 0 ao 6 de dois em dois (o número 2 indica isso)
    print(c)
print('fiM')

n = int(input('Digite um número: '))
for c in range (0, n):#aqui o laço irá imprimir do número 0 até o que o usuário indicar, no entanto não sairá o número final pois o computador começa do 0 e não do 1. Se vc colocar o 5 por exemplo, irá aparecer do 0 até o 4 para acertar isso podemos colocar n + 1 e sairá do 0 ao número escolhido
    print(c)
print('fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p): #aqui o laço irá ter os parâmetros inseridos pelo usuário (no parâmetro fim (f+1) para imprimir o número escolhido)
    print(c)
print('fim')

for c in range (0, 3):#nesse laço a variável n vai fazer a pergunta 3 vezes
    n = int(input('Digite um valor: '))
print('fim')

s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s +=n
print(f'O somatório de todos os valores foi {s}')
