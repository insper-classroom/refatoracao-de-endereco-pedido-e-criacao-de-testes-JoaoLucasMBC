import pytest
from classes.Carrinho import Carrinho
from classes.Produto import Produto


@pytest.mark.carrinho
def test_criacao_de_carrinho():
    car = Carrinho()

    assert {} == car.get_items()


@pytest.mark.carrinho
def test_get_item_carrinho():
    car = Carrinho()
    car.adicionar_item(Produto(nome='teste', id=1), 12)

    assert 1 in car.get_items()
    assert 12 == car.get_items()[1]

# Outros testes de adicionar item, remover item, etc., por serem testes de integração, utilizando diferentes funcionalidades,
# serão testados no arquivo de teste de integração. Obrigado!