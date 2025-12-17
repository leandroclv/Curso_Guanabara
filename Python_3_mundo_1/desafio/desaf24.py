cid = str(input('Em que cidade você nasceu? ')).lower()
cids = cid.split()
print('santo' in cids[0])
#cid = str(input('Em que cidade você nasceu? ')).strip() //o strip retira os espaços antes e depois da frase
#print(cid[:5].upper == 'SANTO') //ele contou as letras da palavra santo e perguntou no programa se é igual a santo e passou tudo para maiúsculo para retirar qualquer erro que o usuário inserir