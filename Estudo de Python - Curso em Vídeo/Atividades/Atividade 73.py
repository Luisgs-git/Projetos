time='Flamengo','Palmeiras','Botafogo','Bahia','Atlhetico A','São Paulo','Cruzeiro','Fortaleza','RB Bragantino','Internacional','Atlético MG','Juventude','Criciuma','Cuiaba','Vitoria','Vasco','Atletico GO','Gremio','Corinthians','Fluminense'
print('=-='*15)
print(f'Lista de times do Brasileirão: {time}')
for i in time:
    print(i)
print('=-='*15)
print(f'Os 5 primeiros são {time[0:5]}')
print('=-='*15)
print(f'Os 4 últimos são {time[:-4]}')
print('=-='*15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('=-='*15)
print(f'São Paulo está na posição {time.index('São Paulo')+1}')