d=int(input("Qual a distância da viagem? Km"))
if d <= 200:
    print("A passagem será de R${:.2f}".format(d*0.5))
else:
    print("A passagem para essa longa viagem será de R${:.2f}".format(d*0.45))