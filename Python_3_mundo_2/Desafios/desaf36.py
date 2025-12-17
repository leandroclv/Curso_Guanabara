casa = float(input('Qual o valor da casa: R$'))
sala = float(input('Qual o valor do salário: R$'))
tempo = int(input('Quantos anos para o pagamento: '))
emprestimo = casa/ (tempo * 12)
salario = sala * 0.30
if emprestimo > salario:
    print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${emprestimo:.2f}!\nEmprestimo NEGADO!')
else:
    print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${emprestimo:.2f}!\nEmpréstimo pode ser CONCEDIDO!')
