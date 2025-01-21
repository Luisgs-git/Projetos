tupla='Lápis',1.75,'Borracha',2, 'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90
print('-'*30)
print(f'{'Lista de Produtos':^30}')
print('-'*30)
for i in range(0,len(tupla),2):
    print(f'{tupla[i]:.<30}R${tupla[i+1]:>7.2f}')
#for i in range(0,len(tupla))
# if i % 2 ==0:
    #print(f'{tupla[i]:.>30},end=' ')
#else:
    #print(f'R${tupla[i]:.7.2f')
