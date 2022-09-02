import pytest
from classes.Produto import Produto


@pytest.mark.produto
def test_criar_produto_normal():
    produto = Produto(id=1, nome='teste')

    assert 1 == produto.id
    assert 'teste' == produto.nome


@pytest.mark.produto
def test_criar_produto_sem_id():
    with pytest.raises(TypeError) as exc:
        Produto(nome='teste')
    
    assert "missing 1 required positional argument: 'id'" in str(exc.value)


@pytest.mark.produto
def test_criar_produto_sem_nome():
    prod = Produto(id=1)

    assert prod.nome == ''


@pytest.mark.produto
def test_produto_busca_nome():
    prod = Produto(nome='teste', id=1)
    result = Produto.busca_nome('teste')[0]

    assert result.nome == prod.nome
    assert result.id == prod.id


@pytest.mark.produto
def test_busca_nome_nao_encontra():
    Produto(nome='teste', id=1)

    assert Produto.busca_nome('joão lucas') == []