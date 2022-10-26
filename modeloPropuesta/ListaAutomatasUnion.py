from modeloPropuesta.ListaAutomatas import ListaAutomatas


class ListaAutomatasUnion(ListaAutomatas):

    def __init__(self,listaAutomataUno,listaAutomataDos):
        super().__init__()
        self.listaAutomataUno=listaAutomataUno;
        self.listaAutomataDos=listaAutomataDos;

    def unirListas(self):# une la lista de automatas de cada objeto en uno general
        self.automatasContenidos=self.listaAutomataUno.automatasContenidos+self.listaAutomataDos.automatasContenidos;
        self.consevarMovimiento()

    def consevarMovimiento(self):#categoriza que movimiento se conserva;
        if (len(self.listaAutomataUno.automatasContenidos)== len(self.listaAutomataDos.automatasContenidos)):
            for automata in self.listaAutomataUno.automatasContenidos:
                self.movimientoAsignacion(automata.movimientoX,automata.movimientoY);
                break;
        else:
            for automata in self.listaAutomataDos.automatasContenidos:
                self.movimientoAsignacion(automata.movimientoX,automata.movimientoY);
                break;

