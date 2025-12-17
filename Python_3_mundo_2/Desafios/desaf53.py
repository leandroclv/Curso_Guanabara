frase = str(input('Digite uma frase: ')).strip().upper() #strip - retira os espaços antes e depois, upper passa tudo para maiusculo
palavra = frase.split() # esse comando separa as palavras da frase em uma lista
junto = ''.join(palavra) # este comando junta as palavras em uma string retirando os espaços
inverso = ''#comça com nada
for letra in range(len(junto)-1, -1, -1): #aqui foi feito o inverso da string
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto: #se a string é igual a inverso é um palíndromo
    print('Temos um palíndromo!')
else:
    print('A letra digitada não é um palíndromo!')



'''aux = ""
for i in (range(0, len(frase))):
    aux += frase[i]
if aux.lower() == aux.lower() [::-1]: # fatiamento invertido
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')'''
