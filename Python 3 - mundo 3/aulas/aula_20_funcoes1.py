'''print('-' * 30)
print('   Curso em vídeo    ')
print('-' * 30)
print('   Aprenda Python    ')
print('-' * 30)
print('   Gustavo Guanabara    ')
print('-' * 30)'''

'''def lin():
    print('-' * 30)
#programa principal
lin()
print('   Curso em vídeo    ')
lin()
print('   Aprenda Python    ')
lin()
print('   Gustavo Guanabara    ')
lin()

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
#programa principal
titulo('Curso em vídeo')
titulo('Aprenda Pyhton')
titulo('Gustavo Guanabara')

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2 
b = 1
s = a + b
print(s) 

def soma(a,b): #a e b são chamados de parêmetros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
#programa principal
soma(4,5)
soma(8,9)
soma(2,1)
soma(b = 39, a= 45)

def contador(*núm):
    #print(núm)
    #for valor in núm:
    #    print(f'{valor} ', end=' ')
    #print('FIM')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *=2
        pos += 1
valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    
soma(5,2)
soma(2,9,4)
