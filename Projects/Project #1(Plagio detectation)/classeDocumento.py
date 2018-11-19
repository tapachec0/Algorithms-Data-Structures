'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-09-29

 Descricao: classe documento, que contem os metodos de gerar ngramas e contencao 
 Copyright(c) 2018 Talyta Pacheco
 '''

import numpy
from DoublyLinkedList import *
from classeNGrama import NGrama

class Documento:
    
    def __init__(self, documento):

        listaPalavras = DoublyLinkedList()
        self.__nomeArquivo = documento
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
        listaPalavras.append(palavra)
        
        self.__vetorPalavras = numpy.array(listaPalavras)
    
    @property
    def palavras(self):
        return self.__vetorPalavras

    @property
    def NGramas(self):
        return self.__listaNGramas
        
    def gerarNGramas(self, n):
        ''' recebe o tamanho do ngrama a ser gerado, e após cria-los,
        coloca na lista de ngramas'''
        indice = 0
        self.__n = n
        while(indice <= (self.__vetorPalavras.size - self.__n)):
            nGrama = NGrama(indice, indice + (self.__n-1), self)
            self.__listaNGramas.append(nGrama)
            indice += 1

                
    def contencao(self, trieNGramas, limiar):
        ''' recebe uma arvore trie com todos os ngramas de todos os documentos
        da corpus, e faz a contencao do objeto com todos os outros documentos
        que tenham pelo menos um ngrama igual'''
        contencoes = {}
        documentosPossiveisPlagiados = DoublyLinkedList()
        for ngrama in self.NGramas:
            docsEncontrados = trieNGramas[str(ngrama)]
            if not docsEncontrados is None:
                for documento in docsEncontrados:
                    if documento in contencoes:
                        contencoes[documento] += 1
                    else:
                        contencoes[documento] = 1
                        
        for documento in contencoes:
            contencao = contencoes[documento]/len(documento.NGramas)
            if contencao > limiar:
                documentosPossiveisPlagiados.append((documento,contencao))

        return documentosPossiveisPlagiados
    

    def __repr__(self):
        return self.__nomeArquivo

    def __str__(self):
        return self.__repr__()
                    
        
        
        
        
            
            
        
