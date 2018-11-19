'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-11-02

 Descricao: Estrutura de dados que armazena chaves e seus respectivos valores
 Copyright(c) 2018 Talyta Pacheco
 '''

from DoublyLinkedList import *
import numpy

class Node:
    def __init__(self, chave=None, valor=DoublyLinkedList()):
        self.chave = chave
        self.valor = valor
        self.filhos = numpy.empty(0, dtype=object)

    def __eq__(self, outro):
        return self.chave == outro.chave


class TrieTree:
    def __init__(self):
        self.raiz = Node()

    def inserir(self, chave, valorDocumento):
        ''' Metodo que insere uma chave e um valor na arvore. A cada caractere
        da chave, se não existir um nó com o valor do caractere nos filhos do
        nó atual, um nó é criado com a chave sendo o caractere. Somente ao final
        da iteração, no ultimo nó, o valor é adicionado'''
        noAtual = self.raiz
        for caractere in chave:
            novoNo = Node(caractere, DoublyLinkedList())
            if not novoNo in noAtual.filhos:
                noAtual.filhos = numpy.append(noAtual.filhos, novoNo)
                noAtual = novoNo
            else:
                indice = numpy.where(noAtual.filhos == novoNo)[0][0]
                noAtual = noAtual.filhos[indice]
        noAtual.valor.append(valorDocumento)

    def buscar(self,chave):
        ''' Recebe uma chave, e retorna o valor que está contido no ultimo nó '''
        noAtual = self.raiz
        for caractere in chave:
            noAux = Node(caractere, DoublyLinkedList())
            if noAux in noAtual.filhos:
                indice = numpy.where(noAtual.filhos == noAux)[0][0]
                noAtual = noAtual.filhos[indice]
            else:
                return None
        if(len(noAtual.valor) == 0):
            return None
        else:
            return noAtual.valor    

    def __getitem__(self, chave):
        ''' metodo especial que permite buscar na lista usando colchetes'''
        return self.buscar(chave)

    def __setitem__(self, chave, valor):
        ''' metodo especia que permite adicionar ou mudar valor de determinada
        chave '''
        self.inserir(chave,valor)
    
