def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        numb = str(input(msg))
        if numb.isnumeric():
            valor = int(numb)
            ok = True
        else:
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

numb = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numb}')