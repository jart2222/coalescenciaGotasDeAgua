class MoverAutomata:
    etapa=0;
    def moverElementosArreglo(self,listaDeAutomatas):
        MoverAutomata.etapa=MoverAutomata.etapa+1;
        print("===========================Etapa de ejecucion: ",MoverAutomata.etapa);
        movimientoX = 1
        movimientoY = 1

        for listaAutomata in listaDeAutomatas:
            tamanoArreglo=len(listaAutomata.regresarLista())

            if (tamanoArreglo == 1):
                print("Tamaño Lista ",tamanoArreglo)
                listaAutomata.mostrarListAutomata()
                for automata in listaAutomata.regresarLista():
                    automata.ubicacionX = automata.ubicacionX + movimientoX
                    automata.ubicacionY = automata.ubicacionY + movimientoY



            if (MoverAutomata.etapa==2): ## se ejecuta en etapa=2,4,6
                if (tamanoArreglo%2== 0):
                    print("Tamaño Lista ", tamanoArreglo)
                    listaAutomata.mostrarListAutomata()
                    for automata in listaAutomata.regresarLista():
                        automata.ubicacionX = automata.ubicacionX + movimientoX
                        automata.ubicacionY = automata.ubicacionY + movimientoY
                    print("Nueva ubicacion ")
                    listaAutomata.mostrarListAutomata()

            if (MoverAutomata.etapa == 3 ):
                if (tamanoArreglo%3 ==0):
                    print("Tamaño Lista ", tamanoArreglo)
                    listaAutomata.mostrarListAutomata()
                    for automata in listaAutomata.regresarLista():
                        automata.ubicacionX = automata.ubicacionX + movimientoX
                        automata.ubicacionY = automata.ubicacionY + movimientoY


