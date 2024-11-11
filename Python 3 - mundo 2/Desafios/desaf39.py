import datetime
try:
    ano = int(input('Ano de nascimento: '))
    hoje = datetime.date.today().year
    reserva = hoje - ano
    if reserva < 18:
        falta = 18 - reserva
        alis = hoje + falta
        print(f'Quem nasceu em {ano} tem {reserva} anos em {hoje}.\nAinda faltam {falta} anos para o alistamento\nSeu alistamento será em {alis}.')
    elif reserva == 18:
        print(f'Quem nasceu em {ano} tem {reserva} anos em {hoje}.\nVocê tem que se alistar IMEDIATAMENTE!')
    elif reserva > 18:
        falta = reserva - 18
        alis = hoje - falta
        print(f'Quem nasceu em {ano} tem {reserva} anos em {hoje}.\nVocê já deveria ter se alistado há {falta} anos.\nSeu alistamento foi em {alis}.')
except:
    print('Valor errado, tente novamente!')
