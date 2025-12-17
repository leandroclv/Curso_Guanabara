ext = ('zero', 'um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number <= 20: 
        break
    print('Tente novamente. ',end=' ')
print(f'Você digitou o número {ext[number]}')
