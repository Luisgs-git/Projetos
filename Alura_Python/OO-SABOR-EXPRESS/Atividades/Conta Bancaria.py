class ContaBancaria:
    def __init__(self,titular='',saldo=0.00):
        self.titular = titular
        self.saldo = saldo
        self._ativo= False 
 
    def __str__(self):
        return f'Conta de {self.titular} | Saldo R$ {self.saldo}'
    
    
    @classmethod
    def ativar_conta(cls):
        ContaBancaria.ativo = True

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property   
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
            conta = ContaBancariaPythonica(titular, saldo_inicial)
            return conta


   