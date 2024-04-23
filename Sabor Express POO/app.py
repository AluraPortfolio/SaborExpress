from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_1 = Restaurante('All Capone', 'Italiano')
bebida_1 = Bebida('Suco de Laranja', 5.00, 'Médio')
bebida_1.aplicarDesconto()
prato_1 = Prato('Carbonara', 25.00, 'Carbonara com Guanchale e Pecorino Romano')
prato_1.aplicarDesconto()
restaurante_1.AdicionarItemNoCardapio(bebida_1)
restaurante_1.AdicionarItemNoCardapio(prato_1)


# restaurante_1.receberAvaliacao('Vini', 5)
# restaurante_1.receberAvaliacao('Gabi', 4)
# restaurante_1.receberAvaliacao('Lucas', 2)
# restaurante_2 = Restaurante('Bonjour', 'Francês') 
# restaurante_3 = Restaurante('Las Tapitas', 'Espanhol') 
# restaurante_1.alterarStatus() 

def main():
    # Restaurante.listar_restaurantes()
    restaurante_1.ExibirCardapio

if __name__=='__main__':
    main()