from random import randint
comp = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
cont = 0
while not acertou: 
    numb = int(input('Qual o seu palpite? '))
    cont += 1
    if numb == comp:
        acertou = True
    else:
        if numb < comp:
            print('Mais... Tente novamente!')
        elif numb > comp:
            print('Menos... Tente novamente')
print(f'PARABÉNS! Você conseguiu me vencer depois de {cont} tentativas!')
