num = [2, 5, 9, 1]
num[2] = 3
print(num)
#num[4] = 7 OBS: esse comando dará erro pois não existe o índice 4
num.append(7) #adiciona o elemento 7 na lista 
num.sort() #Ordena os elementos (crescente)
num.sort(reverse=True) #inverte a ordem dos elementos
num.insert(2, 8) #insere o elemento 8 no índice 2
num.insert(2, 2) #insere o elemento 2 no índice 2
num.remove(2) #esse comando percorre a lista atrás do elemento e assim que o encontra elimina e para de procurar
#num.pop() #retira o último elemento da lista
#num.pop(2) #retira o elemento do índice 2
if 4 in num: #caso trocarmos o elemento 4 pelo 5, o elemento 5 será apagado da lista
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} Elementos.') #fornece a quantidade de elementos na lista (len(num))

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v} ...', end='')
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Chegueiao final da lista.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

a = [2,3,4,7]
b = a #ligação da lista b com a lista a. Modificando uma modifica a outra (shallow copy)
b[2] = 8
b = a[:] #ou b = a.copy() - este comando manda pegar todos os elementos da lista a e copiar para a lista b e não possui ligação (deep copy)
b[1] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')