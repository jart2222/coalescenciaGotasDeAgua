from RepositorioAutomatas.modelo.Automata import Automata
from RepositorioAutomatas.ListaDeAutomatas import ListaDeAutomatas
import random
from matriz.MatrizAutomata import MatrizAutomata
matriz=MatrizAutomata(12);

for _ in range(10):
    matriz.poblarMatriz(random.randint(0,10),random.randint(0,10))

matriz.detectarUbicacionAutomatas()
matriz.formarArregloDeAutomomatas()
matriz.dibujarArreglosDeAutomatas();
