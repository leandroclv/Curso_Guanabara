def escreva(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'  {texto}')
    print('-' * tam)
    

text = str(input('Escreva o texto: '))
escreva(text)