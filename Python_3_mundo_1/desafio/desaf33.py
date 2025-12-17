n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 > n3:
    print('O maior número é o {}.'.format(n1))
if n2 > n1 > n3:
    print('O maior número é o {}.'.format(n2))
if n3 > n1 > n2:
    print('O maior número é o {}.'.format(n3))
if n1 < n2 < n3:
    print('O menor número é o {}.'.format(n1))
if n2 < n1 < n3:
    print('O menor número é o {}.'.format(n2))
if n3 < n1 < n2:
    print('O menor número é o {}.'.format(n3))

'''menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c'''