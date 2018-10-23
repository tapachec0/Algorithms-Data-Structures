'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-09-29

 Descricao: Checa se documentos são plagiados
 Copyright(c) 2018 Talyta Pacheco
 '''

from classeNGrama import NGrama
from classeDocumento import *
from DoublyLinkedList import *
import os

class Corpus:
    def __init__(self, pastaArquivo):
        self.__documentos = self.lerArquivos(pastaArquivo)
    
    def lerArquivos(self, pasta):
        documentosReferencia = DoublyLinkedList()
        for nomeArquivo in os.listdir(pasta):
            documento = Documento(pasta+"/"+nomeArquivo)
            documentosReferencia.append(documento)
        return documentosReferencia
   

    def verificaPlagio(self, documentoSuspeito, limiar, tamanhoNGrama):
        documentosPossiveisPlagiados = DoublyLinkedList()
        documentosOrdenados = DoublyLinkedList()
        documentoSuspeito.gerarNGramas(tamanhoNGrama)
        for documento in self.__documentos:
            contencao = documentoSuspeito.contencao(documento)
            if contencao > limiar:
                documentosPossiveisPlagiados.append((documento,contencao))
                
        tamanhoLista = len(documentosPossiveisPlagiados)
        contencoes = [x[1] for x in documentosPossiveisPlagiados]
        documentos = [x[0] for x in documentosPossiveisPlagiados]
        while(tamanhoLista > 0):
            menor = contencoes[0]
            cont = 0
            contMenor = 0
            for x in contencoes:
                if x > menor:
                    menor = x
                    contMenor = cont
                cont += 1

            
            documentosOrdenados.append(documentos[contMenor])
            documentosPossiveisPlagiados.remove((documentos[contMenor],contencoes[contMenor]))
            tamanhoLista -= 1
            
            
        return documentosOrdenados
           
        
        
