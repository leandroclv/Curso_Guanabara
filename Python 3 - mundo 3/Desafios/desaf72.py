number = int(input('Digite um número de 0 a 20: '))
numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
ext = ('zero', 'um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while number not in numeros:
    number = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número \033[0;34m{ext[number]}\033[m')
