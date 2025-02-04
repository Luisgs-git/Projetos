a= int(input("Valor 1:"))
b= int(input("Valor 2:"))
c= int(input("Valor 3:"))
menor = a
if b<c and b<a:
    menor=b
if c<b and c<b:
    menor=c
maior=a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior=c
print("O menor valor é {}!".format(menor))
print("E o maior valor é {}!".format(maior))