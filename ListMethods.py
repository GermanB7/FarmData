class ListedLinkList():
    def __init__(self, data):
        self.data = data            # Fa
        self.next = None            # Fa
                                    # ---> 2Fa
    
    def printList(self):
        if self.data != None:                                           # Fc
            if type(self.data) == str or type(self.data) == int:        # Fc
                print("[",(self.data),end=' ')                          # Fp
            else:                                                       # Fc
                print("[",end=' ')                                      # Fp
                self.data.printList()

            while self.next != None:
                self = self.next
                if type(self.data) == str or type(self.data) == int:
                    print(", "+ self.data, end = ' ')
                else:
                    print(",",end='')
                    self.data.printList()
            
            print(']')
        else:
            print("Lista enlazada vacía")
        #O(N)
                    
    def MakeEmpty(self):
        self.data = None
        self.next = None
        return self
        #O(1)   
    
    def FindElement(self, number):
        cont = 0
        head= self
        while head.next != None:
            if number == head.data:
                print("Dato encontado!, posicion: ", cont)
                return
            else:
                head = head.next
                cont += 1
        if number == head.data:
            print("Dato encontado!, posicion: ", cont)
            return
        else:        
            print("Dato no encontrado")
        #O(N)
    
    def InsertElementFinal(self,data,last):
        head = self                                 # Fa
        if head.data == None:                       # Fc
            self = ListedLinkList(data)             # 2Fa
            return self,self                        # Fr ----- 3Fa + Fc + Fr
        else:                                       # Fc
            node = ListedLinkList(data)             # 2Fa
            last.next = node                        # Fa
            return self,node                        # Fr ----- 4Fa + 2Fc + Fr
        #O(1)
        
        
    def InsertElement(self,position,number,size):
        global cont
        head = self
        cont = 0
        if head.data == None:
            self = ListedLinkList(number)
            return self
    
        if position == 0:
            if head.next == None:
                node = ListedLinkList(number)
                node.next = head
                print("Dato Insertado!")
                self = node
                return self
            else:
                node = ListedLinkList(number)
                node.next = head
                print("Dato Insertado!")
                self = node
                return self
        else:
            if head.next == None:
                print(position," ",size)
                if position == size:
               
                    node = ListedLinkList(number)
                    head.next = node
                    return self
                else:
                    print("Posición invalida first")
                    return self
            else:
                while head.next != None:    
                    cont += 1
                    if position == cont:
                        node = ListedLinkList(number)
                        node.next = head.next
                        head.next = node
                        print("Dato insertado")
                        return self
                    head = head.next
                if position == cont +1:
                    node = ListedLinkList(number)
                    head.next = node
                    print("Dato insertado")
                    return self
                print("Posición invalida last")
                return self
            #O(N)
                          
    def RemoveElement(self,position):
        head = self
        cont = 0
        if position == 0 and self.next == None:
            print("Dato desenlazado")
            self.data = None
            self.next = None
            return self
        elif position == 0:

            head = head.next
            print("Dato desenlazado")
            return head
        else:
            while position != cont+1:
                if head.next != None:
                    head = head.next
                    cont += 1
                        
                else:
                    print("Posición invalida")
                    return self
                    cont += 1
                    
            if head.next != None:
                if head.next.next != None:
                    head.next = head.next.next
                    return self
                else:
                    head.next = None
                    return self
            else:
                print("Posición invalida")
                return self
        #O(N)
                        
    def FindKth(self,position):
        head = self                                     # Fa
        cont = 0                                        # Fa
        if position == 0:                               # Fc
            #print(head.data)
            return head.data                            # Fr ------ n(0) = (2Fa + Fc + Fr)
        else:                                           # Fc
            while head.next != None:                    # (n+1 * Fc)
                cont += 1                               # Fa
                head = head.next                        # Fa
                if position == cont:                    # Fc
                    #print(head.data)
                    return head.data                    # Fr ------ n(n) = (4Fa + (n+4)Fc + 2Fr)
            print("Posición invalida")                  # Fp ------ n(n+1) = (4Fa + (n+4)Fc + 2Fr + Fp)
        #O(N)
        
        
        
    def GiveNext(self,number):
        head = self
        cont = 0
        if number == 0:
            if head.next != None:
                if head.next.next != None:
                    return head.data, head.next
        else:
            if head.next != None:
                if head.next.next != None:
                    return head,head.next
            return  None,None
        #O(1)  
            
    def isEmpty(self):
        if self == None:
            return True
        else:
            return False
        #O(1)
        