try:
    print('Analisador de Triângulos')
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))
    if (a + b > c) and (a + c > b) and (b + c > a):
        print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
        if a == b == c:
            print('EQUILÁTERO!')
        elif a != b and a != c and b != c:
            print('ESCALENO!')
        else:
            print('ISÓCELES')
    else:
        print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
except:
    print('Dados inválidos, tente novamente!')
