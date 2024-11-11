velo = float(input('Qual é a velocidade atual do carro? '))
if velo > 80:
    multa = (velo - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é 80km/h\nVocê deve pagar uma multa de R${:.2f}!\nTenha um bom dia! Dirija com segurança!'.format(multa)) 
print('Tenha um bom dia! Dirija com segurança!')
