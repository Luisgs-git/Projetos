lista=[]
par=[]
impar=[]
while True:
    n=int(input("Digite um número: "))
    lista.append(n)
    pergunta=str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if pergunta in 'Nn':
        break
print('=-'*20)
for i in lista:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
lista.sort()
par.sort()
impar.sort()
print(f'Os números selecionados foram {lista}')
print(f'Impar {impar}')
print(f'Par {par}')