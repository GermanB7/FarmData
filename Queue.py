from ListMethods import ListedLinkList

class ListLinkQueue(ListedLinkList):
    def __init__(self):
        self.first = None           # Td + Ta
        self.last = None            # Td + Ta
        self.size = 0               # Td + Ta
                                    # ---> 3Td + 3Ta
    
    def printQueue(self):
        if self.first == None:
            print("Cola vacía")
            return 
        head = self.first
        if type(head.data) != ListLinkQueue and type(head.data) != ListedLinkList:
            while head.next != None:
                print(head.data, end = " ")
                head = head.next
            print(head.data)
        else:
            while head.next != None:
                head.data.printQueue()
                head = head.next
            head.data.printQueue()
        #O(N)
            
            
    def enqueue(self,data):
        head = self.first                       # Td + Ta
        tail = self.last                        # Td + Ta
        if head == None:                        # Tc
            node = ListedLinkList(data)         # Td + Ta + 2Ta
            head =  node                        # Ta
            self.first = head                   # Ta
            self.tail = head                    # Ta
            self.size += 1                      # Ta + To
            return self                         # Tr
        elif self.size == 1:                    # Tc
            node = ListedLinkList(data)         # Td + Ta + 2Ta
            head.next = node                    # Ta
            self.last = node                    # Ta
            self.size += 1                      # Ta + To
            return                              # Tr
        elif self.size > 1:                     # Tc
            node = ListedLinkList(data)         # Td + Ta + 2Ta   
            tail.next = node                    # Ta
            self.last = node                    # Ta
            self.size += 1                      # Ta + To
            return                              # Tr
                                                # ---> 5Td + 21Ta + 3To + 3Tr + 3Tc
        #O(1)
        
             
        
    def dequeue(self):
        tail = self.tail
        head = self.first
        if self.size == 0:
           print("Cola vacía")
        elif self.size == 1:
            print(self.first.data)
            self.first = None
            self.last = None
            self.size -= 1
            return head
            
        else:
            print(head.data)
            self.first = head.next
            self.size -= 1
            return head
        #O(1)
            
   
    def MakeEmpty(self):
        self.first = None
        self.tail = None
        #O(1)
        
        
    def Peek(self):
        if self.first != None:
            print(self.first.data)
        else:
            print("Cola vacía")
        #O(1)
        
    def Lower(self):
        if self.tail != None:
            print(self.tail.data)
        else:
            print("Cola vacía")
        #0(1)
    


    