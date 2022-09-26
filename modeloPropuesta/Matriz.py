import numpy as np
import random

from matplotlib import pyplot as plt

from modeloPropuesta.AutomataPropuesta import AutomataPropuesta
from modeloPropuesta.ListaAutomatasPropuesta import ListaAutomatasPropuesta


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
            automataPropuesta= AutomataPropuesta(self.ubicacionAutomata[0][j], self.ubicacionAutomata[1][j],self.dim);         #Crea Automata
            self.listaDeAutomatasContenidos.append(automataPropuesta); #A la lista de autamatas creada la añade a una lista
            self.listaDeAutomatasContenidosCopia.append(automataPropuesta)

    def pintarMatrizConsola(self):     #Imprime la matriz en consola y toda la lista de automatas
        print(self.a)
        print()
        #for listaAutomatasPropuesta in self.listaDeListaDeAutomatasContenidos:
        #    listaAutomatasPropuesta.mostarUbicacionAutomatasEnListas()

    def asignarAutomataALista(self): # por cada automata en la matriz le asigna una lista, y busca si tiene vecinos
        for automataPropuesta in self.listaDeAutomatasContenidos:
            if automataPropuesta in self.listaDeAutomatasContenidosCopia:
                self.listaDeAutomatasContenidosCopia.remove(automataPropuesta)
                listaAutomatasPropuesta = ListaAutomatasPropuesta();  # Crear lista de automatas
                listaAutomatasPropuesta.anadirAutomata(automataPropuesta);  # Al autamata creado lo añade a una lista
                self.dectarVecinoAutomata(listaAutomatasPropuesta,automataPropuesta)
                self.listaDeListaDeAutomatasContenidos.append(listaAutomatasPropuesta)#Agrega la lista de Automatas  A una lista genenal


    def dectarVecinoAutomata(self, listaAutomatasPropuesta, automataPropuesta): # busca vecinos en la matriz
        tamanoOriginal=len(listaAutomatasPropuesta.automatasContenidos)
        for i in np.array(self.arregloEnteros1):
            for j in np.array(self.arregloEnteros2):
                if (self.a[automataPropuesta.ubicacionX + i, automataPropuesta.ubicacionY + j] == 1):
                    automata=AutomataPropuesta(automataPropuesta.ubicacionX + i, automataPropuesta.ubicacionY + j,self.dim)
                    for automataPropuesta2 in self.listaDeAutomatasContenidosCopia:
                        if(automataPropuesta2.__eq__(automata)):
                            listaAutomatasPropuesta.anadirAutomata(automataPropuesta2)
                            self.listaDeAutomatasContenidosCopia.remove(automataPropuesta2)
        if(tamanoOriginal <len(listaAutomatasPropuesta.automatasContenidos)):
            for AutomataPropuestaEnLista in listaAutomatasPropuesta.automatasContenidos:
                self.dectarVecinoAutomata(listaAutomatasPropuesta, AutomataPropuestaEnLista)

    def darMovimientoALista(self):
        for listaAutomatasPropuesta in self.listaDeListaDeAutomatasContenidos:
            listaAutomatasPropuesta.movimientoAsignacion(random.randint(-1, 1),random.randint(-1, 1))

    def moverListasContenidas(self):
        for listaAutomatasPropuesta in self.listaDeListaDeAutomatasContenidos:
            tamanoLista=len(listaAutomatasPropuesta.automatasContenidos)
            contadorEtapa=self.contadorImagen

            if (tamanoLista==1):
                listaAutomatasPropuesta.moverLista()
                continue

            if ((tamanoLista%2==0) and (contadorEtapa%2==0)):
                listaAutomatasPropuesta.moverLista()
                continue
            if ((tamanoLista%3==0) and (contadorEtapa%3==0)):
                listaAutomatasPropuesta.moverLista()
                continue;

    def nuevaMatriz(self):
        self.a = np.zeros((self.dim, self.dim));
        for listaAutomatasPropuesta in self.listaDeListaDeAutomatasContenidos:
            for automataPropuesta in listaAutomatasPropuesta.automatasContenidos:
                self.poblarMatriz(automataPropuesta.ubicacionX, automataPropuesta.ubicacionY)

    def obtenerImagenMatriz(self):
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []
        fig, ax = plt.subplots()
        ax.axis([0, self.dim, 0, self.dim])

        for listaAutomatasPropuesta in self.listaDeListaDeAutomatasContenidos:
            for automataPropuesta in listaAutomatasPropuesta.automatasContenidos:
                self.listaCoordenadasX.append(automataPropuesta.ubicacionX)
                self.listaCoordenadasY.append(automataPropuesta.ubicacionY)
        ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[1])
        plt.savefig(f"fotosEtapa\\Etapa_{self.contadorImagen}.png")
        plt.close()
        self.contadorImagen=self.contadorImagen+1;






