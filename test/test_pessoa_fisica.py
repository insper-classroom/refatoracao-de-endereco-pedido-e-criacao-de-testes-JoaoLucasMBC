import pytest
from classes.PessoaFisica import PessoaFisica


@pytest.mark.pessoa_fisica
def test_pessoa_criada_normal():
    pessoa = PessoaFisica(cpf='52579701800', email='joao@gmail.com', nome='João')

    assert pessoa.cpf == '52579701800'
    assert pessoa.email == 'joao@gmail.com'
    assert pessoa.nome == 'João'


@pytest.mark.pessoa_fisica
def test_pessoa_sem_cpf():
    with pytest.raises(TypeError) as exc:
        PessoaFisica(nome='João', email='joao@gmail.com')
    
    assert "missing 1 required positional argument: 'cpf'" in str(exc.value)


@pytest.mark.pessoa_fisica
def test_pessoa_sem_email():
    with pytest.raises(TypeError) as exc:
        PessoaFisica(nome='João', cpf='52579701800')
    
    assert "missing 1 required positional argument: 'email'" in str(exc.value)


@pytest.mark.pessoa_fisica
def test_pessoa_sem_nome():
    pessoa = PessoaFisica(cpf='52579701800', email='joao@gmail.com')

    assert pessoa.nome == 'Visitante'


@pytest.mark.pessoa_fisica
def test_busca_nome_pessoa():
    pessoa = PessoaFisica(cpf='52579701800', email='joao@gmail.com', nome='João')
    result = PessoaFisica.busca_nome('João')[0]

    assert result.nome == 'João'
    assert result.cpf == '52579701800'
    assert result.email == 'joao@gmail.com'


@pytest.mark.pessoa_fisica
def test_busca_nome_pessoa_nao_existe():
    PessoaFisica(cpf='52579701800', email='joao@gmail.com')
    assert PessoaFisica.busca_nome('Joao') == []