lista=[]
gordo=[]
magro=[]
dados=[]
menor=maior=contador=0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso:')))
    lista.append(dados[:])
    if contador == 1:
        maior=menor=dados[1]
    elif dados[1]>maior:
        maior=dados[1]
    elif dados[1]<menor:
        menor=dados[1]
    contador+=1
    dados.clear()
    continuar=str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar=str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if continuar in 'N':
        break
for i in range(len(lista)):
    if lista[i][1]==maior:
        gordo.append(lista[i][0])
    elif lista[i][1]==menor:
        magro.append(lista[i][0])
print(f'A quantidade de pessoas cadastradas foi de {contador}.')
print(f'O maior peso foi de {maior}Kg. Peso de {gordo}')
print(f'O menor peso foi de {menor}Kg. Peso de {magro}')
