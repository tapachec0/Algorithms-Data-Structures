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
            aux = self.head
            for element in iterable:
                aux.after = Node(element, aux)
                aux = aux.after
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
        
        if(self.__contains__(item) == False):
            raise ValueError("Item not found")
        
        else:
            cont = 0
            tam = self.__len__()
            aux = self.head.after
            while(cont < tam):
                print(self.__len__())
                keepFinding = aux
                if(aux.item == item):
                    if(aux.after == None):
                        aux.prev.after = aux.after
                    else:
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
                
    def copy(self):
        
        self.newObject = DoublyLinkedList()
        cont = 0
        aux = self.head.after
        tam =  int(self.__len__())
        
        while(cont < tam):
            self.newObject.append(aux.item)
            aux = aux.after
            cont += 1
        self.tail = aux
            
        return self.newObject
        
    def extend(self, iterable):
       
        for item in iterable:
            self.append(item)

                
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
            
    def __iter__(self):
        return DoublyLinkedListIterator(self)
            
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
   
    
    
'''def concanate(list1, list2):
    list3 = DoublyLinkedList()
    cont = 0
    while(cont < len(list1)):
        list3.append(list1[cont])
        cont += 1
    cont = 0
    while(cont < len(list2)):
        list3.append(list2[cont])
        cont += 1
    return list3'''
def concanate(list1, list2):
    list1.tail.after = list2.head.after
    list2.head.after.prev = list1.tail
    return list1
    
    
