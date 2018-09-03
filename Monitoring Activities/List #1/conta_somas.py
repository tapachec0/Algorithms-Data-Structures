'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados

Autor:    Antônio Paulino de Lima Neto
Email:    apln2@cin.ufpe.br
Data:        2018-03-01

Descricao:  Algoritmo para contagem de triplas em vetores cuja soma seja zero.


Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
'''
import sys
import numpy
from tmrp_listaMonitoria_if969 import Cronometro

# Lembre-se de importar a sua classe cronometro
#from Cronometro import Cronometro

MAX = 999999

def gera_seq_aleatoria(tam):
   return numpy.random.randint(-MAX,MAX, size=tam)

# Voce deve implementar essa funcao
def conta_somas(vetor):

   quantidadeTriplas = 0
   for primeiroNumero in vetor:
      for segundoNumero in vetor:
         for terceiroNumero in vetor:
            if((primeiroNumero + segundoNumero + terceiroNumero) == 0):
               quantidadeTriplas += 1
   return quantidadeTriplas
            
   
               

def main():
    '''
    Contem os comandos em Python referentes `a implementacao do algoritmo
    '''
    seeds = [11,7,13,19,5189]
    tam = [50,100,250,500,1000]
    for i,seed in enumerate(seeds):
       numpy.random.seed(seed)
       vetor = gera_seq_aleatoria(tam[i])
       cron = Cronometro()
       cron.iniciar()
       total = conta_somas(vetor)
       print("Tempo gasto com {0} elementos foi {1} segundos".format(tam[i],cron))
       del vetor
       del cron


if __name__ == '__main__':
    main()
