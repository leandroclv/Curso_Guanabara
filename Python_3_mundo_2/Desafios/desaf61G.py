print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = primeiro
cont = 1
while cont <= 10:
    print(f'{termos} -> ', end='')
    termos += razao
    cont += 1
print('Fim')
    