count = hom = mul = 0
while True:
    print('-*-' * 30)
    print('Cadastre uma pessoa')
    idade = int(input('Qual a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        count += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {count}')
print(f'Ao todo temos {hom} Homens cadastrados')
print(f'e temos {mul} mulheres com menos de 20 anos')