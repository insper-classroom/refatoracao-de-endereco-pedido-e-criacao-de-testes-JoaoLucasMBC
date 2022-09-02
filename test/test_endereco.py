import pytest
import requests

from classes.Endereco import Endereco


@pytest.mark.endereco
def test_criar_endereco_completo():
    end = Endereco(cep='05641100', numero=567)

    assert end.cep == '05641100'
    assert end.numero == 567


@pytest.mark.endereco
def test_endereco_sem_cep():
    with pytest.raises(TypeError) as exc:
        Endereco(numero=567)
    assert "missing 1 required positional argument: 'cep'" in str(exc.value)

@pytest.mark.endereco
def test_endereco_sem_num():
    with pytest.raises(TypeError) as exc:
        Endereco(cep='05641100')
    assert "missing 1 required positional argument: 'numero'" in str(exc.value)

@pytest.mark.endereco
@pytest.mark.calcula_cep
def test_consulta_cep_nao_e_string_ou_int():
    assert False == Endereco.consultar_cep(cep=False)

@pytest.mark.endereco
@pytest.mark.calcula_cep
def test_cep_formato_numerico_errado():
    assert False == Endereco.consultar_cep(cep=52527)

@pytest.mark.endereco
@pytest.mark.calcula_cep
def test_cep_nao_existente():
    assert False == Endereco.consultar_cep(cep=99999999)

@pytest.mark.sem_conexao
@pytest.mark.calcula_cep
def test_caiu_a_net():
    with pytest.raises(requests.exceptions.ConnectionError) as exc:
        Endereco.consultar_cep(cep='05641100')
    
    assert 'Max retries' in str(exc.value)