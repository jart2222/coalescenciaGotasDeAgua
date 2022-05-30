from RepositorioAutomatas.modelo.Automata import Automata
from RepositorioAutomatas.ListaDeAutomatas import ListaDeAutomatas
from matriz.MatrizAutomata import MatrizAutomata
x1=Automata(1,0);
x2=Automata(0,1);
x3=Automata(2,1);
x4=Automata(1,2)
x5=Automata(2,4)
x6=Automata(3,5)
x7=Automata(4,4)
x8=Automata(5,3)
x9=Automata(8,3)
x10=Automata(8,4)
x11=Automata(7,5)
x12=Automata(7,4)
x13=Automata(9,9)
x14=Automata(9,8)
matriz=MatrizAutomata(12);
matriz.poblarMatriz(x1)\
    .poblarMatriz(x2)\
    .poblarMatriz(x3)\
    .poblarMatriz(x4)\
    .poblarMatriz(x5)\
    .poblarMatriz(x6)\
    .poblarMatriz(x7)\
    .poblarMatriz(x8)\
    .poblarMatriz(x9)\
    .poblarMatriz(x10)\
    .poblarMatriz(x11)\
    .poblarMatriz(x12)\
    .poblarMatriz(x13)\
    .poblarMatriz(x14)

matriz.mostrarMatriz()
matriz.detectarUbicacionAutomatas()
matriz.formarArregloDeAutomomatas()
