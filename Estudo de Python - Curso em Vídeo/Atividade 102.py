def fatorial(a, b=False):
    '''
    -> Calculadora de fatorial
    :param a: O numero a ser calculado
    :param b: Para mostrar a conta
    :return: O valor retorna com Fatorial (f)
    '''
    f=1
    for i in range (a,0,-1):
        f*=i
            if i==1:
                if b:
                    print(f"{i} ",end="")
            else:
                print(f"{i} X ",end=" ")
        print(f"= {f}")
    return f

fatorial(10)
