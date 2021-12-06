from ListMethods import ListedLinkList
from Sistematizar import Sistematizar
from Stack import LinkedListStack
from MockUpsV2 import MockupData 
from Notificaciones import Notifications
from ApiladorAnimales import *
from ControlPedidos import OrderControl
from Queue import ListLinkQueue
import time


def main():
    
# Datos vacas
  node = ListedLinkList(None)
  vacas = ListedLinkList(None)
  vacasFinal = ListedLinkList(None)
  vacasFinalMatrix = ListedLinkList(None)
  vacasSize = 0
  vacasSizeMatrix = 0

  
# Datos Notificaciones
  notification = Notifications()
  tamañoNotificaciones = 0

# Datos pedidos
  lista_pedidos = ListLinkQueue()
  pedidos_guardados = OrderControl()
  pedido = ListLinkQueue()
  pedidosSize = 0  
  
# Animales Apilados
  camionesVacas = CamionesVacas()
  nodeStack = LinkedListStack(None)
  pedidosVacas = LinkedListStack(None)
  Caux = 0
  Ccont = 0
    
  
  opM = 0
  print("Bienevido al sistema farm data")
  print(" ")
  while opM != 5:
      print("")
      
      print("1) List")
      print("2) Stacks")
      print("3) Queue")
      print("4) Generador de mokups")

      opM = int(input())

      if opM == 1:
          op = 0  
          print("lISTAS")
          while op != 7:
            print(" ")
            print("Escoga alguna opción")
            
            print("1) Imprimir lista")
            print("2) Limpiar Lista")
            print("3) Encontrar un elemento")
            print("4) Insertar un elemento")
            print("5) Remover un elemento")
            print("6) Encontra un k elemento")
            print("8) Insertar elemento al final")
            print("7) Salir")
            print("9) Lista de vacas")
            print("10) Subir")
            print("11) Cargar la lista")
            print("12) Notificaciones")
            print("13) Ver Notificaciones")
            
        
        
            op = int(input())
            if op == 1:
                node.printList()
            elif op == 2:
                node = ListedLinkList(None)
            elif op == 3:
                print("Digite la posición del dato a encontrar")
                posicion = int(input())
                
                print("Digite el dato a encontrar")
                dato = input()
                node.FindKth(posicion).printList()
                node.FindKth(posicion).FindElement(dato)
            elif op == 4:
                print("Digite la posición del dato a insertar")
                posicion = int(input())
                nodeaxu = ListedLinkList(None)
                nodoFinal = ListedLinkList(None) 
                print("Digite el codigo de la vaca")
                codigo = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(codigo, nodoFinal)
                print("1 si es lechera, 0 si no")
                lechera = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(lechera, nodoFinal)
                print("Digite el peso de la vaca")
                peso = input()
                nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(peso, nodoFinal)

                nodeaxu = node.InsertElement(posicion,nodeaxu,tamañoNotificaciones)
                if posicion <= vacasSize:
                    vacasSize += 1
                
                
            elif op == 5:
                print("Digite la posicion del dato a eliminar")
                position = int(input())
                node = node.RemoveElement(position)
                if vacasSize > 0:
                    vacasSize -= 1
                
            elif op == 6:
                print("Digite la posición del elemento a encontrar")
                k = int(input())
                node.FindKth(k).printList()
                
            elif op == 7:
                break
            
            elif op == 8:
                print("Digite el dato")
                dato = input()
                node,vacasFinal = node.InsertElementFinal(dato,vacasFinal)
                vacasSize += 1
            elif op == 9:
                vacasSizeMatrix += 1
                if node != None:
                    print(node.printList())
                else:
                    print("Lista vacas vacía")
                    
                    
            elif op == 10:
                print("Subir")
                Sistematizar.subir(vacas,0,vacasSize)
            elif op == 11:
                print("Cargar")
                node,tamañoNotificaciones = Sistematizar.cargarLinkList(0)
                vacasSizeMatrix = tamañoNotificaciones
            elif op == 12:
                print("vacasSize ",tamañoNotificaciones)
                
                if node.data != None:
                    ini = time.time()
                    notification = notification.generateNotifications(node,tamañoNotificaciones)    # Tp + 4Ta + n( 21Tc + 25Ta + 9Tr) + Tr
                    print("Notificaciones generadas")                                               # Tp
                    end = time.time() - ini                                                
                    # --> 2Tp + 4Ta + n( 21Tc + 25Ta + 9Tr) + Tr
                    # Constantes -> A + n * B
                    # Complejidad = O(N)
                    print("Tiempo: ",end, "Ms " )
                    a = input()                
                else:
                    print("Lista vacía")
                              
            elif op == 13:
                    notification.showNotifications()
                
            elif op == 14:
                vacas.printList()
            
            else:
                print("Opción invalida")
        
            a = input("Presione ENTER")
            
      elif opM == 2:
          print("Stacks")
          op = 0  
          while op != 7:
            print(" ")
            print("Escoga alguna opción")
            
            print("1) Imprimir Stack")
            print("2) Limpiar Stack")
            print("3) Push")
            print("4) Pop")
            print("5) Peek")
            print("6) Salir")
            print("7) Mover vacas")
            print("8) Subir")

        
        
            op = int(input())
            if op == 1:
                camionesVacas.apilador.printList()
            elif op == 2:
                camionesVacas.apilador = LinkedListStack(None)
            elif op == 3:
                if camionesVacas.apilador != None:
                    nodeaxu = ListedLinkList(None)
                    nodoFinal = ListedLinkList(None) 
                    contenedor = LinkedListStack(None)
                    print("Digite el codigo de la vaca")
                    codigo = input()
                    nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(codigo, nodoFinal)
                    print("1 si es lechera, 0 si no")
                    lechera = input()
                    nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(lechera, nodoFinal)
                    print("Digite el peso de la vaca")
                    peso = input()
                    nodeaxu,nodoFinal = nodeaxu.InsertElementFinal(peso, nodoFinal) 
                    contenedor.Push(nodeaxu)
                    contenedor.next = camionesVacas.apilador.FindKth(Caux)
                    camionesVacas.apilador = camionesVacas.apilador.Push(contenedor)
                
                else:
                    print("Cargue el apilador")

            elif op == 4:                
                if Ccont <= tamañoCamiones:
                    camionesVacas.apilador.FindKth(Caux).printList()
                    camionesVacas.apilador.FindKth(Caux).Pop()
                    Ccont += 1
                else:
                    Ccont = 0
                    Caux += 1
                    
            elif op == 5:
                camionesVacas.apilador.FindKth(Caux).data.printList()
            elif op == 6:
                break
            elif op == 7:
                
                print("Digite el tamaño de los camiones")
                tamañoCamiones = int(input())

                if vacas.data == None:
                    print("Cargando lista de vacas....")
                    node,tamañoNotificaciones = Sistematizar.cargarLinkList(0)
                    elemento = node
                    vacas,vacasFinalMatrix = vacas.InsertElementFinal(elemento,vacasFinalMatrix)
                    node = ListedLinkList(None)
                print("Subiendo vacas en los camiones....")
                
                start = time.time()
                camionesVacas = camionesVacas.PushLists(vacas,tamañoNotificaciones,tamañoCamiones)

                # --> 6Ta + 3Td + n * (14Tc + 8Ta + 2Tr + 2To + 12Td)
                # Constantes -> A + n * B
                # Complejidad = O(N)

                end = time.time() -start
                print(end, "ms ")
                a = input()
                camionesVacas.PopList()
                
                
                
                op = 0
            elif op == 8:
                print("Subir")
                Sistematizar.subirLinkStack(pedidosVacas,1,pedidosSize)
            
            else:
                print("Opción invalida")
                 
      elif opM == 3:
          print("GESTIÓN DE PEDIDOS")
          op = 0  
          while op != 3:
                print(" ")
                print("Escoga alguna opción")
                
                print("1) Crear pedido")
                print("2) Ver lista de pedidos")
                print("3) Control de pedidos")
                print("4) Salir")
                print("5) Subir datos")
                print("6) Cargar datos")
            
            
                op = int(input())
                if op == 1:
                    datos = [input("Código: "),input("Tipo animal: "),input("Cantidad: ")]
                    pedido.enqueue(datos[0])
                    pedido.enqueue(datos[1])
                    pedido.enqueue(datos[2])
                    lista_pedidos.enqueue(datos)
                elif op == 2:
                    lista_pedidos.printQueue()
                    
                elif op == 3:
                    start = time.time()
                    pedidos_guardados.passDays()                            # 2Td + 2Ta + 2To
                    if pedidos_guardados.diasAcum > 0:                      # Tc
                        pedidos_guardados.guardarPedido(lista_pedidos)      # Td + Ta + Tc + Tr + n * (4Tc + 5Td + 22Ta + 3To + 3Tr)
                        lista_pedidos = ListLinkQueue()                     # Ta + 3Td + 3Ta
                        pedidos_guardados.diasAcum = 0                      # Ta
                    end = time.time() -start
                    # --> 6Td + 8Ta + 2To + Tc + n * (4Tc + 5Td + 22Ta + 3To + 3Tr)
                    # Constantes -> A + n * B
                    # Complejidad = O(N)
                    print(end, "ms ")
                        
                elif op == 4:
                    break
                elif op == 5:
                    print("Subir")
                    Sistematizar.cargarLinkQueue(lista_pedidos,1,pedidosSize)
            
                elif op == 6:
                    print("Cargando datos.....")
                    lista_pedidos = Sistematizar.cargarLinkQueue(1)
                    '''start = time.time()
                    node2 = Sistematizar.cargar(0)
                    print(node2.getSize())
                    end = time.time() - start
                    node2.printList()
                    print("Tiempo: ",end)
                    print("end")'''

        
      elif opM == 4:
          op = 0
          while op != 7:
              genData = MockupData()
              print("Creación de mokups data ")
              print("")
              
              print("Escoga alguna opción")
              print("1) Generar mokup de vacas")
              print("2) Generar mokup de pedidos")  
              print("3) Salir")
              op = int(input())
              
              """try:
                  op = int(input())
              except:
                  print("ERROR DE CASTING A NUMERO")
                  op = 0
              """
              if op == 1:
                  print("Digite el tamaño del mokup 'vacas' :")
                  tam = int(input())
                  print("Digite el nombre del archivo")
                  nombre = input()
                  genData.genMvacas(tam,nombre)
                  
              elif op == 2:
                  print("Digite el tamaño del mokup 'pedidos' :")
                  tam = int(input())
                  print("Digite el nombre del archivo")
                  nombre = input()
                  genData.genMpedidos(tam,nombre)
              elif op == 3:
                  break
                  
                  
              else:
                  print("Opción invalida")      
                      
                  
                    
main()