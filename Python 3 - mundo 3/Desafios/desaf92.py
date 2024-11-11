import datetime
cadastro = {}
hoje = datetime.date.today().year
cont = 0
while cont<1:
    cadastro['nome'] = str(input('Nome: ')).capitalize()
    idade = int(input('Ano de nascimento: '))
    cadastro['idade'] = hoje - idade
    cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        print('-=' * 50)
        print(cadastro)
        print(f'Nome tem valor {cadastro["nome"]}.')
        print(f'Idade tem o valor {cadastro["idade"]} anos.')
        print(f'CTPS tem o valor {cadastro["ctps"]}.')
    else:
        cadastro['contratação'] = int(input('Ano de contratação: '))
        cadastro['salario'] = float(input('Salário: R$'))
        cadastro['aposentadoria'] = hoje - cadastro['contratação']
        print('-=' * 50)
        print(cadastro)
        print(f'Nome tem valor {cadastro["nome"]}.')
        print(f'Idade tem o valor {cadastro["idade"]} anos.')
        print(f'CTPS tem o valor {cadastro["ctps"]}.')
        print(f'Contratação tem o valor {cadastro["contratação"]}.')
        print(f'Salário tem o valor R${cadastro["salario"]:.2f}.')
        print(f'Aposentadoria tem o valor {cadastro["aposentadoria"]} anos.')
    cont +=1


#Guanabara

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
