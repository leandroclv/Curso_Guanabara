import moeda
#ou você pode fazer from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}') #metade(p)
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')   #dobro(p)
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}') #aumentar(p, 10)