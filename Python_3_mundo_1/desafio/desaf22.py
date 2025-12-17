nome = input('Qual o seu nome completo: ')
#nome = str(input('Qual o seu nome completo: ')).strip() //nesse comando foi forçado a resposta ser em string e o final retira os espaços antes e depois
divi = nome.split()
first = divi[0]
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) //nesse comando o Guanabara contou todas as letras com espaço e contou quantos espaços tem e depois diminuiu um por outro dando o número de caracteres sem os espaços
print('Seu primeiro nome é {} e ele tem {} letras'.format(first.capitalize(), len(first)))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) // nesse comando o Guanabara pede para encontrar o primeiro espaço e retorna com o número depois das letras do primeiro nome
#separa = nome.split() // esse comando irá colocar os nomes em uma lista separados
#print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0]))) // esse comando irá mostrar primeiro o elemento 0 da lista e depois o tamanho do elemento 0 da lista