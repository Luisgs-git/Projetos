dados=dict()
dados={'Nome':'Pedro','idade':25}
print(dados['Nome'])
dados['Sexo']='M'
print(dados)
dados['idade']=30
print(dados)
del dados['idade']
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())