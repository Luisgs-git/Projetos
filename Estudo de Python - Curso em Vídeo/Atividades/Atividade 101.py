from datetime import date
def alistamento(ano):
    idade=date.today().year - ano
    votar= 'NÃO VOTA'
    if idade>18 and idade<65:
        votar ='VOTO OBRIGATÓRIO'
    elif idade>65 or 16<=idade<18:
        votar ='VOTO OPCIONAL'
    else:
        votar = 'NÃO VOTA'
    print(f'Com {idade} anos: {votar}')


ano=int(input("Em que ano você nasceu: "))
alistamento(ano)