from math import sqrt
oposto = float(input('Qual o comprimento do cateto oposto: '))
adjace = float(input('Qual o comprimento do cateto adjacente: '))
hipot = sqrt(oposto ** 2 + adjace ** 2)
print('O comprimento da hipotenusa é {:.2f}.'.format(hipot))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))