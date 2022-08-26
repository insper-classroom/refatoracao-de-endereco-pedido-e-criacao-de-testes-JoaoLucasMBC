#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    instancias = []

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}

        Endereco.intancias.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        return {nome:str(self.__enderecos[nome]) for nome in self.__enderecos}
    
    def __str__(self):
        return f'{self.nome} - {self.__cpf}'

    @classmethod
    def busca_nome(cls, nome):
        procura = []

        for obj in cls.instancias:
            if nome.lower() == obj.nome[0:len(nome)].lower():
                procura.append(obj)
        
        return procura