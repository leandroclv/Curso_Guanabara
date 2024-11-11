from time import sleep

'''def contador(ini, fim, pas):
    for i in range(ini, fim + pas, pas):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('Fim!')

def lin():
    print('-=' * 25)

lin()
print('Contagem de 1 até 10 de 1 em 1')
for i in range(1, 11):
    print(i, end=' ', flush=True)
    sleep(0.5)
print('Fim!')
lin()
print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, -1, -2):
    print(i, end=' ', flush=True)
    sleep(0.5)
print('Fim!')
lin()
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
lin()
print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
contador(ini, fim, pas)'''

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        print('Erro, pois o 0 não pode ser um passo, tente novamente')
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(1)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(1)
            cont -= p
        print('FIM!')

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)