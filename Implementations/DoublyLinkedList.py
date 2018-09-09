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
        
        self.head = Node()
        if(iterable == None):
            self.tail = self.head
            
        else:
            cont = 0
            aux = self.head
            
            if(type(iterable) == str):
                string = ""
                while(cont < len(iterable)):
                    char = iterable[cont]
                    string += char
                    cont += 1
                aux.after = Node(string, aux)
                aux = aux.after
                
            else:
                while(cont < len(iterable)):
                    aux.after = Node(iterable[cont],aux)
                    aux = aux.after
                    cont += 1
            self.tail = aux

    def isEmpty(self):
        
        if(self.__len__() == 0):
            return True
        
        else:
            return False
        
    def append(self, item):
        
        self.tail.after = Node(item, self.tail)
        self.tail = self.tail.after

    def insertByIndex(self, item, index):
        
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

    def pop(self, index):
        
        if(self.isEmpty()):
            print("List is empty")
            
        elif(index > self.__len__()):
            raise IndexError("Index out of Range")
        
        else:
            aux = self.head.after
            cont = 0
            while(cont != index):
                aux = aux.after
                cont += 1
            aux.prev.after = aux.after
            aux.after.prev = aux.prev
            valueReturn = aux
            del aux
            return valueReturn
        
    def remove(self, item):
        
        if(self.isEmpty()):
            print("List is empty")
            
        elif(self.__contains__(item) == False):
            raise ValueError("Item not found")
        
        else:
            aux = self.head.after
            while(aux.item != item):
                aux = aux.after
            aux.prev.after = aux.after
            aux.after.prev = aux.prev
            del aux
            
    def eliminate(self, item):
        
        if(self.__contains(item) == False):
            raise ValueError("Item not found")
        
        else:
            cont = 0
            aux = self.head.after
            while(cont < self.__len__()):
                keepFinding = aux
                if(aux.item == item):
                    aux.prev.after = aux.after
                    aux.after.prev = aux.prev
                    del keepFinding
                aux = aux.after
                cont += 1

    def research(self, item):
        
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
                
    def copy(self, doublyLinkedList):
        
        self.newObject = DoublyLinkedList()
        cont = 0
        aux = self.head
        tam =  int(doublyLinkedList.__len__())
        
        while(cont < tam):
            item = doublyLinkedList.__getitem__(cont)
            aux.after = Node(item,aux)
            self.newObject.append(aux.after)
            aux = aux.after
            cont = cont + 1
        self.tail = aux
            
        return self.newObject
        
    def extend(self, iterable):
        #FALTANDO SE FOR UM DICIONARIO
        cont = 0
        tam = len(iterable)
        
        if(type(iterable) == str):
            string = ""
            while(cont < tam):
                char = iterable[cont]
                string += char
                cont += 1
            self.append(string)
            
            
        else:
            while(cont < tam):
                item = iterable[cont]
                self.append(item)
                cont += 1
                
    def switch(self, index1, index2):
        
        if(index1 > (self.__len__()-1) or index2 > (self.__len__()-1)):
            raise IndexError("Index out of range")

        else:
            cont = 0
            aux = self.head.after
            self.secondValue = self.firstValue = 0
            
            while(cont != index1):
                aux = aux.after
               
                cont += 1
                
            self.firstValue = aux.item
            print("primeiro", self.firstValue)
            cont = 0
            aux = self.head.after
            
            while(cont != index2):
                aux = aux.after
                cont += 1
           
            self.secondValue = aux.item
            self.__setitem__(index1, self.secondValue)
            self.__setitem__(index2, self.firstValue)
            
    def __contains__(self, item):
        
        aux = self.head.after
        found = False
        while(found == False and aux.after != None):
            if(aux.item == item):
                found = True
                return True
            aux = aux.after
        return False
                
    def __getitem__(self, index):
        
        if(self.isEmpty()):
            print("List is empty")
            
        elif(index > self.__len__()):
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
        
        if(index > self.__len__()):
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
