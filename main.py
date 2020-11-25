import os
#encoding: "UTF-16"

#GUARDAR DISPAROS
def guardarDisparos(lista, disparo): #Se pasa la lista de disparos i el disparo del jugador
    letraInicio = int(equivalencias.get(disparo[0]))
    letraFinal = int(disparo[1:])
    letraFinal-=1
    lista[letraInicio][letraFinal] = "D"#Cambiar la posicion de la lista por una D de disparo.

#Cambio de jugador
def cambioJugador(turno):
    limpiarPantalla()#Limpiar
    enter = str
    print("Turno del segundo jugador")
    #Loop que espera al usuario a que pulse enter
    while enter != "" "":
        print("Pulsa enter para continuar!")
        enter = input("> ")
    limpiarPantalla()#Limpiar
    #Devuelve el turno
    if turno == 0:
        return 1
    else:
        return 0


#LIMPIAR PANTALLA
def limpiarPantalla():
    if os.name == "posix": #Para mac y linux
        _ = os.system("clear")
    else:#Para windows
        _ = os.system("cls")

limpiarPantalla()

#INSTRUCCIONES
def instrucciones():
    #Explicar como funciona el juego
    print("\n------Como se juega a este juego------\n")
    print("El juego consiste en undir todos los barcos del contrincante.")
    print("Para ello, debe colocar su propia flota estrategicamente, encontrar y undir la flota contraria.")
    print("Cada jugador tiene su propio tablero y debera posicionar los siguientes barcos en el:")
    print("- 1 barco de 4 posiciones.")
    print("- 2 barcos de 3 posiciones.")
    print("- 3 barcos de 2 posiciones.")
    print("- 4 barcos de 1 posicion.")
    print("La colocacion de los barcos debe ser respetando la franja de las posiciones, es decir, nunca se puede colocar un barco al lado de otro, este debe estar almenos a mas de una posicion de cualquier otro barco del tablero.")
    print("Para colocar cada barco se dira la posicion inicial y la final de este, por ejemplo, si es un barco de 3 casillas: B3 B5, asi este sera colocado en B3, B4 i B5. Si solo es el barco de una casilla solo se introducira una coordenada")
    print("Para disparar a otro jugador se debera insertar una coordenada no repedia anterior y si se golpea a un barco sera 'tocado', si se falla sera 'agua', para que un barco se hunda debe golpearse en todas sus casillas.")
    print("Para ganar se debe hundir todos los barcos del contrincante. Si se hunden todos tus barcos has perdido.\n")

#instrucciones()

equivalencias = {
    'A': '0',
    'B': '1',
    'C': '2',
    'D': '3',
    'E': '4',
    'F': '5',
    'G': '6',
    'H': '7',
    'I': '8',
    'J': '9'
}

def colocarBarco(lista_barcos, casilla):
    letra_inicio, numero_inicio = casilla[0], int(casilla[1])
    lista_barcos[int(equivalencias[letra_inicio])][numero_inicio-1] = 'X'
    

def imprimirTableroBarcos(jugadores, turno):
    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    if turno == 0:
        rival = 1
    else: rival = 0

    # Imprimo mi tablero de barcos con los disparos del rival
    for fila in range(len(jugadores[turno]['barcos'])):
        print(letras[fila], end=" ")
        for columna in range(len(jugadores[turno]['barcos'][fila])):
            ## Barcos que me han disparado
            if jugadores[turno]['barcos'][fila][columna] == 'X' and jugadores[rival]['disparos'][fila][columna] == 'D':
                print('DD', end = " ")
            ## DISPAROS DEL RIVAL EN AGUA
            elif jugadores[turno]['barcos'][fila][columna] != 'X' and jugadores[rival]['disparos'][fila][columna] == 'D':
                print('~~', end = " ")
            # MIS BARCOS
            elif jugadores[turno]['barcos'][fila][columna] == 'X' and jugadores[rival]['disparos'][fila][columna] != 'D':
                print('XX', end = " ")
            # Zonas de agua sin disparos y sin barcos
            else: 
                print('--', end = " ")
        print(end = "\n")

def imprimirTableroDisparos(jugadores, turno):
    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    if turno == 0:
        rival = 1
    else: rival = 0
    # Imprimo el tablero de mis disparos
    for fila in range(len(jugadores[turno]['disparos'])):
        print(letras[fila], end=" ")
        for columna in range(len(jugadores[turno]['disparos'][fila])):
            #  SI HE DADO A UN BARCO
            if jugadores[turno]['disparos'][fila][columna] == 'D' and jugadores[rival]['barcos'][fila][columna] == 'X':
                print('TT', end = " ")
            #  Si he dado a agua
            elif jugadores[turno]['disparos'][fila][columna] == 'D' and jugadores[rival]['barcos'][fila][columna] != 'X':
                print('AG', end = " ")
            # Casillas que no se que hay
            else: 
                print('--', end = " ")
        print(end = "\n")




#ASUMIMOS QUE LA ENTRADA DEL USUARIO VA A SER SIEMPRE ALGO COMO ESTO: "B3 B7", "A5 A1"
#COMPRUEBA SI EL BARCO TIENE UNA ORIENTACION Y TAMAÑO CORRECTOS. DESPUES METE TODAS LAS COORDENADAS QUE OCUPA EL BARCO EN listaPosBarco

