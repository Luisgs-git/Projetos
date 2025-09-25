from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        #com super, é possível acessar os atributos de uma classe, importando ela.
        super().__init__(nome,preco)# HERANÇA
        self._descricao = descricao

    def __str__(self):
        return self._nome