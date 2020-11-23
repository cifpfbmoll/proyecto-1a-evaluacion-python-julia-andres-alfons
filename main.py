#encoding: "UTF-16"

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
    

def imprimirTablero(lista):
    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    for fila in range(len(lista)):
        print(letras[fila], end=" ")
        for columna in range(len(lista[fila])):
            # print(columna)
            if lista[fila][columna] == 'X':
                print('XX', end = " ")
            else: 
                print('--', end = " ")
        print(end = "\n")

# lista = [[j for j in range(0,10)] for i in range(0,10)]
# imprimirTablero(lista)

# print('esta es la lista origianl',lista)
# colocarBarco(lista,'A3' )
# print('esta es la lista con un barco en la casilla A3',lista)
# imprimirTablero(lista)

#ASUMIMOS QUE LA ENTRADA DEL USUARIO VA ASER SIEMPRE ALGO COMO ESTO: "B3 B7", "A5 A1"
def posBarco(casilla, tamano):
    if casilla[0] == casilla[3]:
        var = int(equivalencias.get(casilla[1])) - int(equivalencias.get(casilla[4])) 
        var = abs(var) + 1
        if var == tamano:
            return True
        else:
            return False
    elif casilla[1] == casilla[4]:
        var = int(casilla[0]) - int(casilla[3])
        var = abs(var) + 1
        if var == tamano:
            return True
    else:
        return False

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
            jugadores = [{'nombre': jugador1},
                        {'nombre': jugador2}]

            # Le preguinto a cada  jugador donde quiere colocar los barcos
            for jugador in jugadores:
                #Tengo que saber cuantos barcos hay de cada . Pongo dos de momento para probar          
                lista_barcos = (4,3)
                print('Hola', jugador['nombre'])
                # creo el tablero del jugador
                tablero = [[j for j in range(0,10)] for i in range(0,10)]
                # guardo el tablero en el diccionario de ese jugador
                jugador['barcos'] = tablero

                for barco in lista_barcos:
                    imprimirTablero(jugador['barcos'])
                    coordenadas_barco = input(f'Escribe donde quieres colocar tu barco de {barco} casillas. Indicando la casilla de inicio y la de fin. Por ejemplo para el barco de 4: A1 A4: ')
                    #  AQUI VAN lAS COMPROBACIONES Y ME DEVUELVEN UNA LISTA DE CASILLAS
                    lista_casillas = ['A1', 'A2', 'A3', 'A4']
                    # SI todo es correcto
                    for casilla in lista_casillas:
                        colocarBarco(jugador['barcos'], casilla)
            
        elif entrada == "2":
            instrucciones()
        elif entrada == "3":
            print ("Adiós")
            seguir = False
        else:
            print ("Vuelve a Introducir")

juego()



#
def posCorrecta(barcosTablero, casilla):
    if casilla[0] 



posCorrecta(barcosTablero, "A4 A6")