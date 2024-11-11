try:
    valor = float(input('Preço das compras: R$'))
    pag = int(input('Forma de pagamento\n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nQual é a opção? '))
    if pag == 1:
        desc = valor - (valor * 0.10)
        print(f'Sua compra de R${valor:.2f} vai custar R${desc:.2f} no final.')
    elif pag == 2:
        desc = valor - (valor * 0.05)
        print(f'Sua compra de R${valor:.2f} vai custar R${desc:.2f} no final.')
    elif pag == 3:
        parce = int(input('Quantas parcelas? '))
        print(f'sua compra será parcelada em {parce}x de R${(valor/parce):.2f} sem juros\nSua compra vai custar R${valor:.2f} no final.')
    elif pag == 4:
        parce = int(input('Quantas parcelas? '))
        desc = valor + (valor * 0.2)
        print(f'Sua compra  será parcelada em {parce}x de R${desc/parce:.2f} com juros\nSua compra de R${valor:.2f} vai custar R${desc:.2f} no final!')
    else:
        print('Dados inválidos, tente novamente')
except:
    print('Dados inválidos, tente novamente!')

