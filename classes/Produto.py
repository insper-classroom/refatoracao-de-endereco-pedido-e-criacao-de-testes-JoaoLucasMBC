#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    instancias = []

    def __init__(self, id, nome=''):
        self.__id = id
        self.__nome = nome

        self.__class__.instancias.append(self)
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_novo):
        self.__id = id_novo
    
    @id.getter
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo
    
    @nome.getter
    def nome(self):
        return self.__nome
    
    def to_dict(self):
        return {
            'id':self.__id,
            'nome':self.__nome
        }
    
    def busca_nome(cls, nome):
        procura = []

        for obj in cls.instancias:
            if nome.lower() == obj.nome[0:len(nome)].lower():
                procura.append(obj)
        
        return procura