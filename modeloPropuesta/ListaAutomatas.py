from modeloPropuesta.Automata import Automata

class ListaAutomatas:
    def __init__(self):
        self.automatasContenidos = [];
        self.tamano = len(self.automatasContenidos);


    def anadirAutomata(self,automataPropuesta):     #añade el automata pasado por argumento
        if len(self.automatasContenidos)==0:           # Si la lista esta vacia lo añade
            self.automatasContenidos.append(automataPropuesta);
        else:
            if(self.automataEsConenido()!= False):#Si el automata no esta contenido lo añade
                self.automatasContenidos.append(automataPropuesta);

    def automataEsConenido(self, automataPropuesta): #busca si el automata ya existe en la lista
        if automataPropuesta  in self.automatasContenidos:
            return True;
    def movimientoAsignacion(self,movimientoX,movimientoY):     #Le asigna el mismo movimiento a todos los automatas contenidos
        for automataPropuesta in self.automatasContenidos:
            automataPropuesta.asignacionMovimientoAutomata(movimientoX,movimientoY)

    def mostarUbicacionAutomatasEnListas(self): #muestra la ubicacion de los automatas contenidos
        print("====metodo mostar list Todos los automatas")
        for automataPropuesta in self.automatasContenidos:
            print(f'({automataPropuesta.ubicacionX},{automataPropuesta.ubicacionY})')

    def moverLista(self): #cambia la ubicacion de cada Automata
        for automataPropuesta in self.automatasContenidos:
            automataPropuesta.moverAutomata();

    def __eq__(self, listaAutomatas):
        return self.automatasContenidos==listaAutomatas



