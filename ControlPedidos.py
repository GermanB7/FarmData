from Queue import *
from Stack import LinkedListStack

class OrderControl:
    def __init__(self):
        self.lista_pedidos = ListLinkQueue()
        self.dias = 0
        self.diasAcum = 0

    def passDays(self):
        self.dias += 1              # Td + Ta + To
        self.diasAcum += 1          # Td + Ta + To
                                    # ---> 2Td + 2Ta + 2To

    def mostrarPedidos(self):
        self.lista_pedidos.printQueue()


    def guardarPedido(self,lista_datos):
        pedido = lista_datos.first                      # Td + Ta
        while pedido.next != None:                      # (n * Tc) + Tc
            self.lista_pedidos.enqueue(pedido.data)     # n * (5Td + 21Ta + 3To + 3Tr + 3Tc)
            pedido = pedido.next                        # n * Ta
        return self                                     # Tr
                                                        # ---> Td + Ta + Tc + Tr + n * (4Tc + 5Td + 22Ta + 3To + 3Tr)

# def main2():
#     # Funcionalidad como tal
#     pedidos = OrderControl()
#     with open("archivo",'r') as txt:
#         while True:
#             linea = txt.readline()
#             if linea == "":
#                 break
#             else:
#                 try:
#                     # Código - Tipo_animal - Cantidad
#                     datos = linea[:-1].strip().split(" ")
#                     pedidos.guardarPedido(datos)
#                 except:
#                     print("No se pudo cargar los datos.")
           
#     pedidos.mostrarPedidos()
