
class Automata:

    def __init__(self, ubicacionX, ubicacionY):
        self.estado=0;
        self.ubicacionX=ubicacionX;
        self.ubicacionY=ubicacionY;


    def __eq__(self, automata):
        return (self.ubicacionX==automata.ubicacionX and self.ubicacionY==automata.ubicacionY)







