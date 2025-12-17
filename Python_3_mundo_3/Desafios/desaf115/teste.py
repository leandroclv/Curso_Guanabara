import dados
import time

arq = 'cursoemvideo.txt'

if not dados.arquivoExiste(arq):
    dados.criarArquivo(arq)


while True:
    resposta = dados.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        dados.lerArquivo(arq)
    elif resposta == 2:
        dados.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).capitalize()
        idade = dados.leiaInt('Idade: ')
        dados.cadastrar(arq, nome, idade)
    elif resposta == 3:
        dados.cabecalho('Saindo do sistema ... Até logo!')
        break
    else:
        dados.cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
    time.sleep(1)