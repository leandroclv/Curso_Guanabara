import random #posso colocar from random import choice para importar somente o comando choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #foi realizado uma lista com os nomes inseridos pelo cliente facilitando fazer a escolha
escolhido = random.choice(lista) #aqui eu posso tirar o random e deixar só o choice(lista)
print(f'O aluno escolhido foi {escolhido}')
