def mensagem(msg):
    print('-'*20)
    print(f'{msg:^20}')
    print('-'*20)


mensagem('SISTEMA')

def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f"Somando os valores {valores} temos {s}")

soma(15,10)

def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1


valore=[3,4,85,5]
dobra(valore)
print(valore)

soma(5,2)