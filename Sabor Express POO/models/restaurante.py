from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, Nome, Categoria):
        self._Nome = Nome.title()
        self._Categoria = Categoria.title()
        self._Status = False
        self._Avaliacao = []
        self._Cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._Nome} | {self._Categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._Nome.ljust(25)} | {restaurante._Categoria.ljust(25)} | {str(restaurante.mediaAvaliacoes).ljust(25)} | {restaurante.Status}')

    @property
    def Status(self):
        return '✅' if self._Status else '❌'
    
    def alterarStatus(self):
        self._Status = not self._Status

    def receberAvaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._Avaliacao.append(avaliacao)

    @property
    def mediaAvaliacoes(self):
        if not self._Avaliacao:
            return '-'
        somaDasNotas = sum(avaliacao._nota for avaliacao in self._Avaliacao)
        quantidadeDeNotas = len(self._Avaliacao)
        mediaDasNotas = round(somaDasNotas / quantidadeDeNotas, 1)
        return mediaDasNotas

    def AdicionarItemNoCardapio(self, item):
        if isinstance (item, ItemCardapio):
            self._Cardapio.append(item)
    
    @property
    def ExibirCardapio(self):
        print(f'Cardapio do restaurante {self._Nome}\n')
        for i, item in enumerate(self._Cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagemPrato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}.'
                print(mensagemPrato)
            else:
                mensagemBebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}.'
                print(mensagemBebida)

