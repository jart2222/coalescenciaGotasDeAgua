import random
from matriz.MatrizAutomata import MatrizAutomata
matriz=MatrizAutomata(15);

for _ in range(10):
    matriz.poblarMatriz(random.randint(0,10),random.randint(0,10))

matriz.detectarUbicacionAutomatas()
matriz.formarArregloDeAutomomatas()
matriz.dibujarArreglosDeAutomatas()
for _ in range(3):
    matriz.moverArreglo()
    matriz.actualizarMatriz()
    matriz.detectarUbicacionAutomatas()
    matriz.formarArregloDeAutomomatas()
    matriz.dibujarArreglosDeAutomatas()



