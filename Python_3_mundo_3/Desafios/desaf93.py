jogador = {}
gols = []
nome_jogador = str(input('Nome do jogador: '))
jogador['nome'] = nome_jogador
jogos = int(input(f'Quantas partidas {nome_jogador.capitalize()} jogou? '))
for i in range(0, int(jogos)):
    gol = int(input(f'Quantos gols na partida {i + 1}°?'))
    gols.append(gol)
jogador['gols'] = gols
total = sum(gols)
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-='*30)
print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campo gols tem o valor {jogador["gols"]}.')
print(f'O campo total tem o valor {jogador["total"]}.')
print('-='*30)
print(f'O Jogador {nome_jogador} jogou {jogos} partidas.')
for c in enumerate(gols):
    print(f'-> Na partida {c + 1}, fez {gols} gols.')
print(f'Foi um total de {total} gols')

#Guanabara

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')