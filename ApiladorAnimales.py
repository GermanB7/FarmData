from Stack import LinkedListStack
from ListMethods import ListedLinkList


class CamionesVacas():
    
    apilador = LinkedListStack(None)
    numeroCamiones = 0
    def __init_(self):
        self.numeroCamiones = 0                         # Ta + Td
        self.apilador = LinkedListStack(None)           # Td + Ta + 2Ta
                                                        # ---> 4Ta + 2Td

        
    def PushLists(self, vacas,vacasSizeMatrix, tamañoCamiones):
        cont = 1                                                        # Ta
        instancia = self                                                # Ta 
        camion = LinkedListStack(None)                                  # 4Ta + 3Td 

        for i in range(vacasSizeMatrix-1):                              # n * Tc
            if vacas.data.FindKth(1) == "1":                            # Tc + (4Ta + (n+4)Tc + 2Tr) == n-1 * ( 6Tc + 4Ta + 2Tr)
                if cont <= tamañoCamiones:                              # n * Tc
                    
                    camion = camion.Push(vacas.FindKth(0))              # n * (2Tc + 6Td + 9Ta + Tr + (2Ta + Tc + Tr))
                    cont += 1                                           # n * (Ta + To)
                else:                                                   # n * Tc

                    instancia.apilador = self.apilador.Push(camion)     # n * (Ta + 2Tc + 6Td + 9Ta + Tr)
                    cont = 0                                            # n * Ta
                    camion = LinkedListStack(None)                      # n * (4Ta + 3Td)
                    instancia.numeroCamiones += 1                       # n * (Ta + To)
            vacas = vacas.next                                          # n * (Ta)
   
        return self                                                     # Tr

        # == 6Ta + 3Td + n * (14Tc + 8Ta + 2Tr + 2To + 12Td)
        
        
    def PopList(self):
        
        for i in range(self.numeroCamiones):
            print("Camion numero ",i)
            self.apilador.FindKth(i).printList()
        
        
        
    
    
    
    























