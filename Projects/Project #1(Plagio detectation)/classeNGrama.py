'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-09-29

 Descricao: Formação de vetores de palavras a partir de uma lista de palavras 
 Copyright(c) 2018 Talyta Pacheco
 '''


import numpy

class NGrama:
    def __init__(self, n, listaPalavrasDocumento, indice):
        
        self.__n = n #quantidade de palavras no vetor 
        self.__listaPalavrasDocumento = listaPalavrasDocumento #lista de palavras separadas na classe Documento
        self.__vector = numpy.empty(self.__n, dtype=object)
        self.__indice = indice #indice inicial para pegar palavras da lista
        cont = 0
        while(cont < self.__n):
            self.__vector[cont] = self.__listaPalavrasDocumento[self.__indice]
            self.__indice += 1
            cont += 1

    def __str__(self):
        return str(self.__vector)

    def __repr__(self):
        return str(self.__vector)
    def __eq__(self, otherObject):
        return (self.__vector == otherObject.__vector).all() == True
    
