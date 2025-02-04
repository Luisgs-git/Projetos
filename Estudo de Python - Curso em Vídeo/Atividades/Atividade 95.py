time=dict()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {jogador["nome"]} jogou?"))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c}?")))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time=jogador.copy()


    while True:
        resp = str(input("Deseja continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(time)
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end="")
    for d in time.values():
            print(f"{str(d):<15}", end="")
    print()