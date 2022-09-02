import pytest
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho


@pytest.mark.pedido
def test_cria_pedido_completo():
    pessoa = PessoaFisica(nome='João', cpf='52579701800', email='joao@gmail.com')
    car = Carrinho()
    pedido = Pedido(pessoa, car)

    pedido.endereco_entrega = 'Rua Quatá'
    pedido.endereco_faturamento = 'Rua Quatá'

    assert str(pedido) == f'Pedido de {pessoa.nome} - {pessoa.cpf}, será enviado para Rua Quatá e comprou {car.get_items()}'


@pytest.mark.pedido
def test_cria_pedido_sem_pessoa():
    with pytest.raises(TypeError) as exc:
        Pedido(carrinho=Carrinho())
    
    assert "missing 1 required positional argument: 'cliente'" in str(exc.value)


@pytest.mark.pedido
def test_cria_pedido_sem_carrinho():
    pessoa = PessoaFisica(nome='João', cpf='52579701800', email='joao@gmail.com')
    with pytest.raises(TypeError) as exc:
        Pedido(cliente=pessoa)
    
    assert "missing 1 required positional argument: 'carrinho'" in str(exc.value)


# Outros testes, por serem testes de integração, utilizando diferentes funcionalidades,
# serão testados no arquivo de teste de integração. Obrigado!