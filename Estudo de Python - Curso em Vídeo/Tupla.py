a= 2,5,6
b=4,5,8
c=a+b
print(c)
print(c.index(5))#Identificar a posição
pessoa='Gustavo',39,'M',99.88
print(pessoa) #Tuplas são imutáveis
del(pessoa)#Apaga toda a tupla, não é possível deletar um item da Tupla[0]

lanche=('Hamburguer','Suco','Pizza', 'Pudim','Batata Frita')
#Metodos de explorar a Tupla v
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição{pos}')

print('Comi pra caramba!')
print(sorted(lanche))
