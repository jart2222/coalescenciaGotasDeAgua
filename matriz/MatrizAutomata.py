from typing import List

import numpy as np
import random
import matplotlib.pyplot as plt
from RepositorioAutomatas.ListaDeAutomatas import ListaDeAutomatas
from RepositorioAutomatas.modelo.Automata import Automata;


class MatrizAutomata:
    listaDeTodosLosAutomatas: List[Automata]

    def __init__(self, dim):
        self.dim = dim
        self.a = np.zeros((self.dim, self.dim))
        self.arregloEnteros1 = [*range(-1, 1 + 1, 1)]
        self.arregloEnteros2 = [*range(-1, 1 + 1, 1)]
        self.listaDeTodosLosAutomatas = []
        self.copiaListaDeTodosLosAutomatas = []
        self.ubicacionAutomata=[];
        self.listaDeListaDeAutomatas=[];

    def poblarMatriz(self, numeroFila,numeroColumna):
        self.a[numeroFila, numeroColumna] = 1

    def mostarListTodosLosAutomatas(self):
        print("====metodo mostar list Todos los automatas")
        for automata in self.copiaListaDeTodosLosAutomatas:
            print(f'({automata.ubicacionX},{automata.ubicacionY})')

    def eliminarElementoLTAutomatas(self, automata):
        for elemento in self.copiaListaDeTodosLosAutomatas:
            if (elemento.__eq__(automata)):
                self.copiaListaDeTodosLosAutomatas.remove(elemento)

    def detectarUbicacionAutomatas(self):
        self.ubicacionAutomata = np.where(self.a == 1)

        for j in range(len(self.ubicacionAutomata[0])):
            self.listaDeTodosLosAutomatas.append(Automata(self.ubicacionAutomata[0][j], self.ubicacionAutomata[1][j]))
            self.copiaListaDeTodosLosAutomatas.append(Automata(self.ubicacionAutomata[0][j], self.ubicacionAutomata[1][j]))

    def formarArregloDeAutomomatas(self):
        for elementoDeListaTodosLosAutomatas in self.listaDeTodosLosAutomatas:
            for automataCopia in self.copiaListaDeTodosLosAutomatas:
                if(elementoDeListaTodosLosAutomatas.__eq__(automataCopia)):
                    listaDeAutomatas = ListaDeAutomatas()
                    self.dectarVecinoAutomata(listaDeAutomatas, elementoDeListaTodosLosAutomatas)
                    self.listaDeListaDeAutomatas.append(listaDeAutomatas);
                    listaDeAutomatas.contarAutomatas()
                else:
                    continue;



    def dectarVecinoAutomata(self, listaDeAutomatas, automata):

        for i in self.arregloEnteros1:
            for j in self.arregloEnteros2:
                if (i == 0 and j == 0):
                    listaDeAutomatas.checharExistenciaAutomata(automata)
                    self.eliminarElementoLTAutomatas(automata)

                if (self.a[automata.ubicacionX + i, automata.ubicacionY + j] == 1):
                    automota2 = Automata(automata.ubicacionX + i, automata.ubicacionY + j)
                    listaDeAutomatas.checharExistenciaAutomata(automota2)
                    self.eliminarElementoLTAutomatas(automota2)

        self.dectectarVecinosAutomatasAñadidos(listaDeAutomatas)


    def dectectarVecinosAutomatasAñadidos(self, listaDeAutomatas):
        self.permitirCiclo = False
        for elemento in listaDeAutomatas.automatasArreglo:
            for i in self.arregloEnteros1:
                for j in self.arregloEnteros2:
                    if (i == 0 and j == 0):
                        listaDeAutomatas.checharExistenciaAutomata(elemento)
                        self.eliminarElementoLTAutomatas(elemento)
                        continue

                    if (self.a[elemento.ubicacionX + i, elemento.ubicacionY + j] == 1):
                        automota2 = Automata(elemento.ubicacionX + i, elemento.ubicacionY + j)
                        listaDeAutomatas.checharExistenciaAutomata(automota2)
                        self.eliminarElementoLTAutomatas(automota2)



    def mostrarMatriz(self):
        print(self.a)

    def dibujarArreglosDeAutomatas(self):
        print("""====== metodo dibujarArreglosDeAutomatas  \n""")
        print("Arreglo de automatas detectados: ", len(self.listaDeListaDeAutomatas))
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []
        for listaAutomata in self.listaDeListaDeAutomatas:
            for automata in listaAutomata.regresarLista():
                self.listaCoordenadasX.append(automata.ubicacionX)
                self.listaCoordenadasY.append(automata.ubicacionY)


        fig, ax = plt.subplots()
        ax.axis([-1, 10, -1, 10])
        ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, "or")
        plt.show()

