c=('\033[m',
  '\033[0;30;41m')
def ajuda(com):
    help(com)
def t ítulo(msg,cor=0):
    tam=len(msg)
    print(c[cor],end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0],end='')

#progrma principal
comando=''
while True:
    título ("SYSTEMA DE AJUDA PyHelp")
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper()=='FIM':
        break
    else: ajuda(comando)
título("Até logo!")