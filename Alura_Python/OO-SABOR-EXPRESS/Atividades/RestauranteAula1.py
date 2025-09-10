import os
restaurantes=[{'nome':'Praça', 'categoria':'Japonesa','ativo':False},{'nome':'Supreme', 'categoria':'Pizza','ativo':True},{'nome':'Cantina', 'categoria':'Italiano','ativo':False}]
# variável onde guardará o dicionarios dos restaurantes.

def finaliza_app():
    '''Limpa e finaliza o código.'''
    os.system('cls')
    print("Finalizando app...")
    
def exibir_subtitulo(texto):
    #Limpa o terminal e print
    os.system('cls')
    linha = '=' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    #função para criar "Botão de volar"
    input("\nDigite uma tecla para voltar ao menu principal. ")
    main()


def nome_programa():
    #Nome do Programa Restaurante
    print("""
        
🅡 🅔 🅢 🅣 🅐 🅤 🅡 🅐 🅝 🅣 🅔
""")


def exibir_opcoes():
    #Exibe as funções em lista, podendo adicionar mais.
    lista= ['Cadastrar restaurante.','Listar restaurante.','Alternar estado do restaurante.','Fechar aplicativo.']
    cont=1
    for i in lista:
        print(f"{cont} - {i}")
        cont+=1


def opcao_invalida():
    #Informa ao usuario no terminal.
    exibir_subtitulo("Opção Inválida\n")
    voltar_ao_menu()


def escolher_opcao():
    #Escolher opção
        try: 
            opcao_escolhida = int(input('Escolha uma opção:'))
            if opcao_escolhida == 1:
                cadastrar()
            elif opcao_escolhida == 2:
                listar()
            elif opcao_escolhida == 3:
                alterando_estado_restaurante()
            elif opcao_escolhida == 4:
                finaliza_app()
            else:
                opcao_invalida()
        except:
            opcao_invalida()



def cadastrar():
    #Cadastro de Restaurantes (Dicionários)
    cadastro = dict()
    cadastro.clear()
    exibir_subtitulo("Cadastro de novos restaurantes")
    cadastro['nome']=input("Digite o nome do restaurante que deseja cadastrar: ")
    cadastro['categoria']=input("Qual a categoria do restaurante: ")
    cadastro['ativo'] = False
    restaurantes.append(cadastro.copy())
    print(f'O restaurante {cadastro['nome']} foi cadastrado!')
    voltar_ao_menu()


def listar():
    #Listar restaurantes
    exibir_subtitulo("RESTAURANTES CADASTRADOS\n")
    cont=1
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'} ')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"{nome.ljust(20)} | {categoria.ljust(20)} | {ativo}")
        cont+=1
    voltar_ao_menu()

def alterando_estado_restaurante():
    #Alterna a variavel ativo do restaurante (True/False)
    exibir_subtitulo("Ativar Restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")
    
    voltar_ao_menu()


def main():
    #Função que retorna o menu.
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    #Mantem esse código como principal.
    main()
