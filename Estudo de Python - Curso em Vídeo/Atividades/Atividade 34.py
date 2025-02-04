import random
print('{:=^80}'.format('JOGO DE PEDRA, PAPEL OU TESOURA'))
print("Vamos jogar pedra, papel e tesoura!!")
print("""Escolha:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
""")
player=int(input("Escolha uma das opções: "))
while player>3:
  player=int(input("Escolha uma das opções: "))
pc=random.randrange(0,2)
grupo = ['Pedra','Papel','Tesoura']
if (player==0 and pc==2) or (player==1 and pc==0) or (player==2 and pc==1):
  print("Parabéns, você ganhou com {} e o BOT escolheu {}".format(grupo[player],grupo[pc]))
elif (pc==0 and player==2) or (pc==1 and player==0) or (player==2 and pc==1):
  print("Você perdeu! Com {} e o BOT escolheu {}".format(grupo[player],grupo[pc]))
elif pc==player:
  print("""Deu empate!
  Ambos escolheram {}""".format(grupo[player]))
