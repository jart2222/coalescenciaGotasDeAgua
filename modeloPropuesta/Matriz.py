import numpy as np
import random

from matplotlib import pyplot as plt

from modeloPropuesta.Automata import *
from modeloPropuesta.ListaAutomatas import ListaAutomatas
from modeloPropuesta.ListaAutomatasUnion import ListaAutomatasUnion


class Matriz:


    def __init__(self, dim):
        self.dim = dim
        self.a = np.zeros((self.dim, self.dim));
        self.listaDeAutomatasContenidos=[];
        self.listaDeAutomatasContenidosCopia=[];
        self.listaFormatosGrafica = ["o", "d", "v", "s"]
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
                if (self.a[automata.ubicacionX + i, automata.ubicacionY + j] == 1):
                    automata=Automata(automata.ubicacionX + i, automata.ubicacionY + j, self.dim)
                    for automata2 in self.listaDeAutomatasContenidosCopia:
                        if(automata2.__eq__(automata)):
                            listaAutomatas.anadirAutomata(automata2)
                            self.listaDeAutomatasContenidosCopia.remove(automata2)
        if(tamanoOriginal <len(listaAutomatas.automatasContenidos)): #Si agregaron elementos a la lista repite el metodo para las nuevas celdas
            for automataEnLista in listaAutomatas.automatasContenidos:
                self.dectarVecinoAutomata(listaAutomatas, automataEnLista)

    def darMovimientoALista(self):
        self.numeros=[1,0,1,0]
        contador=0
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            listaAutomatas.movimientoAsignacion(self.numeros[contador],0)
            contador=contador+1
            #listaAutomatas.movimientoAsignacion(random.randint(-1, 1),random.randint(-1, 1))

    def nuevaMatriz(self):
        self.a = np.zeros((self.dim, self.dim));
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            for automata in listaAutomatas.automatasContenidos:
                self.poblarMatriz(automata.ubicacionX, automata.ubicacionY)


    def detectarUniones(self):
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            for automata in listaAutomatas.automatasContenidos:
                for i in np.array(self.arregloEnteros1):
                    for j in np.array(self.arregloEnteros2):
                        if (self.a[automata.ubicacionX + i, automata.ubicacionY + j] == 1):
                            automatadetectado=Automata(automata.ubicacionX + i,automata.ubicacionY + j,self.dim)
                            if (listaAutomatas.__eq__(self.automataContenidoLista(automatadetectado))): # Si el vecino ya pertence a la lista lo ignora
                                continue;
                            else:
                                listaAutomatasUnion=ListaAutomatasUnion(listaAutomatas, self.automataContenidoLista(automatadetectado));
                                listaAutomatasUnion.unirListas()
                                listaAutomatasUnion.mostarUbicacionAutomatasEnListas()
        pass

    def automataContenidoLista(self, automata):
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            if automata in listaAutomatas.automatasContenidos:
                return listaAutomatas;



    def obtenerImagenMatriz(self):
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []
        fig, ax = plt.subplots()
        ax.axis([0, self.dim, 0, self.dim])

        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            for automata in listaAutomatas.automatasContenidos:
                self.listaCoordenadasX.append(automata.ubicacionX)
                self.listaCoordenadasY.append(automata.ubicacionY)
        ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[1])
        plt.savefig(f"fotosEtapa\\Etapa_{self.contadorImagen}.png")
        plt.close()
        self.contadorImagen=self.contadorImagen+1;

    def moverListasContenidas(self):
        for listaAutomatas in self.listaDeListaDeAutomatasContenidos:
            tamanoLista=len(listaAutomatas.automatasContenidos)
            contadorEtapa=self.contadorImagen

            if (tamanoLista==1):
                listaAutomatas.moverLista()
                continue

            if ((tamanoLista%2==0 or  contadorEtapa%4==0 ) and (contadorEtapa%2==0)):
                if(contadorEtapa==2 and tamanoLista==4):
                    continue
                listaAutomatas.moverLista()
                continue

            if ((tamanoLista%3==0 or tamanoLista%6==0) and (contadorEtapa%3==0)):
                if (contadorEtapa == 3 and tamanoLista==6):
                    continue
                listaAutomatas.moverLista()
                continue;

            if ((tamanoLista%5==0) and (contadorEtapa%5==0)):
                listaAutomatas.moverLista()
                continue;

            if ((tamanoLista%7==0) and (contadorEtapa%7==0)):
                listaAutomatas.moverLista()
                continue;

            if(tamanoLista>7):
                #agregar funcion para eliminar automata y agregar nuevos automatas
                continue;








