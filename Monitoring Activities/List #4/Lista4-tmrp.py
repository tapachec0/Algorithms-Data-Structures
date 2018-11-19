'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Talyta Maria Rosas Pacheco
 Email:	tmrp@cin.ufpe.br
 Data:	2018-11-19
  
 Copyright(c) 2018 Talyta Pacheco
 '''
class GraficoLista():
    '''
    Grafo que usa listas para armazenas os adjacentes. Essa implementação
    tem uma grande vantagem de custo de memoria em relação ao uso de matriz,
    principalmente para grafos escassos, pois as listas começam vazias, e só
    vai aramazenar adjacentes quando arestas forem adicionadas. Também retorna
    os adjacentes de determinado vertice de maneira mais rápida, pois a lista
    de adjacentes de um vertice, já são os proprios adjacentes, diferentemente
    da matriz, que é composta de 0 e 1 (ou o peso). Porem, essa implementação
    é menos trivial na hora de checar se existe aresta entre dois vertices,
    porque é preciso varrer a lista de adjacencia procurando o possivel
    adjacente. 
    '''
    def __init__(self, qtdVertices, arestas=[], direcionado=False, peso=False):
        self.vertices = qtdVertices
        self.numeroArestas = 0
        self.__direcionado = direcionado
        self.__peso = peso
        self.__listaAdj = []

        for vertice in range(self.vertices):
            self.__listaAdj.append([])
            
        if not self.__peso:
            for aresta in arestas:
                    self.addAresta(aresta[0],aresta[1])
        else:
            for aresta in arestas:
                self.addAresta(aresta[0],aresta[1],aresta[2])
    

    def addAresta(self,u,v,peso=0): 
        '''
        Insere arestas no grafo. Se o grafo não for direcionado, insere tanto
        de u até v, quanto de v até u
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):
            if not self.__peso:
                if not v in self.__listaAdj[u]:
                    self.__listaAdj[u].append(v)
                    self.numeroArestas += 1
                    if not self.__direcionado and u != v:
                        self.__listaAdj[v].append(u)
                else:
                    raise IndexError ("Aresta ja existente")
            else:
                for adj in self.__listaAdj[u]:
                    if adj[0] == v:
                        raise IndexError ("Aresta ja existente")
                self.__listaAdj[u].append((v,peso))
                self.numeroArestas += 1
                if not self.__direcionado and u != v:
                    self.__listaAdj[v].append((u,peso))
        else:
            raise IndexError ("Pelo menos um dos vertices nao existe no grafo")


    def removerAresta(self,u,v): 
        '''
        Remove v dos adjacentes de u. se for direcionado, tambem remove u dos
        adjacente de v
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):  
            if not self.__peso:
                if v in self.__listaAdj[u]:
                    self.__listaAdj[u].remove(v)
                    self.numeroArestas -= 1
                    if not self.__direcionado:
                        self.__listaAdj[v].remove(u)
                else:
                    raise IndexError ("Pelo menos um vertice nao existe")
            else:
                for adj in self.__listaAdj[u]:
                    if adj[0] == v:
                        self.__listaAdj[u].remove(adj)
                        self.numeroArestas -= 1
                if not self.__direcionado:
                    for adj in self.__listaAdj[v]:
                        if adj[0] == u:
                            self.__listaAdj[v].remove(adj)
        else:
            raise IndexError ("Pelo menos um dos vertices nao existe no grafo")


    def existeAresta(self,u,v): 
        '''
        Verifica se existe aresta entre u e v
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):
            if not self.__peso:
                if u in self.__listaAdj[v]:
                    return True
                if self.__direcionado:
                    if v in self.__listaAdj[u]:
                        return True
                return False
            else:
                for adj in self.__listaAdj[v]:
                    if adj[0] == u:
                        return True
                if self.__direcionado:
                    for adj in self.__listaAdj[u]:
                        if adj[0] == v:
                            return True
                return False
                    
        raise IndexError ("Pelo menos um dos vertices nao existe no grafo")

    def grauEntrada(self,v): 
        '''
        Retorna o grau de entrada do vertice(quantos vertices tem esse vertice
        como adjacente
        '''
        if self.__existeVertice(v):
            if not self.__direcionado:
                return len(self.__listaAdj[v])
        
            grauEntrada = 0
            if not self.__peso:
                for lista in self.__listaAdj:
                    if v in lista:
                        grauEntrada += 1
            else:
                for lista in self.__listaAdj:
                    for adj in lista:
                        if adj[0] == v:
                            grauEntrada+=1
            return grauEntrada
        else: raise IndexError ("Vertice nao existe no grafo")
            
        
    def grauSaida(self,v): 
        '''
        Retorna o grau de saida de v (um inteiro de quantos vertices sao
        adjacentes a v)
        '''
        return len(self.__listaAdj[v])
        
    
    @property
    def tree(self):
        '''
        Retorna um booleano True, se o grafo é uma arvore ou False, se não for
        '''
        if self.numeroArestas == self.vertices-1:
            antecessores = buscaLargura(self)
            for i in range(1,self.vertices):
                if antecessores[i] == -1:
                    return False
            return True
        return False

    def conversao(self): 
        '''
        retorna um objeto grafo matriz
        '''
        arestas = []
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if not self.__peso:
                        arestas.append((vertice,adj))
                    else:
                        arestas.append((vertice,adj[0],adj[1]))
        else:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if adj >= vertice:
                        if not self.__peso:
                            arestas.append((vertice,adj))
                        else:
                            arestas.append((vertice,adj[0],adj[1]))
            
        grafoMatriz = GraficoMatriz(self.vertices,arestas,self.__direcionado,
                                  self.__peso)

        return grafoMatriz

    def __existeVertice(self, v): 
        '''
        Verifica se o vertice existe no grafo
        '''
        if 0 <= v and  v < self.vertices:
            return True
        return False
    
    def __getitem__(self,v): 
        '''
        Retorna todas as arestas que se conectam a v
        '''
        if self.__existeVertice(v):
            arestas = []
            if not self.__peso:
                for adj in self.__listaAdj[v]:
                    arestas.append((v,adj))   
            else:
                for adj in self.__listaAdj[v]:
                    arestas.append((v,adj[0],adj[1]))
                    
            return arestas
        else: raise IndexError ("Vertice nao existente no grafo")
        
        return arestas

    def __repr__(self):
        if self.numeroArestas == 0:
            return "GraficoLista()"
            
        grafo = "GraficoLista("
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if not self.__peso:
                        grafo+=("({},{}),").format(vertice,adj)
                    else:
                        grafo+=("({},{},{}),").format(vertice,adj[0],adj[1])
        else:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if adj >= vertice:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            grafo+=("({},{},{}),").format(vertice,adj[0],adj[1])
        grafo = grafo[:len(grafo)-1] + ")"
                 
        return grafo   


    def __str__(self):
        if self.numeroArestas == 0:
            return "[]"
        grafo = "["
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if not self.__peso:
                        grafo+=("({},{}),").format(vertice,adj)
                    else:
                        grafo+=("({},{},{}),").format(vertice,adj[0],adj[1])
        else:
            for vertice in range(self.vertices):
                for adj in self.__listaAdj[vertice]:
                    if adj >= vertice:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            grafo+=("({},{},{}),").format(vertice,adj[0],adj[1])
                               
        grafo = grafo[:len(grafo)-1] + "]"
        
        return grafo





    
