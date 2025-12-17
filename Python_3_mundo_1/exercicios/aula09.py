frase = 'Curso em Vídeo Python'
print(frase[9:13]) #esse comando irá mostrar as letras da possição 9 a 13 sem mostrar a letra da posição 13
print(frase[1:15:2])#esse comando irá mostrar as letras da posição 1 a 15 pulando de 2 em dois 
print(frase.count('o'))#esse comando irá contar quantas letras o existem na variável
print(frase.upper().count('O'))#esse comando irá primeiro passar todas as letras para maiúsculo e depois contará quantos O possui
print(len(frase))#esse comando irá dizer quantos caracteres a variável possui (espaço conta como caracter)
print(len(frase.strip()))#esse comando retira os espaços desnecessários antes e depois
print(frase.replace('Python', 'Android'))#esse comando irá trocar a palavra Python pela palavra Android
frase = frase.replace('Ṕython', 'Android')#esse comando irá fazer a troca das palavras e salvará na variável
print('Curso' in frase)#esse comando irá procurar a palavra Curso na variável e encontrando retorna como True ou False
print(frase.find('Curso'))#esse comando irá procurar a palavra Curso e retornará com a posição desta palavra na variável
print(frase.lower().find('vídeo'))#esse comando irá passar todas as letras para minúsculo e depois procura-rá pela palavra vídeo
print(frase.split())#esse comando irá separar as palavras da variável e colocando em uma lista
dividido = frase.split()#coloquei as palavras em lista da variável frase em uma outra variável chamada dividido
print(dividido[0])#mandei mostrar o conteúdo da lista na posição 0
print(dividido[2][3])#mandei mostrar a treceira letra do conteúdo da lista na posição 2
