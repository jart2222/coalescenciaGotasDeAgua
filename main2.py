from modeloPropuesta.Matriz import Matriz
import random

matriz=Matriz(20);
matriz.poblarMatriz(2,3)
matriz.poblarMatriz(4,4)
matriz.crearAutomata()
matriz.asignarAutomataALista()
matriz.darMovimientoALista()
matriz.obtenerImagenMatriz()
for _ in range(3):
    matriz.moverListasContenidas()
    matriz.nuevaMatriz()
    matriz.obtenerImagenMatriz()
    matriz.detectarUniones()