#=================================GrafoMatriz==================================


class GraficoMatriz():
    '''
    A implementação por matriz de adjacência guarda informações sobre como os
    vértices vi e vj estão relacionados (isto é, informações sobre a adjacência
    de vi e vj). Essa relação de adjacência é identificada por 0 e 1
    (não-adjacente e adjacente, respectivamente), quando as arestas não possuem
    peso. Já quando possuem peso, o 1 representado na matriz é trocado pelo peso
    da aresta. A desvantagem desse tipo de implementação deve-se ao grande
    espaço ocupado, que é O(v²), por isso para grafos escassos é melhor usar
    lista de adjacencia. Além disso, a procura pelo vértice adjacente
    a outro vértice i, deve-se olhar para todas as entradas |V| na coluna i,
    mesmo quando o número de vértices adjacentes é pequeno. Por outro lado,
    a vantagem deve-se aos métodos de Remoção de Arestas (custo O(1)), pois
    só é preciso acessar a posição vi na matriz e trocar por 0, e Checar
    Existência de Arestas que tambem é O(1).
    '''
    def __init__(self, qtdVertices, arestas=[], direcionado=False, peso=False):
        self.vertices = qtdVertices
        self.numeroArestas = 0
        self.__direcionado = direcionado
        self.__peso = peso
        self.__matrizAdj = [] 

        for vertice in range(self.vertices):
            self.__matrizAdj.append([0] * self.vertices)

        if not self.__peso:
            for aresta in arestas:
                    self.addAresta(aresta[0],aresta[1])
        else:
            for aresta in arestas:
                self.addAresta(aresta[0],aresta[1],aresta[2])

    def addAresta(self,u,v, peso=0):
        '''
        Insere arestas no grafo. Se o grafo não for direcionado, insere tanto
        de u até v, quanto de v até u
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):
            if not self.__peso:
                self.__matrizAdj[u][v] = 1
                self.numeroArestas+=1
                if not self.__direcionado:
                    self.__matrizAdj[v][u] = 1
            else:
                self.__matrizAdj[u][v] = peso
                self.numeroArestas+=1
                if not self.__direcionado:
                    self.__matrizAdj[u][v] = peso
        else:
            raise IndexError ("Pelo menos um dos vertices nao existe no grafo")
        

    def removerAresta(self,u,v):
        '''
        Remove v dos adjacentes de u. se for direcionado, tambem remove u dos
        adjacente de v
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):
            self.__matrizAdj[u][v] = 0
            self.numeroArestas-=1
            if not self.__direcionado:
                self.__matrizAdj[v][u] = 0
        else:
            raise IndexError ("Pelo menos um dos vertices nao existe no grafo")


    def existeAresta(self,u,v):
        '''
        Verifica se existe aresta entre u e v
        '''
        if self.__existeVertice(u) and self.__existeVertice(v):
            if self.__matrizAdj[u][v] != 0:
                return True
            if self.__direcionado:
                if self.__matrizAdj[v][u] != 0:
                    return True
            return False
        else:
            raise IndexError ("Pelo menos um dos vertices nao existe no grafo")
        
        

    def grauEntrada(self,v):
        '''
        Retorna o grau de entrada do vertice(quantos vertices tem esse vertice
        como adjacente
        '''
        if self.__existeVertice(v):
            if not self.__direcionado:
                return self.grauSaida(v)
            else:
                grauSaida = 0
                for listaVertice in self.__matrizAdj:
                    if listaVertice[v] != 0:
                        grauSaida += 1
                return grauSaida
        else:
            raise IndexError ("O vertice nao existe no grafo")
                    
                    

    def grauSaida(self,v):
        '''
        Retorna o grau de saida de v (um inteiro de quantos vertices sao
        adjacentes a v
        '''
        if self.__existeVertice(v):
            grauSaida = 0
            for vertice in self.__matrizAdj[v]:
                if vertice != 0:
                    grauSaida += 1
            return grauSaida
        else:
            raise IndexError ("O vertice nao existe no grafo")
             
            
    @property
    def tree(self):
        '''
        Retorna True, se o grafo for uma arvore ou False, se não for
        '''
        if self.numeroArestas == self.vertices-1:
            antecessores = buscaLargura(self)
            for i in range(1,self.vertices):
                if antecessores[i] == -1:
                    return False
            return True
        else:
            return False
        
    def conversao(self):
        '''
        Converte o grafo para usar lista de adjacencia
        '''
        arestas = []
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in range(self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            arestas.append((vertice,adj))
                        else:
                            self.__matrizAdj[vertice][adj]
                            arestas.append((vertice,adj,peso))
        else:
            for vertice in range(self.vertices):
                for adj in range(vertice,self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            arestas.append((vertice,adj))
                        else:
                            self.__matrizAdj[vertice][adj]
                            arestas.append((vertice,adj,peso))
        grafoLista = GrafoLista(self.vertices,arestas,self.__direcionado,
                                self.__peso)
        return grafoLista

    def __existeVertice(self, v): 
        '''
        Verifica se o vertice existe no grafo
        '''
        if 0 <= v and  v < self.vertices:
            return True
        return False

    def __getitem__(self,v):
        '''
        Retorna todas as arestas que se conectam a v
        '''
        if self.__existeVertice(v):
            arestas = []
            if not self.__peso:
                for adj in range(self.vertices):
                    if self.__matrizAdj[v][adj] != 0:
                        arestas.append((v,adj))
            else:
                for adj in range(self.vertices):
                    if self.__matrizAdj[v][adj] != 0:
                        arestas.append((v,adj,self.__matrizAdj[v][adj]))
            return arestas
        else:
            raise IndexError ("O vertice nao existe no grafo")
        
    def __repr__(self):
        grafo = "GraficoLista("
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in range(self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            peso = self.__matrizAdj[vertice][adj]
                            grafo+=("({},{},{}),").format(vertice,adj,peso)
        else:
            for vertice in range(self.vertices):
                for adj in range(vertice, self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            peso = self.__matrizAdj[vertice][adj]
                            grafo+=("({},{},{}),").format(vertice,adj,peso)
        grafo = grafo[:len(grafo)-1] + ")"
                 
        return grafo   

    def __str__(self):
        grafo = "["
        if self.__direcionado:
            for vertice in range(self.vertices):
                for adj in range(self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            peso = self.__matrizAdj[vertice][adj]
                            grafo+=("({},{},{}),").format(vertice,adj,peso)
        else:
            for vertice in range(self.vertices):
                for adj in range(vertice, self.vertices):
                    if self.__matrizAdj[vertice][adj] != 0:
                        if not self.__peso:
                            grafo+=("({},{}),").format(vertice,adj)
                        else:
                            peso = self.__matrizAdj[vertice][adj]
                            grafo+=("({},{},{}),").format(vertice,adj,peso)
        grafo = grafo[:len(grafo)-1] + "]"
                 
        return grafo     

#==============================================================================
def buscaProfundidade(grafo):
    '''
    Essa implementacao usa o getitem das classes grafo lista e grafo matriz
    para retornar os adjacentes do vertice em forma de tuplas, por isso é
    acessado o adjacente indice 1 - u[1]
    '''
    marcados = grafo.vertices * [False]
    antecessores = grafo.vertices * [-1]
    for v in range (g.vertices):
        if marcados[v] == False:
            dfs(grafo,v,antecessores,marcados)
    del marcados
    return antecessores

def dfs(g,v,antecessor,marcado):
    marcado[v] = True
    for u in g[v]:
        if marcado[u[1]] == False:
            antecessor[u[1]] = v
            dfs(g,u[1],antecessor,marcado)
            
            
def buscaLargura(grafo):
    '''
    Essa implementacao usa o getitem das classes grafo lista e grafo matriz
    para retornar os adjacentes do vertice em forma de tuplas, por isso é
    acessado o adjacente indice 1 - u[1]
    '''
    marcados = grafo.vertices * [False]
    antecessores = grafo.vertices * [-1]
    vertices = []
    
    for i in range(grafo.vertices):
        if marcados[i] == False:
            vertices.append(i)
            marcados[i] = True
            
            while len(vertices) > 0:
                v = vertices[0]
                del vertices[0]
                
                for u in grafo[v]:
                    if marcados[u[1]] == False:
                        marcados[u[1]] = True
                        antecessores[u[1]] = v
                        vertices.append(u[1])
    del marcados
    return antecessores

#==============================================================================

g = GraficoLista(7,[(0,1),(1,2),(1,3),(2,3),(2,4),(4,6),(5,6)])

print(buscaLargura(g))

if not g.tree:
    print("nao é uma arvore")

g2 = g.conversao()
print(buscaProfundidade(g2))

g2.removerAresta(2,3)
if g2.tree:
    print("é uma arvore")

g3=GraficoMatriz(7,[(0,1,3),(1,2,5),(1,3,7),(2,4,2),(4,6,9),(5,6,9)],True,True)






