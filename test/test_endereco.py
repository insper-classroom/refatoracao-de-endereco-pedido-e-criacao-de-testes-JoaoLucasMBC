import pytest

from classes.Endereco import Endereco


@pytest.mark.endereco
def test_endereco_sem_cep():
    with pytest.raises(TypeError) as exc:
        assert exc == Endereco(numero=567)

@pytest.mark.endereco
def test_endereco_sem_num():
    with pytest.raises(TypeError) as exc:
        assert exc == Endereco(cep=f'05641100')

@pytest.mark.endereco
def test_consulta_cep_nao_e_string_ou_int():
    with pytest.raises(TypeError) as exc:
        Endereco.consultar_cep(cep=False)
        assert 'missing' in str(exc.value)

@pytest.mark.endereco
def test_cep_formato_numerico_errado():
    with pytest.raises(TypeError) as exc:
        Endereco.consultar_cep(cep=52527)
        assert 'length' in str(exc.value)

@pytest.mark.endereco
def test_cep_nao_existente():
    assert '' == Endereco.consultar_cep(cep=99999999)

@pytest.mark.endereco
def test_caiu_a_net():
    pass