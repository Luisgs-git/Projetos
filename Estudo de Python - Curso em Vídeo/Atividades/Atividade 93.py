soma=0
dados={}
jogo=[]
dados["Nome"]= str(input("Digite nome do Jogador: "))
partidas=int(input(f"Quantas partidas {dados["Nome"]} jogou?"))
for i in range (partidas):
    gol=(int(input(f"Quantos gols na partida {i}:")))
    jogo.append(gol)
    soma+=gol
dados['Gol']=jogo[:]
dados['total']=soma
print("=-"*25)
print(dados)
print("=-"*25)
for i,v in dados.items():
    print(f"O campo {i} tem o valor {v}")
print("=-"*25)
print(f'O jogador {dados["Nome"]} jogou {partidas}')
for t,v in enumerate(dados['Gol']):
    print(f"=> Na partida {t}, o número de gols foi {v} ")
print(f'Foi um total de {dados["total"]} gols.')