velhos=[]
mulheres=[]
lista=[]
dados={}
cont=somaidade=0
while True:
    dados.clear()
    cont+=1
    dados['nome']=str(input("Nome:"))
    sexo = str(input("Sexo: ")).strip().upper()[0]
    while sexo not in "FfMm":
        sexo=str(input("Digite um sexo válido [F/M]: ")).strip().upper()[0]
    dados['sexo']=sexo
    dados['idade']=int(input("Idade: "))
    somaidade+=dados['idade']
    lista.append(dados.copy())
    continuar=str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar=str(input("ERRO! Digite apenas S ou N! "))
    if continuar in 'Nn':
        break
media = somaidade / cont
print('-=-'*15)
print(f'Foram cadastradas {cont} pessoas!')
for i in range(len(lista)):
    print(f"Nome: {lista[i]['nome']}{'.':.^10}Idade de {lista[i]['idade']} Sexo: {lista[i]['sexo']}.")
    if lista[i]['idade']>=media:
        velhos.append(lista[i])
    if lista[i]['sexo']=='F':
        mulheres.append(lista[i])
print('-=-'*15)
print(f'A idade média é de {media} e as pessoas acima desta idade são:')
for a in range(len(velhos)):
    print(f"Nome: {velhos[a]['nome']} {'.':.^10} Idade:{velhos[a]['idade']} Sexo: {velhos[a]['sexo']} ")
print('-=-'*15)
print(f'As mulheres da lista são:')
for r in range(len(mulheres)):
    print(f"Nome: {mulheres[r]['nome']} {'.':.^10} Idade: {mulheres[r]['idade']}")


