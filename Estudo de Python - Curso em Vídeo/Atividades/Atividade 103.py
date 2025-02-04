def ficha(nome="<desconhecido>",gols=0):
    print(f"O jogador {nome} fez {gols} gols!")

nome=input("Nome do jogador:")
gols=input("Número de gols: ")
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=="":
    ficha()
else:

    ficha()

ficha(nome,gols)

