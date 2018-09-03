###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Talyta Maria Rosas Pacheco
# Email:	tmrp@cin.ufpe.br
# Data:		2018-08-26
#
# Descricao:   
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Talyta Pacheco
#
###############################################################################

import time

class Cronometro:
    ''' Essa classe inicializa três atributos: tempo inicial, tempo final e status do cronometro.
        A diferença entre os atributos para o tempo resultam no tempo atual.'''
    def __init__(self):
        self.__tempoInicial = 0
        self.__tempoFinal = 0
        self.__parado = True
    def iniciar(self):
        time.clock()
        self.__tempoInicial = time.clock()
        self.__parado = False
    def parar(self):
        self.__tempoFinal = time.clock()
        self.__parado = True
    def zerar(self):
        self.__tempoInicial = 0
        self.__tempoFinal = 0
        self.__parado = True
    def exibir(self):
        if(self.__parado):
            return self.__tempoFinal - self.__tempoInicial
        self.__tempoFinal = time.clock()
        return self.__tempoFinal - self.__tempoInicial
    def __str__(self):
        if(self.__parado):
            return str(self.__tempoFinal - self.__tempoInicial)
        self.__tempoFinal = time.clock()
        return str(self.__tempoFinal - self.__tempoInicial)
    def __repr__(self):
        if(self.__parado):
            status = " Está parado"
        else:
            self.__tempoFinal = time.clock()
            status = " Está rodando"
        return str(self.__tempoFinal - self.__tempoInicial) + status
    def getTempoFinal(self):
        return self.__tempoFinal
    def getTempoInicial(self):
        return self.__tempoInicial
    def getStatus(self):
        return self.__parado
        
