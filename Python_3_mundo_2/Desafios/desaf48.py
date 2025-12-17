soma = 0
cont = 0 #guana
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c #um acumulador soma um valor mais outro
        cont += 1 #um contador soma um valor mais um - idéia do Guana
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
