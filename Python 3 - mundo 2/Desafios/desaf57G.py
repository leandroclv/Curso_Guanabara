sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #retira os espaços, coloca em maiúsculo e pega somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
