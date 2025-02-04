l1=float(input("Lado1:"))
l2=float(input("Lado2:"))
l3=float(input("Lado3:"))
if (l1+l2)<l3 or (l2+l3)<l1 or (l1+l3)<l2:
    print("Não da pra formar um triangulo")
else:
    print("Da pra formar um triangulo!")

