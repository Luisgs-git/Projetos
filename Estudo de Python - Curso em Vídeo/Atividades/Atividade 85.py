lista=[[],[]]
for i in range (1,8):
    a=(int(input(f'Digite o {i} valor número: ')))
    if a%2==0:
        lista.insert(0,0,a)
    else:
        lista.insert(1,0,a)
print(lista)
