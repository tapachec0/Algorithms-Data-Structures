import numpy
from DoublyLinkedList import *
from classeNGrama import NGrama

class Documento:
    
    def __init__(self):
        
        listaPalavras = DoublyLinkedList()
        self.__listaNGramas = DoublyLinkedList()
        self.__arquivo = open("source-document00010.txt", "r")
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
        print(self.__vetorPalavras)


    def gerarNGramas(self, n):

        indice = 0
        self.__n = n
        while(indice <= (self.__vetorPalavras.size - self.__n)):
            nGrama = NGrama(self.__n, self.__vetorPalavras, indice)
            self.__listaNGramas.append(nGrama)
            indice += 1

        print(self.__listaNGramas)
            
            
        
