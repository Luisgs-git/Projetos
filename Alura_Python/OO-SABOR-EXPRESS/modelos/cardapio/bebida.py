from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self,nome,preco,tamanho):
        #com super, é possível acessar os atributos de uma classe, importando ela.
        super().__init__(nome,preco)# HERANÇA
        self._tamanho = tamanho
        
    def __str__(self):
        return self._nome