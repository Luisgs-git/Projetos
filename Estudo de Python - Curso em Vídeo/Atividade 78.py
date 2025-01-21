lista=[]
mai=men=0
for i in range(0,5):
    lista.append(int(input(f"Informe um número na que estarána posição {i} : ")))
    if i==0:
        mai=men=lista[i]
    else:
        if lista[i]>mai:
            mai=lista[i]
        if lista[i]<men:
            men=lista[i]
print('=-='*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(lista):
    if v==mai:
        print(f'{i}...',end="")
print(f'\nO menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(lista):
    if v==men:
        print(f'{i}...',end="")
