from datetime import date # importar da biblioteca datetima o método date para pegar o ano em que estou realizando este desafio
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #essa instrução vai pegar o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é um ano bissexto!')
else:
    print('Este ano não é um ano bissexto!')