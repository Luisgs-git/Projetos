def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mErro: Por favor digite um número válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            f=float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: Por favor digite um número válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return f


n= leiaint("Digite um número:")
f=leiafloat("Digite um numero Real:")
print(f"O número escolhido inteiro foi {n} e o real foi {f}")
