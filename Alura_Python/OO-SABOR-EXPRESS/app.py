from modelos.cardapio.bebida import Bebida
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa



restaurante_praca = Restaurante ('praça','Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.00,'Grande')
prato_paozinho = Prato('Paozinho',2.00,'Melhor pão da cidade.')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()