import numpy

class Polinomio:
    def __init__(self, *args):
        supostoMaiorGrau = (len(args)-1)
        self.vetor = numpy.array(args)
        self.maiorGrau = 0
        achou = False
        for coeficiente in args:
            if(coeficiente != 0 and achou == False):
                self.maiorGrau = supostoMaiorGrau
                achou = True
                print("Maior grau", self.maiorGrau)
            supostoMaiorGrau -=1
    def derivar(self):
        grau = (len(self.vetor)-1)
        listCoeficientesDerivada = []
        for coeficiente in self.vetor:
            if(grau != 0):
                derivada = coeficiente * grau
                listCoeficientesDerivada.append(derivada)
                derivada = 0
            grau -= 1
        vetorCoeficientesDerivada = numpy.array(listCoeficientesDerivada)
       
        resultadoDerivada = Polinomio(*vetorCoeficientesDerivada)
        print("A derivada é: ", resultadoDerivada)
        
                
    def __call__(self, valorX):
        grau = (len(self.vetor)-1)
        resultadoPolinomio = 0
        for coeficiente in self.vetor:
            resultadoPolinomio += (coeficiente * (valorX ** grau))
            grau -= 1
        return "Resultado do polinomio: " + str(resultadoPolinomio)
    def __getitem__(self, indice):
        grau = (len(self.vetor)-1)
        monomio = 0
        achou = False
        if(indice > grau):
             raise ArithmeticError('Indice inexistente!')
        for coeficiente in self.vetor:
            if(grau == indice and achou == False):
                monomio = coeficiente
                achou = True
            grau -= 1
        vetorZeros = numpy.zeros(indice,int)
        resultado = Polinomio(monomio,*vetorZeros)
        return resultado
    
    def __str__(self):
        grau = (len(self.vetor)-1)
        string = "f(x) = "
        for coeficiente in self.vetor:
            if(coeficiente != 0):
                if(grau != 0 and coeficiente < 0):
                    string += str(coeficiente) + "x^" + str(grau)
                elif(grau != 0 and coeficiente > 0):
                    if(grau == (len(self.vetor)-1)):
                        string += str(coeficiente) + "x^" + str(grau)
                    else:
                        string += "+" + str(coeficiente) + "x^" + str(grau) 
                else:
                    string += "+" + str(coeficiente)
            grau -= 1
        return string

    def __repr__(self):
        grau = (len(self.vetor)-1)
        string = "Polinomio("
        numeroDiferenteZero = False
        for coeficiente in self.vetor:
            if(coeficiente != 0 and numeroDiferenteZero == False):
                numeroDiferenteZero = True
            if(numeroDiferenteZero == True):
                if(grau == 0):
                    string += str(coeficiente) + ")"
                else:
                    string += str(coeficiente) + ","
            grau -= 1
                
        return string
        
        
            
            
        
            
            
            
        
        
    
            
        
        
                
             
    
    
