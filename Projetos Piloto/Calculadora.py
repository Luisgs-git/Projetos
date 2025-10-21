
def resultado(n1,n2,operacao):
       if operacao == '+':
              operacao = n1+n2
       elif operacao == '-':
              operacao = n1-n2
       elif operacao == '/':
              operacao = n1/n2
       elif operacao == '*':
              operacao = n1*n2
       elif operacao == '^':
              return f'{pow(n1,n2)}'
       elif operacao == 'r':
              return f'{n1**(1/n2)}'
       elif operacao == '=':
              return ''
       else:
              return None
       
def menu():
       operadores = {
    '+': 'Somar',
    '-': 'Subtrair',
    '/': 'Divisão',
    '*': 'Multiplicar',
    '^': 'Potência',
    'r': 'Raiz'}
       print("MENU DA CALCULADORA")
       print("Opções para a calculadora:")
       for operador,obg in operadores.items():
              print(f'{operador.ljust(2)} -> {obg.center(1)}')

menu()
result = 0
n1 = float(input('Digite um número:'))
operacao=str(input("Digite a operação:"))
n2 = float(input("Digite o segundo número:"))
while operacao:

resultado_1 = resultado(n1,n2,operacao)
if operacao != "=":
       operacao = str(input('Digite a operação (= para sair):'))
       n2_loop = float(input('Digite o próximo número:'))
       resultado_loop =  resultado()
