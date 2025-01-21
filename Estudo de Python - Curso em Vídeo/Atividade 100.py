from random import randint

def sortear(qtd):
    a=[]
    for i in range(0,qtd):
        a.append(randint(1,10))
    print(f"Os números sorteados foram {a}")
    return a
def somapar(lista):
    somap=0
    listapar=[]
    for i in lista:
        if i%2==0:
            somap+=i
            listapar.append(i)
    print(f"Os números pares são {listapar} e a soma deles é de {somap}")
somapar(sortear(5))

