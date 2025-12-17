primeiro = int(input('Primeiro elemento: '))
razao = int(input('Razão: '))
ultimo = primeiro + (10 - 1) * razao
ultimo += 1
print('='*20)
print('10 termos de uma PA')
print('='*20)
for var in range(primeiro, ultimo, razao):
    print(var, end=' -> ')
print('ACABOU')