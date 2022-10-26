from modeloPropuesta.Matriz import Matriz
import random
matriz=Matriz(20);

for _ in range(5):
    matriz.poblarMatriz(random.randint(0,18),random.randint(0,18))

matriz.crearAutomata()
matriz.asignarAutomataALista()
matriz.darMovimientoALista()
matriz.obtenerImagenMatriz()
for _ in range(10):
    matriz.moverListasContenidas()
    matriz.nuevaMatriz()
    matriz.obtenerImagenMatriz()
