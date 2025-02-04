def leiaint(msg):
    ok = False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            n=int(n)
            ok=True
        else:
            print('\033[0;31mNÚMERO INVALIDO!\033[m')
        if ok:
            break
    return n


n= leiaint("Digite um número:")
print(f"O número escolhido foi {n}")