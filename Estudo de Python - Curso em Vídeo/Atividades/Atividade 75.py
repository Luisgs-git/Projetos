list= int(input("Digite um número: ")),int(input("Digite outro número: ")), int(input("Digite mais um número: ")),int(input("Digite o útlimo número: "))
print(f"Você digitou os valores {list}")
print(f'O valor 9 apareceu {list.count(9)} vezes.')
if 3 in list:
    print(f'O valor 3 apareceu na {list.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu nos números digitados.')
for n in list:
    if n % 2==0:
        print(n, end=' ')