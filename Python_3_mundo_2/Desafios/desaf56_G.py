somaidade = 0
maioridadehomem = 0
mediaidade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'------------{p}ª pessoa-----------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho.capitalize()}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')








'''import string
#nome = []
idade = []
#sexo = []
count = 1
for p in range(0, 4):
    #name = str(input(f'Digite o nome da {count} pessoa: '))
    age = int(input(f'Digite a idade da {count} pessoa: '))
    #sex = str(input(f'Digite o sexo da {count} pessoa: '))
    #nome.append(name)
    idade.append(age)
    #sexo.append(sex)
    count += 1
#print(nome)
#print(idade)
#print(sexo)
print(f'A média de idade do grupo é {sum(idade)/4}.')
#print(f'O nome do home mais velho é {')'''