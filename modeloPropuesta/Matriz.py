import numpy as np
import random

from matplotlib import pyplot as plt

from modeloPropuesta.Automata import *
from modeloPropuesta.ListaAutomatas import ListaAutomatas
from modeloPropuesta.ListaAutomatasUnion import ListaAutomatasUnion
from servicios.Imagen import Imagen


class Matriz:


    def __init__(self, dim):
        self.dim = dim
        self.a = np.zeros((self.dim, self.dim));
        self.listaDeListaDeAutomatasContenidosCopia =[];
        self.listaDeAutomatasContenidos=[];
        self.listaDeAutomatasContenidosCopia=[];
        self.listaDeListaDeAutomatasContenidos=[]
        self.arregloEnteros1 = [*range(-1, 2, 1)]
        self.arregloEnteros2 = [*range(-1, 2, 1)]
        self.contadorImagen=0


    def poblarMatriz(self, numeroFila,numeroColumna):
        self.a[numeroFila, numeroColumna] = 1

    def crearAutomata(self):
        self.ubicacionAutomata = np.where(self.a == 1);                                                               #Detecta la ubicacion de los elementos que sean 1
        for j in range(len(self.ubicacionAutomata[0])):                                                               #Por cada elemento 1 en la matriz
            automata= Automata(self.ubicacionAutomata[0][j], self.ubicacionAutomata[1][j], self.dim);         #Crea Automata
            self.listaDeAutomatasContenidos.append(automata); #A la lista de autamatas creada la añade a una lista
            self.listaDeAutomatasContenidosCopia.append(automata)

    def pintarMatrizConsola(self):     #Imprime la matriz en consola y toda la lista de automatas
        print(self.a)
        print()
        #for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
        #    listaAutomatas.mostarUbicacionAutomatasEnListas()

    def asignarAutomataALista(self): # por cada automata en la matriz le asigna una lista, y busca si tiene vecinos
        for automata in self.listaDeAutomatasContenidos:
            if automata in self.listaDeAutomatasContenidosCopia:
                self.listaDeAutomatasContenidosCopia.remove(automata)
                listaAutomatas = ListaAutomatas();  # Crear lista de automatas
                listaAutomatas.anadirAutomata(automata);  # Al autamata creado lo añade a una lista
                self.dectarVecinoAutomata(listaAutomatas,automata)
                self.listaDeListaDeAutomatasContenidos.append(listaAutomatas)#Agrega la lista de Automatas  A una lista genenal


    def dectarVecinoAutomata(self, listaAutomatas, automata): # busca vecinos en la matriz
        tamanoOriginal=len(listaAutomatas.automatasContenidos)
        for i in np.array(self.arregloEnteros1):
            for j in np.array(self.arregloEnteros2):
                listaParametros=self.detectarVecino(automata.ubicacionX + i, automata.ubicacionY + j)
                if listaParametros[0]==True:
                    automata=Automata( listaParametros[1],listaParametros[2], self.dim)
                    for automata2 in self.listaDeAutomatasContenidosCopia:
                        if(automata2.__eq__(automata)):
                            listaAutomatas.anadirAutomata(automata2)
                            self.listaDeAutomatasContenidosCopia.remove(automata2)
        if(tamanoOriginal <len(listaAutomatas.automatasContenidos)): #Si agregaron elementos a la lista repite el metodo para las nuevas celdas
            for automataEnLista in listaAutomatas.automatasContenidos:
                self.dectarVecinoAutomata(listaAutomatas, automataEnLista)

    def darMovimientoALista(self):

        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            listaAutomatas.movimientoAsignacion(random.randint(-1, 1),random.randint(-1, 1))

    def nuevaMatriz(self):
        self.a = np.zeros((self.dim, self.dim));
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            for automata in listaAutomatas.automatasContenidos:
                self.poblarMatriz(automata.ubicacionX, automata.ubicacionY)

    def detectarUniones(self):
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:#Por cada lista
            validoEliminar = True;
            for automata in listaAutomatas.automatasContenidos: #por cada automata en lista
                for i in np.array(self.arregloEnteros1):
                    for j in np.array(self.arregloEnteros2):
                        listaParametros = self.detectarVecino(automata.ubicacionX + i, automata.ubicacionY + j)
                        if listaParametros[0]==True: #si encuentra un vecino de automata
                            automatadetectado=Automata(listaParametros[1] ,listaParametros[2],self.dim)
                            if (listaAutomatas.automataEsConenido(automatadetectado)): # Si el vecino ya pertence a la lista lo ignora
                                continue;
                            else:
                                validoEliminar=self.unionDeDosListas(listaAutomatas,automatadetectado,validoEliminar, automata)


    def detectarVecino(self,buscarX,buscarY):
        if(buscarX<=0):
            buscarX=self.dim-1;
        if (buscarX >= self.dim):
            buscarX = 0;
        if (buscarY <= 0):
            buscarY = self.dim - 1;
        if (buscarY >= self.dim):
            buscarY = 0;

        listaValoresObtenidos=[]
        listaValoresObtenidos.append(self.a[buscarX, buscarY] == 1)
        listaValoresObtenidos.append(buscarX)
        listaValoresObtenidos.append(buscarY)
        return listaValoresObtenidos;

    def unionDeDosListas(self, listaAutomatas,automatadetectado, validoEliminar, automata): # se encarga de unir 2 listas
        listaEvaluarSiEsContenido = self.automataContenidoLista(automatadetectado)
        if(listaEvaluarSiEsContenido is not None):
            listaAutomatasUnion = ListaAutomatasUnion(listaAutomatas,listaEvaluarSiEsContenido);  # crea lista de union de listas
            listaAutomatasUnion.unirListas()  # une la listas
            self.listaDeListaDeAutomatasContenidos.remove(listaEvaluarSiEsContenido)

            if validoEliminar:
                self.listaDeListaDeAutomatasContenidos.remove(listaAutomatas)
            self.listaDeListaDeAutomatasContenidos.append(listaAutomatasUnion)  # agrega a la lista general
            return False
        else:
            print(f"Lista no encontrada \n se analiza el Automata ({automata.movimientoY},{automata.movimientoY})")
            print(f"Y se encontro un vecino en  ({automatadetectado.movimientoX},{automatadetectado.movimientoY})")
    def automataContenidoLista(self, automata): #retorna la lista del automata que se busca
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            if automata in listaAutomatas.automatasContenidos:
                return listaAutomatas;
    #def obtenerImagenMatriz(self):
        #imagen=Imagenes(self)
        #imagen.obtenerImagenMatriz()
        # self.listaCoordenadasX = []
        # self.listaCoordenadasY = []
        # fig, ax = plt.subplots()
        # ax.axis([0, self.dim, 0, self.dim])
        #
        # for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
        #     for automata in listaAutomatas.automatasContenidos:
        #         self.listaCoordenadasX.append(automata.ubicacionX)
        #         self.listaCoordenadasY.append(automata.ubicacionY)
        # ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[0])
        # plt.savefig(f"fotosEtapa\\Etapa_{self.contadorImagen}.png")
        # plt.close()
        # self.contadorImagen=self.contadorImagen+1;

    def moverListasContenidas(self):
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            tamanoLista=len(listaAutomatas.automatasContenidos)

            if (tamanoLista==1): #se ejecutan en cada etapa
                listaAutomatas.moverLista()
                continue

            if tamanoLista%2==0 and self.contadorImagen%2==0:
                listaAutomatas.moverLista()
                continue

            if tamanoLista%3==0 and self.contadorImagen%3==0:
                listaAutomatas.moverLista()
                continue

            if tamanoLista%4==0 and self.contadorImagen%4==0:
                listaAutomatas.moverLista()
                continue

            if tamanoLista%5==0 and self.contadorImagen%5==0:
                listaAutomatas.moverLista()
                continue
            if tamanoLista%6==0 and self.contadorImagen%6==0:
                listaAutomatas.moverLista()
                continue

            if tamanoLista%7==0 and self.contadorImagen%7==0:
                listaAutomatas.moverLista()
                continue
    def pintarListaDeListaDeAutomatas(self):
        print("Lista de automatas")
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            listaAutomatas.mostarUbicacionAutomatasEnListas();


