from arquivo import *
from Modulos import *
arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema')
    if resposta == 1:
        # Opção de visualisar e listar o conteúdo do arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome=str(input("Nome:"))
        idade=leiaint("Idade:")
        escreverArquivo(arq,nome,idade)
    elif resposta == 3:
        # Opção de fechar o arquivo.
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!!")



