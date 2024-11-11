total = []
count = 1
for p in range(0, 5):
    peso = float(input(f'Digite o peso da {count}ª pessoa: '))
    total.append(peso)
    count +=1
print(f'O maior peso lido foi {max(total)}kg\nO menor peso lido foi {min(total)}kg.')

'''Guanabara
maior = 0 
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')'''
