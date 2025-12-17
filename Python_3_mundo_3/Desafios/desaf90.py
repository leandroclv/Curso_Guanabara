aluno = {}
aluno_nome = str(input('Digite um nome: '))
aluno_media = float(input(f'Qual a média do {aluno_nome.capitalize()}: '))
if aluno_media >= 7:
    situ = 'aprovado'
else:
    situ = 'reprovado'
aluno['nome'] = aluno_nome
aluno['media'] = aluno_media
print(f'Nome é igual a {aluno["nome"]}.')
print(f'Média é igual a {aluno["media"]}.')
print(f'Situação é igual a \033[0;31m{situ.upper()}\033[m!')
print(aluno)

#Guanabara

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['situação'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
