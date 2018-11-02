from DoublyLinkedList import *

class Node:
    def __init__(self, chave=None, valor=DoublyLinkedList()):
        self.chave = chave
        self.valor = valor
        self.filhos = {}

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
            if not caractere in noAtual.filhos:
                noAtual.filhos[caractere] = Node(caractere, DoublyLinkedList())
            noAtual = noAtual.filhos[caractere]
        if not valorDocumento in noAtual.valor:
            noAtual.valor.append(valorDocumento)

    def buscar(self,chave):
        ''' Recebe uma chave, e retorna o valor que está contido no ultimo nó '''
        noAtual = self.raiz
        for caractere in chave:
            if caractere in noAtual.filhos:
                noAtual = noAtual.filhos[caractere]
            else:
                return None
        if(len(noAtual.valor) == 0):
            return None
        else:
            return noAtual.valor    

    def __getitem__(self, chave):
        self.buscar(chave)

    def __setitem__(self, chave, valor):
        self.inserir(chave,valor)
    
