#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados=dict()
dados['Aluno']=str(input("Digite o nome do aluno: "))
dados['Média']=float(input(f"Digite a média de {dados['Aluno']}: "))
if dados['Média']>=7:
    dados['Situação']='Aprovado'
elif 5<dados['Média']<7:
    dados['Situação']='Recuperação'
else:
    dados['Situação'] = 'Reprovado'
for i,a in dados.items():
    print(f' - {i} é igual a {a}.')