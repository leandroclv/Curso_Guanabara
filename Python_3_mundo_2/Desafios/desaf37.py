try: 
    numb = int(input('Digite um número inteiro: '))
    base = (input('Escolha qual será o sistema de conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL- hexadecimal\nSua opção: '))
    if base == '1':
        sist = format(numb, 'b')
        print(f'{numb} convertido para BINÁRIO é igual a {sist}')
    elif base == '2':
        sist = format(numb, 'o')
        print(f'{numb} convertido para OCTAL é igual a {sist}')
    elif base == '3':
        sist = format(numb, 'x')
        print(f'{numb} convertido para HEXADECIMAL é igual a {sist}')
    else:
        print('Número inválido')
except:
    print('Número inválido tente novamente')