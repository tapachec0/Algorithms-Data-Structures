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
    def __init__(self, inicio, fim, objetoDocumento):
        
        self.__intervalo = numpy.array([inicio, fim])
        self.__documento = objetoDocumento
        
    def __str__(self):
        return ' '.join(self.__documento.palavras[i] for i in range (
                self.__intervalo[0], self.__intervalo[1]+1))

    def __repr__(self):
        return self.__str__()
        
    def __eq__(self, outro):
        return str(outro) == self.__str__()
    

