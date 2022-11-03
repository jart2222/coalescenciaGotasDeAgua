from modeloPropuesta.ListaAutomatas import ListaAutomatas


class ListaAutomatasUnion(ListaAutomatas):

    def __init__(self,listaAutomataUno,listaAutomataDos):
        super().__init__()
        self.listaAutomataUno=listaAutomataUno;
        self.listaAutomataDos=listaAutomataDos;

    def unirListas(self):# une la lista de automatas de cada objeto en uno general


        for automata in self.listaAutomataUno.automatasContenidos:
            self.anadirAutomata(automata)


        for automataC in self.listaAutomataDos.automatasContenidos:
            self.anadirAutomata(automataC)






        self.consevarMovimiento()

    def consevarMovimiento(self):#categoriza que movimiento se conserva;
        automata= self.listaAutomataUno.automatasContenidos[0];
        for automata2 in self.automatasContenidos:
            automata2.asignacionMovimientoAutomata(automata.movimientoX,automata.movimientoY)
