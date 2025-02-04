lista=[]
listasup=[]
cont=0
while True:
    nome=str(input("Digite o nome do aluno: "))
    nota1=float(input("Nota 1:"))
    nota2=float(input("Nota 2:"))
    media=(nota1+nota2)/2
    cont+=1
    listasup.append([nome,[nota1,nota2],media])
    lista.append(listasup[:])
    listasup.clear()
    resp=str(input("Deseja continuar?"))
    if resp in 'Nn':
        break
print('=-'*15)
print(f'{"BOLETIM DA SALA":=^15}')
print('=-'*15)
for i in range(len(lista)):
    print(f'{i:^5}{lista[i][0]:.<20}{lista[i][3]:^5}')
while True:
    aluno=int(input('Digite o número do aluno que queira saber as notas: '))
    print(f'Aluno:{lista[aluno][0]:.20} Nota 1: {lista[aluno][1]}, Nota 2: {lista[aluno][2]}, Média: {lista[aluno][3]} ')
    if aluno == 999:
        break
print('Fim do Programa')
