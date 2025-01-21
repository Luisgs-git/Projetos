#Realização de uma matriz
lista=[[],[],[]]
for i in range (3):
    for r in range(3):
        a = input(f'Digite um número [{i},{r}]:')
 

        lista[i].insert(r,a)
for l in range (3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]',end='')
    print()