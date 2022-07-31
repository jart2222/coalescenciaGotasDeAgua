class MoverAutomata:
    def moverElementosArreglo(self,listaDeAutomatas):
        for listaAutomata in listaDeAutomatas:
            if(len(listaAutomata.regresarLista())==1):
                movimientoX = 1
                movimientoY = 1
                for automata in listaAutomata.regresarLista():
                    automata.ubicacionX = automata.ubicacionX + movimientoX
                    automata.ubicacionY = automata.ubicacionY + movimientoY


