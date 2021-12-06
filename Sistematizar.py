from ListMethods import ListedLinkList
from Queue import ListLinkQueue
from Stack import *

class Sistematizar():
    global lista_archivos
    lista_archivos = ['Mokup Data\\vacas100000.txt','Mokup Data\\pedidos100000.txt']




    def cargarLinkList(arch):
        global lista_archivos
        size = 0
        nodoFinal = ListedLinkList(None)
        numeroDatos = 0
        lista_c = ListedLinkList(None)
        with open(lista_archivos[arch],'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        numeroDatos += 1
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = ListedLinkList(None)
                        nodoFinalVacas = ListedLinkList(None)
                        for d in datos:
                            lista_datos,nodoFinalVacas = lista_datos.InsertElementFinal(d,nodoFinalVacas)

                    except:
                        print("No se pudo cargar los datos.")
                lista_c,nodoFinal = lista_c.InsertElementFinal(lista_datos,nodoFinal)
        return lista_c,numeroDatos
    
    def subirLinkList(lista,arch,size):
        global lista_archivos
        with open(lista_archivos[arch],'w') as txt:
            for i in range(size):
                for j in range(3):
                    txt.write(lista.FindKth(i).FindKth(j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")
        
        
        
        
    def cargarLinkQueue(arch):
        global lista_archivos
        lista_c = ListLinkQueue()
        with open(lista_archivos[arch],'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = ListLinkQueue()
                        for d in datos:
                            lista_datos.enqueue(d)
                    except:
                        print("No se pudo cargar los datos.")
                lista_c.enqueue(lista_datos)
        return lista_c
    
    def subirLinkQueue(lista,arch):
        global lista_archivos
        with open(lista_archivos[arch],'w') as txt:
            for i in range(lista.getSize()):
                for j in range(lista.FindKth(i).getSize()):
                    txt.write(lista.FindKth(i).FindKth(j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")
        
        
        
        
    def cargarLinkStack(arch):
        global lista_archivos
        lista_c = LinkedListStack(None)
        with open(lista_archivos[arch],'r') as txt:
            while True:
                linea = txt.readline()
                if linea == "":
                    break
                else:
                    try:
                        datos = linea[:-1].strip().split(" ")
                        lista_datos = LinkedListStack(None)
                        for d in datos:
                            lista_datos = lista_datos.Push(d)
                    except:
                        print("No se pudo cargar los datos.")
                lista_c = lista_c.Push(lista_datos)
        return lista_c
    
    def subirLinkStack(lista,arch,size):
        global lista_archivos
        with open(lista_archivos[arch],'w') as txt:
            for i in range(size):
                for j in range(2):
                    txt.write(lista.FindKth(size-1-i).FindKth(1-j) + " ")
                txt.write("\n")
        print("Archivo subido correctamente.")
        
        
        
        
