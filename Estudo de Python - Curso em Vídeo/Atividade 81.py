lista= []
while True:
    n=int(input('Digite um número: '))
    lista.append(n)
    pergunta=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if pergunta =='N':
        break
lista.sort()
print(f'Você digitou {len(lista)} núemros!')
print(f'Os números escolhidos foram {lista[::-1]}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 está fora da lista!')