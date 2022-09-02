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

# Caso de uso em que se busca uma pessoa e um produto
# Cria uma pessoa 
pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf='524.222.452-6')

# Cria  um endereço
end1 = Endereco('08320330', 430)

# Cria um outro endereço
end2 = Endereco('04546042', 300)

# Adiciona endereço à pessoa
pessoa1.adicionar_endereco('casa', end1)

pessoa1.adicionar_endereco('trabalho', end2)

# Criando um produto
sabonete = Produto("0010342967", "Sabonete")

##############################################
# Fim do setup
###########################################

def test_busca_nome_e_produto_e_finaliza_pedido():
    pessoas = PessoaFisica.busca_nome('Carlos')

    pessoa = pessoas[0]  #Pega a primeira pessoa

    assert pessoa == pessoa1

    produtos = Produto.busca_nome("sabon")
    
    produto = produtos[0]

    assert produto == sabonete

    carrinho = Carrinho()
    carrinho.adicionar_item(produto, 5)

    pedido = Pedido(pessoa, carrinho)

    ends = pessoa.listar_enderecos()

    if len(ends) > 0:
        endereco = ends['casa']

    # Lembre-se de adicionar estes atributos ao endereço
    pedido.endereco_entrega = copy.deepcopy(endereco) 
    pedido.endereco_faturamento = copy.deepcopy(endereco)


    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado():
        pedido.status = Pedido.PAGO 

    assert pedido.status == 2
    assert str(pedido) == f'Pedido de {pessoa1.nome} - {pessoa1.cpf}, será enviado para {str(end1)} e comprou {carrinho.get_items()}'
    ## Pedido deve imprir todos os detalhes da compra - pessoa, endereço e produtos