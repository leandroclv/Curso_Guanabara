largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A sua parede tem {}m² de área e você irá utilizar {}L de tinta'.format(area, tinta))