from DoublyLinkedList import *

class Node:
    def __init__(self, chave=None, valor=DoublyLinkedList()):
        self.chave = chave
        self.valor = valor
        self.filhos = [None] * 10

class TrieTree:
    def __init__(self):
        self.raiz = Node()

    def inserir(self, chave, valorDocumento):
        noAtual = self.raiz
        for caractere in chave:
            if(noAtual.filhos[int(caractere)] == None):
                noAtual.filhos[int(caractere)] = Node(caractere)
            noAtual = noAtual.filhos[int(caractere)]
        noAtual.valor.append(valorDocumento)

    def buscar(self,chave):
        noAtual = self.raiz
        for caractere in chave:
            if(noAtual.filhos[int(caractere)!=None]):
                noAtual = noAtual.filhos[int(caractere)]
            else:
                raise KeyError

        if(noAtual.valor == None):
            raise KeyError
        else:
            return noAtual.valor    

    def __getitem__(self, chave):
        self.buscar(chave)

    def __setitem__(self, chave, valor):
        self.inserir(chave,valor)
    
