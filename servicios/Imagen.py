from matplotlib import pyplot as plt

class Imagen:

    def __init__(self, matriz):
        self.matrix= matriz
        self.listaFormatosGrafica = ["o", "d", "v", "s"]
        self.nombreImagen="";





    def obtenerImagenMatriz(self):
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []
        fig, ax = plt.subplots()
        ax.axis([0, self.matrix.dim, 0, self.matrix.dim])

        for listaAutomatas in self.matrix.listaDeListaDeAutomatasContenidos:
            for automata in listaAutomatas.automatasContenidos:
                self.listaCoordenadasX.append(automata.ubicacionX)
                self.listaCoordenadasY.append(automata.ubicacionY)
        ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[0])
        ax.set_title(f" Etapa numero {self.matrix.contadorImagen}")  # Add a title to the axes.
        self.nombreImagen=f"fotosEtapa\\Etapa_{self.matrix.contadorImagen}.png"
        plt.savefig(self.nombreImagen)
        plt.close()
        self.matrix.contadorImagen=self.matrix.contadorImagen+1;