import os
from colorama import Fore, Style
#encoding: "UTF-16"

#Revisar disparo
def revisarDisparo(lista, letraInicio,letraFinal):
    try:#Probar el codigo
        if lista[letraInicio][letraFinal] != "D":#Si no se ha disparado en la casilla
            lista[letraInicio][letraFinal] = "D"#Cambiar la posicion de la lista por una D de disparo.
        else:
            print("Ya has disparado en esta casilla, repite el disparo.")
            guardarDisparos(lista)#Volver a disparar
    except:#Si hay error
        print("Error, el disparo está fuera de rango, repítelo")
        guardarDisparos(lista)#Volver a disparar

    else:#Si funciona bien
        return True

#Guardar disparo

def guardarDisparos(lista): #Se pasa la lista de disparos
    prueba = bool
    while prueba != True:
        disparo = input("¿Dónde quieres disparar?> ")
        disparo = disparo.upper()
        try:
            letraInicio = int(equivalencias.get(disparo[0]))
            letraFinal = int(disparo[1:])
            letraFinal-=1
            revisarDisparo(lista, letraInicio,letraFinal)#Comprobar si el disparo no esta repetido y esta bien
            
        except:
            print("Error de entrada del disparo. Debes entrar un sólo valor como A4 entre los valores disponibles (A-J y 1-10):")
        else:
            prueba = True
            
     
#Cambio de jugador
def cambioJugador(turno):
    #Devuelve el turno
    if turno == 0:
        return 1
    else:
        return 0

#LIMPIAR PANTALLA
def limpiarPantalla():
    input('Pulsa enter para acabar el turno')
    if os.name == "posix": #Para mac y linux
        _ = os.system("clear")
    else:#Para windows
        _ = os.system("cls")
    input('Pulsa enter para empezar tu turno')
    

def juego():
    print ("COMENZAR PARTIDA")
    jugador1 = input('Escribe tu nombre jugador 1: ')
    limpiarPantalla()
    jugador2 = input('Escribe tu nombre jugador 2: ')
    lista_barcos = (2,2)
    trozosBarco = contarTrozosBarco(lista_barcos)

    # inicializo una lista de 2 diccionarios con la info de cada jugador
    jugadores = [{'nombre': jugador1,
                'barcos':[[j for j in range(0,10)] for i in range(0,10)],
                'disparos':[[j for j in range(0,10)] for i in range(0,10)]},
                {'nombre': jugador2,
                'barcos':[[j for j in range(0,10)] for i in range(0,10)],
                'disparos':[[j for j in range(0,10)] for i in range(0,10)]}]


    # Le pregunto a cada  jugador donde quiere colocar los barcos
    turno_actual = 0
    for jugador in jugadores:
        #Tengo que saber cuantos barcos hay de cada . Pongo dos de momento para probar          
        print('Hola', jugador['nombre'])
        # creo el tablero del jugador
        # print(jugadores)
        imprimirTableroBarcos(jugadores, turno_actual)
        for barco in lista_barcos:
            seguir = True
            while seguir:
                coordenadas_barco = input(f'Escribe donde quieres colocar tu barco de {barco} casillas. Indica la casilla de inicio y la de fin. Por ejemplo para el barco de 4: A1 A4: ')
                #  AQUI VAN lAS COMPROBACIONES Y ME DEVUELVEN UNA LISTA DE CASILLAS
                listaPosBarco = []
                if posBarco(trocear(coordenadas_barco), barco, listaPosBarco) and comprobarCasillas(jugador['barcos'], listaPosBarco):
                    # lista_casillas = ['A1', 'A2', 'A3', 'A4']
                # SI todo es correcto
                    for casilla in listaPosBarco:
                        colocarBarco(jugador['barcos'], casilla)
                    imprimirTableroBarcos(jugadores,turno_actual) 
                    seguir = False
        limpiarPantalla()   

        turno_actual +=1
               
    ganador = False
            
    turno_actual = 0
    while ganador == False: #Esto es para qe no entre en bucle
        print('Hola', jugadores[turno_actual]['nombre'])

        ##MUestro tus barcos
        print('Estos son tus barcos: ')
        imprimirTableroBarcos(jugadores, turno_actual)

        ##Empezamos a disparar
        print('Estos son tus disparons ')
        imprimirTableroDisparos(jugadores, turno_actual)
        guardarDisparos(jugadores[turno_actual]['disparos'])
        imprimirTableroDisparos(jugadores, turno_actual)
        ganador = comprobarGanador(jugadores, turno_actual, trozosBarco)
        turno_actual = cambioJugador(turno_actual)
        limpiarPantalla()

    turno_actual = cambioJugador(turno_actual)
    print(f"Ha ganado {jugadores[turno_actual]['nombre']}") 


