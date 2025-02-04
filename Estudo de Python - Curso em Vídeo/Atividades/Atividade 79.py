listanum=[]
while True:
    a=int(input('Digite um valor:'))
    if a in listanum:
        print('Valor duplicado! Não é possível adicionar.')
    else:
        listanum.append(a)
    continuar=str(input('Deseja continuar? [S/N]'))[0].strip()
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]'))[0].strip()
    if continuar in 'Nn':
        break
listanum.sort()
print(listanum)