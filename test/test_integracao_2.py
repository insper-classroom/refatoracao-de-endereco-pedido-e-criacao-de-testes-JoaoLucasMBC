#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento
from classes.Produto import Produto
from classes.Pedido import Pedido

import copy
import pytest

# Caso de uso em que criamos uma pessoa do zero, em seguida um produto, e  depois fechamos um pedido
# Cria uma pessoa 
pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf='524.222.452-6')

# Cria  um endereço
end1 = Endereco('08320330', 430)

# Cria um outro endereço
end2 = Endereco('04546042', 300)


@pytest.mark.integracao
def test_adiciona_endereco_em_pessoa():
    # Adiciona endereço à pessoa
    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)
    
    result = pessoa1.listar_enderecos()

    assert 'casa' in result
    assert 'trabalho' in result
    assert str(end1) == result['casa']
    assert str(end2) == result['trabalho']


@pytest.mark.integracao
def test_cria_e_finaliza_pedido():
    # Criando um produto
    sabonete = Produto("0010342967", "Sabonete")

    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 5)

    pedido = Pedido(pessoa1, carrinho)
    
    pedido.endereco_entrega = copy.deepcopy(end1)
    pedido.endereco_faturamento = copy.deepcopy(end2)
    assert str(pedido.endereco_entrega) == str(end1)
    assert str(pedido.endereco_faturamento) == str(end2)

    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado():
        pedido.status = Pedido.PAGO 

    assert pedido.status == 2
    assert str(pedido) == f'Pedido de {pessoa1.nome} - {pessoa1.cpf}, será enviado para {str(end1)} e comprou {carrinho.get_items()}'