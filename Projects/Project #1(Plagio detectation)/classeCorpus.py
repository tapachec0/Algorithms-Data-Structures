'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-11-02

 Descricao: Checa se documentos são plagiados
 Copyright(c) 2018 Talyta Pacheco
 '''

from classeNGrama import NGrama
from classeDocumento import *
from DoublyLinkedList import *
from TrieTree import *
import os

class Corpus:
    def __init__(self, pastaArquivo):
        self.__documentos = self.lerArquivos(pastaArquivo)
        
                           
    def lerArquivos(self, pasta):
        ''' Estancia todos os objetos documento, referentes ao diretorio
        passado pelo usuario, e os coloca na lista de documentos'''
        documentosReferencia = DoublyLinkedList()
        for nomeArquivo in os.listdir(pasta):
            documento = Documento(pasta+"/"+nomeArquivo)
            documentosReferencia.append(documento)
        return documentosReferencia


    def lerNGramas(self, documentos, n):
        ''' Carrega todos os ngramas de todos os documentos da corpus numa
        arvore trie '''
        
        trie = TrieTree()
        for documento in documentos:
            documento.gerarNGramas(n)
            for ngrama in documento.NGramas:
                trie[str(ngrama)] = documento
        return trie

       
    def verificaPlagio(self, documentoSuspeito, limiar, tamanhoNGrama):
        ''' Faz a contencao do documento suspeito passado pelo usuario, e
        retorna uma lista ordenada dos mais provaveis para os menos provaveis
        de terem servido de base para o plágio'''
        
        self.__trieNGramas = self.lerNGramas(self.__documentos, tamanhoNGrama)
        documentoSuspeito.gerarNGramas(tamanhoNGrama)
        contencoes = documentoSuspeito.contencao(self.__trieNGramas, limiar)
  
        return self.ordenarListaTuplas(contencoes)
    
                
    def ordenarListaTuplas(self, listaTuplas):
        ''' Ordena uma lista de tuplas, baseando-se no segundo elemento
        da tupla, e colocando na lista, apenas o primeiro'''
        documentosOrdenados = DoublyLinkedList()
        tamanhoLista = len(listaTuplas)
        contencoes = [x[1] for x in listaTuplas]
        documentos = [x[0] for x in listaTuplas]
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
            listaTuplas.remove((documentos[contMenor],contencoes[contMenor]))
            tamanhoLista -= 1
            
        return documentosOrdenados
           
        
        
