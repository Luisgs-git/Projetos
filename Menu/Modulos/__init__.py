def linha(tam=42):
    print("-"*tam)

def cabeçalho(titulo):
    linha()
    print(titulo.center(42))
    linha()

def menu(*num):
    cabeçalho('MENU DO SISTEMA')
    contador=1
    for c in num:
        print(f"{contador} - {c}")
        contador+=1
    linha()
    opcao =leiaint('Sua opção:')
    return opcao

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

