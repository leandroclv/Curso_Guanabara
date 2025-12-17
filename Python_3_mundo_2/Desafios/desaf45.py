from time import sleep 
import random
try:
    print('Vamos jogar Jokenpô!')
    numb = int(input('Escolha qual você vai querer:\n1- Pedra\n2- Papel\n3- Tesoura\n: '))
    lista = [1,2,3]
    comp = random.choice(lista)
    print('Jokenpô...')
    sleep(2)
    if numb == 1 and comp == 3:
        print('Você escolheu Pedra e o computador Tesoura. Parabéns você ganhou!')
    elif numb == 1 and comp == 2:
        print('Você escolheu Pedra e o computador Papel. Desculpe você perdeu!')
    elif numb == 2 and comp == 1:
        print('Você escolheu Papel e o computador Pedra. Parabéns você ganhou!')
    elif numb == 2 and comp == 3:
        print('Você escolheu Papel e o computador Tesoura. Desculpe você perdeu!')
    elif numb == 3 and comp == 2:
        print('Você escolheu Tesoura e o computador Papel. Parabéns você ganhou!')
    elif numb == 3 and comp == 1:
        print('Você escolheu Tesoura e o computador Pedra. Desculpe você perdeu! ')
    elif numb == comp:
        print('Vocês escolheram o mesmo e empataram. Tente novamente!')
    else:
        print('Pensou que tinha me enganado hein!\nDados inválidos, tente novamente!')
except:
    print('Dados inválidos, tente novamente!')


