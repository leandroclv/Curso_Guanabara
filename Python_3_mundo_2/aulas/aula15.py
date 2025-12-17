'''cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('Acabou')'''

n = s = 0
while True: # loop infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break # Quebra o loop infinito
    s += n 
print(f'A soma vale {s:*^20}')#*complemento, ^centralizado e 20espaço, >alinhado a direita, <alinhado a esquerda


