from classeNGrama import NGrama
from classeDocumento import *
from DoublyLinkedList import *
import os

class Corpus:
    def __init__(self, pastaArquivo):
        self.__documentos = self.lerArquivos(pastaArquivo)
    
    def lerArquivos(self, pasta):
        arquivos = DoublyLinkedList()
        for nomeArquivo in os.listdir("dados/"+pasta):
            arquivos.append(nomeArquivo)
        return arquivos
    
    def __str__(self):
        return str(self.__documentos)
   # def verificaPlagio(self, documento, limiar):
        
        
