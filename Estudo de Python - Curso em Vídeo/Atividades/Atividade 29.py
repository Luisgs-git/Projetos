from time import sleep
vel=float(input("Qual a velocidade do carro? Km"))
print("Processando...")
sleep(1)
if vel > 80:
    print("Você foi multado por excesso de velocidade.")
    print("Sua multa será de R${:.2f}".format((vel-80)*7))
else:
    print("Velocidade aceitável.")
print("Fim da estrada!")