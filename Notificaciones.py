from ListMethods import ListedLinkList

class Notifications():
    def __init__(self):
        self.days = 0                                           # Ta
        self.notificaciones = ListedLinkList(None)              # 2Ta
        self.numberNotificacion = 0                             # Ta
        self.NotificacioFinal = None                            # Ta
        # O(1)                                                  # ----> 5Ta
        
    def passDays(self):
        self.days += 1
        # O(1)
        
    def generateNotifications(self,vacas,vacasSizeMatrix):
        print("self.days: ",self.days)                          # Tp
        dayActual = self.days                                   # Ta
        nodeFinal = ListedLinkList(None)                        # 2Ta
        nodo = vacas                                            # Ta
        for i in range(vacasSizeMatrix):                        # n*Tc
            node = ListedLinkList(None)                         # n*2Ta
            if nodo.next != None:                               # n*Tc    
                if nodo.data.FindKth(1) == "1":                 # n(n) = (4Ta + (n+4)Tc + 2Tr) --> n(1) == n*(4Ta + 5Tc + 2Tr)
                    node,nodeFinal = node.InsertElementFinal(nodo.data.FindKth(0),nodeFinal) # 4Ta + 2Tc + Tr +  (2Ta + Tc + Tr) == n*(6Ta + 3Tc + 2Tr)
                    node,nodeFinal = node.InsertElementFinal("Vaca en gestacion, días para parto!: "+str(dayActual + int(nodo.data.FindKth(2))),nodeFinal) # 4Ta + 2Tc + Tr + (4Ta + (n+4)Tc + 2Tr) == n*(8Ta + 8Tc + 3Tr)
                    self.notificaciones,self.NotificacioFinal = self.notificaciones.InsertElementFinal(node,self.NotificacioFinal)  # n*(4Ta + 2Tc + Tr)
                nodo = nodo.next                                # n*Ta
            else:                                               # n*Tc
                return self                                     # n*Tr
        return self                                             # Tr
        
        # = Tp + 4Ta + n( 21Tc + 25Ta + 9Tr) + Tr
        # = Constantes -> A + n * B
        #O(N) O(1) O(1) O(1)
        #O(N)   
    
    def showNotifications(self):
        self.notificaciones.printList()
        
        
        
                
        
        
    
    
    
    