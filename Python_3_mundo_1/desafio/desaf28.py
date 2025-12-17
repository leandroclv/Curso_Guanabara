#from random import randint // importar um random para números inteiros
#computador  = randint(0, 5) // expecifica quais números serão escolhidos aleatóriamente
#print('Pensei no número...'.format(copmutador)) // conferir se está funcionando e quais os números que o programa escolheu
from time import sleep #importar da bibliotece time o método sleep que faz o programa esperar alguns segundos para passar para o próximo passo
import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numb = int(input('Em que número pensei? '))
lista = [0, 1, 2, 3, 4, 5]
comp = random.choice(lista)
print('PROCESSANDO...')
sleep(3) #vai fazer o programa esperar 3 segundos para passar para o próximo passo
if numb == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}! Tente novamente!'.format(comp, numb))
