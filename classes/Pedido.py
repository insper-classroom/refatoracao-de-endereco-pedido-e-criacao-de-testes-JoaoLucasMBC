#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    
    def __init__(self, cliente:PessoaFisica, carrinho:Carrinho):
        self.endereco_entrega = ''
        self.endereco_faturamento = ''

        self.cliente = cliente
        self.carrinho = carrinho
    
    def __str__(self):
        return f'Pedido de {self.cliente}, será enviado para {self.endereco_entrega}'