salario = float(input('Qual é o salário do funionário? R$'))
if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print('O seu salário de R${:.2f} teve um aumento de 15% valendo agora R${:.2f}.'.format(salario,aumento))