#INSTRUCCIONES
def mostrarInstrucciones():
    #Explicar como funciona el juego
    print("\n------Cómo se juega a este juego------\n")
    print("El juego consiste en hundir todos los barcos del contrincante.")
    print("Para ello, debes colocar tu propia flota estratégicamente, y encontrar y hundir la flota contraria.")
    print("Cada jugador tiene su propio tablero y deberá posicionar los barcos deseados en el tablero")
    print("La colocación de los barcos debe ser respetando la franja de las posiciones, es decir, nunca se puede colocar un barco al lado de otro, este debe estar al menos a más de una posición de cualquier otro barco del tablero.")
    print("Para colocar cada barco se dirá la posición inicial y la final de éste. Por ejemplo, si es un barco de 3 casillas: B3 B5, asi éste será colocado en B3, B4 y B5. Si sólo es el barco de una casilla solo se introducirá una coordenada.")
    print("Para disparar a otro jugador se deberá insertar una coordenada no repetida anteriormente y si se golpea a un barco será 'tocado', si se falla será 'agua'. Para que un barco se hunda debe golpearse en todas sus casillas.")
    print("Para ganar se debe hundir todos los barcos del contrincante. Si te hunden todos tus barcos has perdido.\n")

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
    letra_inicio, numero_inicio = casilla[0], int(casilla[1:])
    lista_barcos[int(equivalencias[letra_inicio])][numero_inicio-1] = 'X'
    

def imprimirTableroBarcos(jugadores, turno):
    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    rival = cambioJugador(turno)

    # Imprimo mi tablero de barcos con los disparos del rival
    for fila in range(len(jugadores[turno]['barcos'])):
        print(letras[fila], end=" ")
        for columna in range(len(jugadores[turno]['barcos'][fila])):
            ## Barcos que me han disparado
            if jugadores[turno]['barcos'][fila][columna] == 'X' and jugadores[rival]['disparos'][fila][columna] == 'D':
                print(Fore.RED + 'DD', end = " ")
                print(Style.RESET_ALL, end = "")
            ## DISPAROS DEL RIVAL EN AGUA
            elif jugadores[turno]['barcos'][fila][columna] != 'X' and jugadores[rival]['disparos'][fila][columna] == 'D':
                print(Fore.CYAN +'~~', end = " ")
                print(Style.RESET_ALL, end = "")
            # MIS BARCOS
            elif jugadores[turno]['barcos'][fila][columna] == 'X' and jugadores[rival]['disparos'][fila][columna] != 'D':
                print(Fore.GREEN +'XX', end = " ")
                print(Style.RESET_ALL, end = "")
            # Zonas de agua sin disparos y sin barcos
            else: 
                print(Fore.BLUE +'--', end = " ")
                print(Style.RESET_ALL, end = "")
        print(end = "\n")

def imprimirTableroDisparos(jugadores, turno):
    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    rival = cambioJugador(turno)
    
    # Imprimo el tablero de mis disparos
    for fila in range(len(jugadores[turno]['disparos'])):
        print(letras[fila], end=" ")
        for columna in range(len(jugadores[turno]['disparos'][fila])):
            #  SI HE DADO A UN BARCO
            if jugadores[turno]['disparos'][fila][columna] == 'D' and jugadores[rival]['barcos'][fila][columna] == 'X':
                print(Fore.RED + 'TT', end = " ")
                print(Style.RESET_ALL, end = "")
            #  Si he dado a agua
            elif jugadores[turno]['disparos'][fila][columna] == 'D' and jugadores[rival]['barcos'][fila][columna] != 'X':
                print(Fore.CYAN +'AG', end = " ")
                print(Style.RESET_ALL, end = "")
            # Casillas que no se que hay
            else: 
                print(Fore.BLUE + '--', end = " ")
                print(Style.RESET_ALL, end = "")
        print(end = "\n")


#ASUMIMOS QUE LA ENTRADA DEL USUARIO VA A SER SIEMPRE ALGO COMO ESTO: "B3 B7", "A5 A1"
#COMPRUEBA SI EL BARCO TIENE UNA ORIENTACION Y TAMAÑO CORRECTOS. DESPUES METE TODAS LAS COORDENADAS QUE OCUPA EL BARCO EN listaPosBarco

def trocear(casilla):
    aux = casilla.upper()
    aux = aux.replace(" ", "")
    if len(aux) == 6 or len(aux) == 5:
        aux = aux.replace("1", "")
        return aux
    else:
        return aux

