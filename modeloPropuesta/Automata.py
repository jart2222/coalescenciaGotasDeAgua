class Automata:

    def __init__(self, ubicacionX, ubicacionY,dimension):
        self.estado=0;
        self.ubicacionX=ubicacionX;
        self.ubicacionY=ubicacionY;
        self.dimension=dimension;

    def asignacionMovimientoAutomata(self,movimientoX,movimientoY):#Le asigna el movimiento a cada automata
        self.movimientoX=movimientoX;
        self.movimientoY=movimientoY;

    def moverAutomata(self): #Cambia de ubicacion del automata ocupando el movimiento
        if((self.ubicacionY+self.movimientoY)<0): # si la suma de la ubicacion y movimiento es cero se mueve al otro extremo de la matriz
            self.ubicacionY=self.dimension-1;

        elif ((self.ubicacionY + self.movimientoY) >= self.dimension):# si cumple se mueve al otro extremo de la matriz
            self.ubicacionY = 0;

        else:
            self.ubicacionY = self.ubicacionY + self.movimientoY


        if ((self.ubicacionX+self.movimientoX) < 0):# si cumple se mueve al otro extremo de la matriz
            self.ubicacionX = self.dimension-1;

        elif ((self.ubicacionX+self.movimientoX) >= self.dimension):# si cumple se mueve al otro extremo de la matriz
            self.ubicacionX = 0;

        else:
            self.ubicacionX = self.ubicacionX + self.movimientoX

    def __eq__(self, automataPropuesta):
        return (self.ubicacionX==automataPropuesta.ubicacionX and self.ubicacionY==automataPropuesta.ubicacionY)