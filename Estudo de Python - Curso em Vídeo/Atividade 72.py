numero=('zero','um','dois','três','quatro','cinco','seis','sete',
        'oito','nove','dez','onze','doze','treze','catorze','quinze',
        'dezesseis','dezesete','dezoito','dezenove','vinte')
n=int(input('Digite um número entre 0 a 20:'))
while n>20 or n<0:
    n=int(input('Tente novamente.Digite um número entre 0 a 20:'))
print(f'Você digitou o número {numero[n]}.')