class Node:
    
    def __init__(self, item = None, previous = None, after = None):
        
        self.item = item
        self.prev = previous
        self.after = after
        
    def __str__(self):
        
        return str(self.item)

    def __repr__(self):
        
        return repr(self.item)

class DoublyLinkedList:

    def __init__(self, iterable = None):
        '''
        Construtor recebe iteráveis. Por padão é None, que é uma lista vazia
        '''
        self.head = Node()
        if(iterable == None):
            self.tail = self.head
            
        else:
            aux = self.head
            for element in iterable:
                #construindo a lista, começando pelo próximo elemento da cabeça
                aux.after = Node(element, aux)
                aux = aux.after
            #o fim é o último elemento adicionado
            self.tail = aux
                

    def isEmpty(self):
        
        if(self.head == self.tail):
            return True
        
        else:
            return False
        
    def append(self, item):
        '''
        Adicionar um item no fim da lista
        '''
        #o proximo elemento do outro --> Nó
        self.tail.after = Node(item, self.tail)
        #atualização do último elemento
        self.tail = self.tail.after

    def insertByIndex(self, item, index):
        '''
        Insere um elemento na lista, em um índice desejado. Caso o índice seja maior que o tamanho da lista, adiciona na última posição
        '''
        if(index < self.__len__()):
            cont = 0
            aux = self.head.after
            while(cont != index):
                aux = aux.after
                cont += 1
            aux.prev = Node(item, aux.prev, aux)
            aux.prev.prev.after = aux.prev
            
        else:
            return self.append(item)

    #padaro ultimo
    def pop(self, index):
        '''
        Remove o elemento de um índice desejado. Sendo por padrão, o último índice
        '''
        if(self.isEmpty()):
            print("List is empty")
            
        elif(index > (self.__len__()-1)):
            raise IndexError("Index out of Range")
        
        else:
            aux = self.head.after
            cont = 0
            while(cont != index):
                aux = aux.after
                cont += 1
            aux.prev.after = aux.after
            
            #caso o elemento que foi removido seja o ultimo, altera a ligação do último para o anterior do último
            if(aux.after == None):
                self.tail = aux.prev
            else:
                aux.after.prev = aux.prev
            valueReturn = aux
            del aux
            #devolve o valor retirado
            return valueReturn
        
    def remove(self, item):
        '''
        Remove o nó que contém o item passado pelo usuario. Caso haja mais de um nós com esse elemento, remove apenas o primeiro
        '''
        if(self.isEmpty()):
            print("List is empty")
            
        elif(self.__contains__(item) == False):
            raise ValueError("Item not found")
        
        else:
            aux = self.head.after
            while(aux.item != item):
                aux = aux.after
            aux.prev.after = aux.after
            if(aux.after == None):
                self.tail = aux.prev
            else:
                aux.after.prev = aux.prev
            
            del aux
            
    def eliminate(self, item):
        '''
        Retira da lista, todos os nós os nós que possuem o valor passado pelo usuario
        '''
        if(self.isEmpty()):
            print("List is empty")
            
        elif(self.__contains__(item) == False):
            raise ValueError("Item not found")
        
        else:
            cont = 0
            tam = self.__len__()
            aux = self.head.after
            while(cont < tam):
                keepFinding = aux
                if(aux.item == item):
                    if(aux.after == None):
                        aux.prev.after = aux.after
                        self.tail = aux.prev
                    else:
                        aux.prev.after = aux.after
                        aux.after.prev = aux.prev
                    del keepFinding
                aux = aux.after
                cont += 1

    def research(self, item):
        '''
        Devolve para o usuário o índice do valor desejado na lista
        '''
        if(self.__contains__(item) == False):
            raise ValueError("Item not found")
        
        else:
            cont = 0
            aux = self.head.after
            found = False
            while(found == False):
                if(aux.item == item):
                    found = True
                    return "Index de %s é "%(item) + str(cont)
                aux = aux.after
                cont += 1
                
    def copy(self):
        '''
        Faz uma cópia de uma lista duplamente encadeada
        '''
        #novo objeto do tipo lista encadeada
        self.newObject = DoublyLinkedList()
        cont = 0
        aux = self.head.after
        #tamanho da lista que será copiada
        tam =  int(self.__len__())
        
        while(cont < tam):
            #construção da lista por vários appends, até chegar ao tamanho da lista original
            self.newObject.append(aux.item)
            aux = aux.after
            cont += 1
        self.tail = aux

        #devolve a cópia
        return self.newObject
        
    def extend(self, iterable):
        '''
        Põe ao final da lista, um objeto iteravel
        '''
        for item in iterable:
            self.append(item)

                
    def switch(self, index1, index2):
        '''
        Troca os nós de uma lista que possui os indices passados pelo usuario: o primerio e segundo indices que deseja trocar de posição na lista
        '''
        if(index1 > (self.__len__()-1) or index2 > (self.__len__()-1)):
            raise IndexError("Index out of range")

        else:
            cont = 0
            aux = self.head.after
            self.secondValue = self.firstValue = 0
            
            while(cont != index1):
                aux = aux.after
                cont += 1

            #get o valor do primeiro indice do usuario
            self.firstValue = aux.item

            #reseta o auxiliar e cont para encontrar o valor do segundo índice
            cont = 0
            aux = self.head.after
            
            while(cont != index2):
                aux = aux.after
                cont += 1
           
            self.secondValue = aux.item

            #utiliza a função setitem para trocar de posição. O primerio indice recebe o segundo, e o outro o inverso
            self.__setitem__(index1, self.secondValue)
            self.__setitem__(index2, self.firstValue)
            
    def __iter__(self):
        #torna o objeto da lista duplamente encadeada iteravel
        return DoublyLinkedListIterator(self)
            
    def __contains__(self, item):
        '''
        Verifica se há um elemento passado pelo usuario na lista
        '''
        aux = self.head.after
        #tag para auxiliar o encontro
        found = False
        
        while(found == False):
            #caso o aux seja None, significa que chegou ao final, já que não há, agr, nenhum valor guardado. Logo, não encontrou o elemento
            if(aux == None):
                return False
            
            if(aux.item == item):
                found = True
                return True
            
            aux = aux.after
        
                
    def __getitem__(self, index):
        '''
        Retorna o valor de um indice. Implementa a seguinte chamada: lista[indice]
        '''
        if(self.isEmpty()):
            print("List is empty")
            
        elif(index > (self.__len__()-1)):
            raise IndexError("Index out of Range")
        
        else:
            found = False
            cont = 0
            aux = self.head.after
            while(found == False):
                if(cont == index):
                    found = True
                    return aux
                aux = aux.after
                cont += 1
                
    def __setitem__(self, index, item):
        '''
        Troca o valor de um indice. Implementa a seguinte chamada: lista[indice] = valor
        '''
        if(index > (self.__len__()-1)):
            raise IndexError("Index out of Range")
        
        else:
            cont = 0
            aux = self.head.after
            while(cont != index):
                aux = aux.after
                cont += 1
            aux.item = item


    def __len__(self):
        
        cont = 0
        aux = self.head
        while(aux.after != None):
            aux = aux.after
            cont += 1
            
        return cont

    def __str__(self):
        
        string = "["
        cont = 0
        aux = self.head
        while(cont < self.__len__()):
            if(aux.after.after == None):
                string += repr(aux.after)
            else:
                string += repr(aux.after) + "," + " "
            cont += 1
            aux = aux.after

        string += "]"
        return string
    
    def __repr__(self):
        
        string = "DoublyLinkedList(["
        cont = 0
        aux = self.head
        while(cont < self.__len__()):
            if(aux.after.after == None):
                string += repr(aux.after)
            else:
                string += repr(aux.after) + "," + " "
            cont += 1
            aux = aux.after

        string += "])"
        return string
    
    

class DoublyLinkedListIterator:
    
    def __init__(self, doublyLinkedList):
        self.firstPosition = doublyLinkedList.head
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.firstPosition = self.firstPosition.after
        if(self.firstPosition == None):
            raise StopIteration
        return self.firstPosition.item
   


def concanate(list1, list2):
    '''
    Junta duas listas. O princípio é ligar como o proximo elemento do ultimo da primeira lista ao primeiro elemento da segunda lista.
    '''
    list1.tail.after = list2.head.after
    return list1
