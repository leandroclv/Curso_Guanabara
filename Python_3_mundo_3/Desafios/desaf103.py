
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


nome = str(input('Nome do Jogador: '))
g = str(input('Números de gols: ')) #está em string pq aceita não colcoar nehuma resposta
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome, g)