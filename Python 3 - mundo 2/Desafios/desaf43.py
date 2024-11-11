try:
    peso = float(input('Qual é o seu peso? (Kg) '))
    altura = float(input('Qual a sua altura? (m) '))
    icm = peso / (altura ** 2)
    if icm < 18.5:
        print(f'O seu ICM é {icm:.2f}\nVocê está na faixa abaixo do peso!')
    elif icm >= 18.5 and icm < 25: #18.5 <= imc < 25
        print(f'O seu ICM é {icm:.2f}\nPARABÉNS, você está na faixa do peso ideal!')
    elif icm >= 25 and icm < 30: #25 <= imc < 30
        print(f'O seu ICM é {icm:.2f}\nVocê está na faixa de sobrepeso!')
    elif icm >= 30 and icm < 40: #30 <= imc < 40
        print(f'O seu ICM é {icm:.2f}\nVocê está na faixa de obesidade!')
    elif icm >= 40: #else
        print(f'O seu ICM é {icm:.2f}\nVocê está na faixa de obesidade mórbida, cuidado')
    else:
        print('Dados inválidos, tente novamente!')
except:
    print('Dados inválidos, tente novamente!')
