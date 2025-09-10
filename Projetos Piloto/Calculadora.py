

def continuacao (n1,n2,operacao):
       



def resultado(n1,n2,operacao):
       if operacao == '+':
              return f'{n1+n2}'
       elif operacao == '-':
              return f'{n1-n2}'
       elif operacao == '/':
              return f'{n1/n2}'
       elif operacao == '*':
              return f'{n1*n2}'
       elif operacao == '^':
              return f'{pow(n1,n2)}'
       elif operacao == 'raiz':
              return f'{n1**(1/n2)}'
       else:
              return SyntaxError
       

while True:
        n1 = float(input('Digite um número:'))
        operacao=str(input("Digite a operação:"))
        if operacao == "=":
                print()
                break
        else:
            n2 = float(input("Digite o segundo número:"))
            
        

        





