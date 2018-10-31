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

from classeCorpus import *
from classeNGrama import NGrama
from classeDocumento import *
from DoublyLinkedList import *
import cProfile,pstats,io
from memory_profiler import profile
import os


def profileTime(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, *kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        arq = open("profileTime.txt", "w")
        arq.write(s.getvalue())
        arq.close()
        return retval
    return inner

@profileTime
@profile
def main_profileTime():
    documentoSuspeito = Documento("dados/susp/suspicious-document00044.txt")
    corpus = Corpus("dados/teste-src")
    listaOrdenados = corpus.verificaPlagio(documentoSuspeito, 0.20, 3)
    
if __name__ == "__main__":
    main_profileTime()
    
    











