import moeda
#ou você pode fazer from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}') #metade(p)
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')   #dobro(p)
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}') #aumentar(p, 10)