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

    def __init__(self, *args):
        self.head = Node()
        if(args == 0):
            self.tail = self.head
        else:
            cont = 0
            aux = self.head
            while(cont < len(args)):
                aux.after = Node(args[cont],aux)
                aux = aux.after
                cont += 1
            self.tail = aux

    def isEmpty(self):
        if(self.__len__() == 0):
            return True
        else:
            return False
        
    def __contains__(self, item):
        aux = self.head.after
        found = False
        while(found == False and aux.after != None):
            if(aux.item == item):
                found = True
                return True
            aux = aux.after
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
            raise ValueError("Inexist Item")
        else:
            aux = self.head.after
            while(aux.item != item):
                aux = aux.after
            aux.prev.after = aux.after
            aux.after.prev = aux.prev
            del aux
    
            
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
            
