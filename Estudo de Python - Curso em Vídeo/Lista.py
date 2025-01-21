lista= ['lanche','rodizio','carne']
lista.append('cokie')
lista.insert(0,'saco')
del lista[2]
lista.pop()
lista.remove('lanche')
if 'papagaio' != lista:
    lista.insert(3,'Papagaio')
valores= list(range(4,11,2))
embaralhados=[0,5,7,1,2,4]
embaralhados.sort()
embaralhados.sort(reverse=True)
print(embaralhados)
print(valores)
print(lista)
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
coisas=[]
for cont in range(0,5):
    coisas.append(int(input('Selecione um valor:')))
print(coisas)