from ListMethods import *


class LinkedListStack(ListedLinkList):
    def __init__(self, data):
        self.data = data            # Td + Ta
        self.next = None            # Td + Ta
                                    # --> 2Td + 2Ta
    
    def printStackMatrix(self):
        head = self
        #O(1)
    
    def printStack(self):
        head = self
        if head != None:
            print(head.data,end=' ')
            while head.next != None:
                
                print(head.next.data, end = ' ')
                head = head.next
        else:
            print("Lista enlazada vacía")
        #O(N)
            
    def Pop(self):
        head = self
        if head.data != None:
            if head.next != None:
                print(head.data)
                sig = head.next
                self.data = sig.data
                self.next = sig.next
            else:
                print(head.data)
                self.next = None
                self.data = None
        else:
            print("Stack empty")
        #O(1)
        

    def Push(self,data):
        if self.data == None:                   # Tc
            node = LinkedListStack(data)        # Td + Ta + 2Td + 2Ta
            self.next = None                    # Ta
            self.data = data                    # Ta
            return self                         # Tr
        else:                                   # Tc
            node = LinkedListStack(data)        # Td + Ta + 2Td + 2Ta
            node.next = self                    # Ta
            return node                         # Tr
         #O(1)                                  # == 2Tc + 6Td + 9Ta + Tr 

    
    def Peek(self):
        if self.data != None:
            print(self.data)
        else:
            print("Stack empty")
         #O(1)   
    
            
            
    def MakeEmpty(self):
        self.data = None
        self.next = None
        self.size = 0
        return self
        #O(1)
    
    def getSize(self):
        return self.size
        #O(1)
            
            
node = LinkedListStack(None)
op = 0        
"""while op != 7:
    print(" ")
    print("Escoga alguna opción")
    
    print("1) Imprimir lista")
    print("2) Limpiar Lista")
    print("3) Push")
    print("4) Pop")
    print("5) Peek")
    print("6) Salir")

    op = int(input())
    if op == 1:
        if node != None:
            node.printStack()
        else:
            print("Stack Empty")
    elif op == 2:
        node = node.MakeEmpty()
    elif op == 3:
        print("Digite el dato a ingresar")
        dato = input()
        if node != None:
            node = node.Push(dato)
        else:
            node = LinkedListStack(dato)
            
    elif op == 4:
        if node != None:
            node = node.Pop()
        else:
            print("Stack Empty")
    elif op == 5:
        node.Peek()
    elif op == 6:
        break
    else:
        print("Opción invalida")
    
    
"""
        
    
    
    
    
           
            
                
                
                
                    
            
                
                
                
        
        
        
        