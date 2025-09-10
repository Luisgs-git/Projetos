class Pessoa:
    def __init__(self,nome='', idade=0,profissao=''):
        self.nome= nome
        self.idade=idade
        self.profissao=profissao
    
    
    def __str__(self):
        return f'{self.nome} | {self.profissao} | {self.idade} anos'


    def aniversario(self):
        self.idade+=1
    

    @property
    def saudacao(self):
        return f'Olá {self.nome}, que trabalha em {self.profissao}!'

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()
