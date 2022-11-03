from modeloPropuesta.Matriz import Matriz
import random
import os
import cv2

from servicios.Imagen import Imagen
from servicios.Video import Video

matriz=Matriz(30);
etapas=100
ruta = os.path.abspath(os.getcwd())+"\\"
video=Video(ruta)
for _ in range(13):
    matriz.poblarMatriz(random.randint(0, 29), random.randint(0, 29))

matriz.crearAutomata()
matriz.asignarAutomataALista()
matriz.darMovimientoALista()
imagen=Imagen(matriz)
imagen.obtenerImagenMatriz()
video.anadirImagenesVideo(imagen)

for _ in range(etapas):
    matriz.detectarUniones()
    matriz.moverListasContenidas()
    imagen = Imagen(matriz)
    imagen.obtenerImagenMatriz()
    video.anadirImagenesVideo(imagen)
    matriz.nuevaMatriz()

video.crearVideo()
