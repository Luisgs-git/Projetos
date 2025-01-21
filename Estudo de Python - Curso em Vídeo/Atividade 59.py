saida = 0
cont= True
    p1= int(input('Primeiro valor: '))
    s2= int(input('Segundo valor: '))
while cont ==True:
    menu=int(input("""Escolha uma das opções para seguir com os dois valores:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Inserir resposta: """))
    if menu == 1:
            t3= p1+s2
            print('Sua soma é de {}.'.format(t3))
    elif menu == 2:
            t3=p1*s2
            print('A multiplicação dos valores é de {}'.format(t3))
    elif menu == 3:
        if p1 > s2:
                print("O maior entre eles é {}".format(p1))
        elif s2>p1:
                print("O maior entre eles é {}".format(s2))
        else:
                print("Os valores são iguais")
    elif menu == 4:
        print('Selecione novos valores.')
    elif menu == 5:
        print('Saíndo do programa!')
        cont= False
    else:
        print("Selecione um valor válido")