def posBarco(casilla, tamano, listaPosBarco):
    if tamano > 1:
        if casilla[1] == casilla[4]: #SI LOS NUMEROS SON IGUALES EL BARCO ESTA EN VERTICAL Y CONTAMOS LETRAS
            orientacion = int(equivalencias[casilla[0]]) - int(equivalencias[casilla[3]]) 
            var = abs(orientacion) + 1
            if var == tamano:
                if orientacion < 0:
                    for i in range(tamano):
                        aux = str(int(equivalencias[casilla[1]])+i) + str(casilla[4])
                        listaPosBarco.append(aux)
                else:
                    for i in range(tamano):
                        aux = str(int(equivalencias[casilla[1]])+i) + str(casilla[4])
                        listaPosBarco.append(aux)
                return True
            else:
                return False
        elif casilla[0] == casilla[3]: #SI LAS LETRAS SON IGUALES EL BARCO ESTA EN HORIZONTAL Y CONTAMOS NUMEROS
            orientacion = int(casilla[1]) - int(casilla[4])
            var = abs(orientacion) + 1
            if var == tamano:
                if orientacion < 0:
                    for i in range(tamano):
                        aux = str(casilla[0]) + str(int(casilla[1])+i)
                        listaPosBarco.append(aux)
                else:
                    for i in range(tamano):
                        aux = str(casilla[0]) + str(int(casilla[1])-i)
                        listaPosBarco.append(aux)
                return True
        else:
            return False
    else:
        listaPosBarco.append(casilla)
        return True

    #USAMOS listaBarco DONDE SE HA ALMACENADO TODAS LAS COORDENADAS QUE OCUPARÁ EL BARCO Y VAMOS MIRANDO UNA POR UNA SI ALREDEDOR O EN ESA MISMA COORDENADA
    #SI ESTÁ OCUPADA, SI LO ESTA LA FUNCION DEVUELVE FALSO, SI NO ENCUENTRA NADA DEVUELVE VERDADERO

def comprobarCasillas(listaJugador, listaPosBarco):
    for i in range(len(listaPosBarco)):
        varj = int(equivalencias[listaPosBarco[i][0]])
        vark = int(listaPosBarco[i][1])-1
        for j in range(3):
            for k in range(3):
                if ((varj+(j-1)) >= 0 and (vark+(k-1)) >= 0) or ((varj+(j-1)) <= 10 and (vark+(k-1)) <= 10): #TENEMOS EN CUENTA QUE SI UNA DE LAS COORDENADAS TOCA UNA PARED NO MIRAREMOS FUERA DEL RANGO DE LA MATRIZ
                    if listaJugador[varj+(j-1)][vark+(k-1)] == "<O>":  #SUPONGAMOS <O> SIMBOLO DE BARCO
                        return False
    return True
        

def juego():
    seguir = True
    while seguir:
        print ("1 --- Comenzar Partida\n2 --- Instrucciones\n3 --- Salir")
        entrada = str(input())
        if entrada == "1":
            print ("COMENZAR PARTIDA")
            jugador1 = input('Escribe tu nombre jugador 1: ')
            jugador2 = input('escribe tu nombre jugador 2: ')

            # inicializo una lista de 2 diccionarios con la info de cada jugador
            tablero = [[j for j in range(0,10)] for i in range(0,10)]
            jugadores = [{'nombre': jugador1,
                        'barcos':tablero[:],
                        'disparos':tablero[:]},
                        {'nombre': jugador2,
                        'barcos':tablero[:],
                        'disparos':tablero[:]}]


            # Le preguinto a cada  jugador donde quiere colocar los barcos
            turno_actual = 0
            for jugador in jugadores:
                #Tengo que saber cuantos barcos hay de cada . Pongo dos de momento para probar          
                lista_barcos = (4,2)
                print('Hola', jugador['nombre'])
                # creo el tablero del jugador
                # print(jugadores)
                for barco in lista_barcos:
                    coordenadas_barco = input(f'Escribe donde quieres colocar tu barco de {barco} casillas. Indicando la casilla de inicio y la de fin. Por ejemplo para el barco de 4: A1 A4: ')
                    #  AQUI VAN lAS COMPROBACIONES Y ME DEVUELVEN UNA LISTA DE CASILLAS
                    listaPosBarco = []
                    comprobacion1 = posBarco(coordenadas_barco, barco, listaPosBarco)
                    comprobacion2 = comprobarCasillas(jugador['barcos'], listaPosBarco)
                    if comprobacion1 and comprobacion2:
                        # lista_casillas = ['A1', 'A2', 'A3', 'A4']
                    # SI todo es correcto
                        for casilla in listaPosBarco:
                            colocarBarco(jugador['barcos'], casilla)
                        imprimirTableroBarcos(jugadores,turno_actual) 
            
                turno_actual +=1
                
            ganador = False
            
            turno_actual = 0
            while ganador == False:
                print('hola', jugadores[turno_actual]['nombre'])

                ##MUestro tus barcos
                print('estos Son tus barcos')
                imprimirTableroBarcos(jugadores, turno_actual)

                ##Empezamos a disparar
                guardarDisparos(jugadores[turno_actual]['barcos'], 'A1')
                guardarDisparos(jugadores[turno_actual]['barcos'], 'C1')
                print('estos Son tus disparons')
                imprimirTableroDisparos(jugadores, turno_actual)
                # turno_actual = cambiarTurno(turno_actual)
                ganador = True #Esto es para qe no entre en bucle
            

        elif entrada == "2":
            instrucciones()
        elif entrada == "3":
            print ("Adiós")
            seguir = False
        else:
            print ("Vuelve a Introducir")

juego()


