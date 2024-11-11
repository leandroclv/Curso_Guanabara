def area(larg, comp):
    area_tot = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area_tot}m²')


print('Controle de terrenos')
print('-=' * 30)
larg = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(larg, comp)
    