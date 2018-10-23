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
from DoublyLinkedList import *
from classeNGrama import NGrama

class Documento:
    
    def __init__(self, documento):
        
        listaPalavras = DoublyLinkedList()
        self.__listaNGramas = DoublyLinkedList()
        self.__arquivo = open(documento, "r", encoding="utf8")
        palavra = ""
        linha = self.__arquivo.readline()
        while(linha != ""):
            for caractere in linha:
                if(caractere == " " or caractere == "." or caractere == ","
                   or caractere == "\n"):
                    if(palavra != ""):
                        listaPalavras.append(palavra)
                        palavra = ""
                else:
                    palavra += caractere
            linha = self.__arquivo.readline()

        self.__vetorPalavras = numpy.asarray(listaPalavras)
       
        
    def gerarNGramas(self, n):

        indice = 0
        self.__n = n
        while(indice <= (self.__vetorPalavras.size - self.__n)):
            nGrama = NGrama(self.__n, self.__vetorPalavras, indice)
            self.__listaNGramas.append(nGrama)
            indice += 1

        
    def contencao(self, documentoSuspeito):
        
        documentoSuspeito.gerarNGramas(self.__n)
        conjuntoNGramasIguais = 0
        for nGramaOficial in self.__listaNGramas:
            for nGramaSuspeito in documentoSuspeito.__listaNGramas:
                if(nGramaOficial == nGramaSuspeito):
                    conjuntoNGramasIguais += 1
                    
               
                
        contencao = conjuntoNGramasIguais / len(documentoSuspeito.__listaNGramas)
        return contencao
        
                    
        
        
        
        
            
            
        
