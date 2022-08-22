import random
from matriz.MatrizAutomata import MatrizAutomata
matriz=MatrizAutomata(20);

for _ in range(4):
    matriz.poblarMatriz(random.randint(0,5),random.randint(0,5))

matriz.detectarUbicacionAutomatas()
matriz.formarArregloDeAutomomatas()
matriz.dibujarArreglosDeAutomatas()
for _ in range(3):
    matriz.moverArreglo()
    matriz.actualizarMatriz()
    matriz.detectarUbicacionAutomatas()
    matriz.formarArregloDeAutomomatas()
    matriz.dibujarArreglosDeAutomatas()