def posBarco(trozo, tamano, listaPosBarco):
    try:
        if tamano > 1:
            listaLetras = list(equivalencias.keys())
            if trozo[0] == trozo[2]:    #LETRAS IGUALES, BARCO EN HORIZONTAL, CONTAMOS NUMEROS
                if trozo[1] == "0":
                    orientacion = 10 - int(trozo[3])
                elif trozo[3] == "0":
                    orientacion = int(trozo[1]) - 10
                else:    
                    orientacion = int(trozo[1]) - int(trozo[3])
                var = abs(orientacion) + 1
                if var == tamano:
                    if orientacion < 0:
                        for i in range(tamano):
                            aux = str(trozo[0]) + str(int(trozo[1])+i)
                            listaPosBarco.append(aux)
                    else:
                        comp = trozo[1]
                        if comp == "0":
                            comp = "10"
                        for i in range(tamano):            
                            aux = str(trozo[0]) + str(int(comp)-i)
                            listaPosBarco.append(aux)
                    return True
                else:
                    print('Error. El barco no tiene el tamaño adecuado')
                    return False
            elif trozo[1] == trozo[3]:  #NUMEROS IGUALES, BARCO EN VERTICAL, CONTAMOS LETRAS
                orientacion = int(equivalencias[trozo[0]]) - int(equivalencias[trozo[2]]) 
                var = abs(orientacion) + 1
                if var == tamano:
                    if orientacion < 0:
                        comp = trozo[1]
                        if comp == "0":
                            comp = "10"
                        for i in range(tamano):
                            aux = int(equivalencias[trozo[0]])+i
                            aux = listaLetras[aux] 
                            listaPosBarco.append(str(aux) + str(comp))
                    else:
                        comp = trozo[1]
                        if comp == "0":
                            comp = "10"
                        for i in range(tamano):
                            aux = int(equivalencias[trozo[0]])-i
                            aux = listaLetras[aux]      
                            listaPosBarco.append(str(aux) + str(comp))
                    return True
                else:
                    print('Error. El barco no tiene el tamaño adecuado')
                    return False
            else:
                print('No se puede colocar en diagonal')
                return False
        else:
            listaPosBarco.append(trozo)
            return True
    except:
        print("Entrada de datos inválida, vuelve a intentarlo")
        return False

    #USAMOS listaBarco DONDE SE HA ALMACENADO TODAS LAS COORDENADAS QUE OCUPARÁ EL BARCO Y VAMOS MIRANDO UNA POR UNA SI ALREDEDOR O EN ESA MISMA COORDENADA
    #SI ESTÁ OCUPADA, SI LO ESTA LA FUNCION DEVUELVE FALSO, SI NO ENCUENTRA NADA DEVUELVE VERDADERO
def comprobarCasillas(listaJugador, listaPosBarco):
    for i in range(len(listaPosBarco)):
        varj = int(equivalencias[listaPosBarco[i][0]])
        vark = int(listaPosBarco[i][1:])-1
        for j in range(3):
            for k in range(3):
                if ((varj+(j-1)) >= 0 and (vark+(k-1)) >= 0) and ((varj+(j-1)) <= 9 and (vark+(k-1)) <= 9): #TENEMOS EN CUENTA QUE SI UNA DE LAS COORDENADAS TOCA UNA PARED NO MIRAREMOS FUERA DEL RANGO DE LA MATRIZ
                    if listaJugador[varj+(j-1)][vark+(k-1)] == "X":  #SUPONGAMOS <O> SIMBOLO DE BARCO
                        print('Posición ocupada o muy cerca de otro barco')
                        return False
    return True

def contarTrozosBarco(barcos):
    trozos = 0
    for i in range(len(barcos)):
        trozos += int(barcos[i])
    return trozos

def comprobarGanador(listaJugadores, turno, maxBarcos):
    counter = 0
    rival = cambioJugador(turno)
    for fila in range(len(listaJugadores[turno]['disparos'])):
        for columna in range(len(listaJugadores[turno]['disparos'][fila])):
            if listaJugadores[turno]['disparos'][fila][columna] == 'D' and listaJugadores[rival]['barcos'][fila][columna] == 'X':
                counter+=1
    if maxBarcos == counter:
        return True
    else:
        return False

def programa():
    seguir = True
    while seguir:
        print ("1 --- Comenzar Partida\n2 --- Instrucciones\n3 --- Salir")
        entrada = str(input())
        if entrada == "1":
            juego()
            seguir = False
        elif entrada == "2":
            mostrarInstrucciones()
        elif entrada == "3":
            print ("Adiós")
            seguir = False
        else:
            print ("Vuelve a introducir")

programa()