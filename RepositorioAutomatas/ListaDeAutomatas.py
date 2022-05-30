from RepositorioAutomatas.modelo.Automata import Automata
import matplotlib.pyplot as plt
class ListaDeAutomatas:

    def __init__(self):
        self.automatasArreglo=[];
        self.automatasTotales=0;
        self.validoAñadir=True;

    def mostrarListAutomata(self):
        for automata in self.automatasArreglo:
            print(f"({automata.ubicacionX}, {automata.ubicacionY})")

    def checharExistenciaAutomata(self, automata2):
        self.validoAñadir=True;
        if len(self.automatasArreglo)==0:
            self.añadirLista(automata2)
        else:
            for automata in self.automatasArreglo:
                if(automata.__eq__(automata2)):
                    self.validoAñadir = False;

            if(self.validoAñadir):
                self.añadirLista(automata2)




    def añadirLista(self, automata):
        self.automatasArreglo.append(automata)

    def contarAutomatas(self):
        print("""====== metodo contar automatas \n""")
        self.automatasTotales=len(self.automatasArreglo);
        print("Total Automatas en la lista: ",self.automatasTotales);
        self.mostrarListAutomata()
        self.dibujarListaAutomatas()

    def dibujarListaAutomatas(self):
        self.listaCoordenadasX=[]
        self.listaCoordenadasY=[]
        for automata in self.automatasArreglo:
            self.listaCoordenadasX.append(automata.ubicacionX)
            self.listaCoordenadasY.append(automata.ubicacionY)

        fig, ax = plt.subplots()
        ax.axis([-1, 10, -1, 10])
        ax.plot(self.listaCoordenadasX,self.listaCoordenadasY,"or")
        plt.show()
