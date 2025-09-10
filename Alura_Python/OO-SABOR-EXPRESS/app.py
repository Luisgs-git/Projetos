from modelos.restaurante import Restaurante

restaurante_praca = Restaurante ('praça','Gourmet')
restaurante_praca.receber_avaliacao('Luis',10)
restaurante_praca.receber_avaliacao('Judas',7)

restaurante_mexicano=Restaurante('Mexican Food','Mexicano')
restaurante_italiano=Restaurante('Pizzarino','Italiano')

restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()