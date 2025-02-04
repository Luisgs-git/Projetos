import random
from time import sleep
x=int(input("Escolha um número de 0 a 10: "))
y=random.randint(0,10)
sleep(2)
print("Deixa eu pensar...")
sleep(2)
contador=1
acertou = False
while not acertou:
    if x == y:
        acertou = True
    else:
        print("Você não acertou, a resposta certa seria {} e você escolheu {}. Tente de novo até acertar!!".format(y,x))
        x = int(input("Escolha novamente um número de 0 a 10: "))
        y = random.randint(0, 10)
        sleep(2)
        print("Deixa eu pensar...")
        contador+=1

print("Parabéns, você acertou o número {} depois de {} tentativas kkkkkkkkk".format(x,contador))
