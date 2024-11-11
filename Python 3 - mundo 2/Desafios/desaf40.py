try:
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
    if media < 5.0:
        print('O aluno está REPROVADO!')
    elif media >= 5.0 and media < 7:
        print('O aluno está de RECUPERAÇÃO!')
    elif media >= 7.0 and media <= 10.0:
        print('O aluno está APROVADO')
    else:
        print('A média está com o valor errado acima de 10, tente novamente')
except:
    print('Valor inválido, tente novamente!')
