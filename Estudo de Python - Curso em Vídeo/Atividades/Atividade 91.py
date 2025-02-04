from random import randint
from operator import itemgetter
contador=1
jogadores={}
for i in range(1,5):
    jogadores[i]=randint(1,6)
for a in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{contador}º Jogador{a}, tirou {jogadores[a]}.')
    contador+=1
print('=-'*30)
