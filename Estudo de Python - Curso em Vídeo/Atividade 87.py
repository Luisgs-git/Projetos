lista=[[],[],[]]
soma=0
coluna=0
maior=0
for i in range(0,3):
    for r in range (0,3):
        a = int(input(f"Digite um valor na posição [{i},{r}]:"))
        if a%2==0:
            soma+=a
        if r==2:
            coluna+=a
        if i==1:
            if r==0:
                maior=a
            if maior<a:
                maior=a
        lista[i].insert(r,a)
for i in range (0,3):
    for r in range (0,3):
     print(f"[{lista[i][r]:^5}]",end=" ")
    print()
print(f"A soma dos números pares é {soma} ")
print(f"A soma da 3a coluna é {coluna}")
print(f"O maior número da 2a linha é {maior}")