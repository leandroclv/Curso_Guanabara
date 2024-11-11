print('\033[1;31;43mOlá, Mundo!\033[m') #o 033[m no final é para o fundo ficar somente na frase e não na linha toda

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;31;43m', nome, '\033[m'))