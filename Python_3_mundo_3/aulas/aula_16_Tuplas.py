lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita') #Tuplas são imutáveis
#lanche[1] = 'refrigerante' #vai dar erro pq tupla são imutáveis
print(len(lanche)) # mostra quantos elementos a tupla possui
for comida in lanche: #tem a mesma função do 'for' abaixo sem usar o range
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)): #tem a mesma função do 'for' abaixao, mas utilizando o range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche): #mesma função dos outros for, mas coloca a posição com a primeira
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(sorted(lanche)) #mostre o lanche em ordem (não muda a tuplas só muda a ordem que mostra)

a = (2,5,4,)
b = (5,8,1,2)
c = b + a #junta as duas tuplas e forma uma terceira
print(c)
print(len(c))
print(c.count(5))# conta quantos 5 aparecem na tupla
print(c.index(8))# em que posição está o número 8 na tupla
print(c.index(5, 1))#não vai mostrar o 5 na posição 0, pois vai começar a procurar da posição 1 para frente

pessoa = ('Gustavo', 39, 'M', 99.88) #a tupla pode ter dados de tipos diferentes
#del(pessoa)#você pode apagar a tupla totalmente
#print(pessoa)#vai dar erro pq no comando passado a tupla pessoa foi deletada


