n1 = int(input('Informe um valor de  PA:'))
r=int(input('Razão da PA:'))
c=1
print(n1,'-> ',end='')
while c<10:
    n1+=r
    print("{} -> ".format(n1),end='')
    c+=1
print('Pausa')
d=1
while d!=0:
    termos = int(input("Quantos termos quer "))
    if termos!=0:
        d=0
        while d<termos:
            n1 += r
            print("{} -> ".format(n1), end='')
            d+=1
        print ("Pausa")
    else:
        d=0