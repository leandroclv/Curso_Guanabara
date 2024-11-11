nome = str(input('Digite o seu nome completo: ')).strip()
name = nome.split()
print('Prazer em te conhecer')
print('Seu primeiro nome é {}'.format(name[0].title()))
print('Seu último nome é {}'.format(name[-1].title()))
#print('Seu último nome é {}'.format(nome[len(nome)-1])) // feito pelo Guanabara