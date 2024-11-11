import datetime
maior = 0
menor = 0
for a in range(1, 8):
    age = int(input(f'Digite em que ano a {a} pessoa nasceu: '))
    hoje = datetime.datetime.today().year
    idade = hoje - age
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{menor} ainda não atingiram a maioridade e {maior} já atingiram a maioridade.')
