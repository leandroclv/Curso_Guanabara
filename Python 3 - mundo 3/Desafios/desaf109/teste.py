import moeda
#ou você pode fazer from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}') #metade(p)
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')   #dobro(p)
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}') #aumentar(p, 10)
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')