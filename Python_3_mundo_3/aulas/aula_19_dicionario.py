pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade':22 }
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
    
for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#del pessoas ['sexo']
pessoas['nome'] = 'Leandro' #troca Gustavo por Leandro
print(pessoas)
pessoas['peso'] = 98.5

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)