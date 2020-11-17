#encoding: "UTF-16"

def instrucciones():
    print("\n------Como se juega a este juego------\n")
    print("El juego consiste en undir todos los barcos del contrincante.")
    print("Para ello, debe colocar su propia flota estrategicamente, encontrar y undir la flota contraria.")
    print("Cada jugador tiene su propio tablero y debera posicionar los siguientes barcos en el:")
    print("- 1 barco de 4 posiciones.")
    print("- 2 barcos de 3 posiciones.")
    print("- 3 barcos de 2 posiciones.")
    print("- 4 barcos de 1 posicion.")
    print("La colocacion de los barcos debe ser respetando la franja de las posiciones, es decir, nunca se puede colocar un barco al lado de otro, este debe estar almenos a mas de una posicion de cualquier otro barco del tablero.")
    print("Para colocar cada barco se dira la posicion inicial y la final de este, por ejemplo, si es un barco de 3 casilla: B3 B5, asi este sera colocado en B3, B4 i B5. Si se tr")

instrucciones()





def juego():
    seguir = True
    while seguir:
        print ("1 --- Comenzar Partida\n2 --- Instrucciones\n3 --- Salir")
        ent = str(input())
        if ent == "1":
            print ("OPCION1")
        elif ent == "2":
            instrucciones()
        elif ent == "3":
            print ("Adios")
            seguir = False
        else:
            print ("Vuelve a Introducir")

juego()


def imprimirTablero():
    lista = [[j for j in range(0,10)] for i in range(0,10)]

    letras = ('A |', 'B |', 'C |', 'D |', 'E |', 'F |', 'G |', 'H |', 'I |', 'J |')
    print('     1  2  3  4  5  6  7  8  9 10')
    print('---------------------------------')

    for fila in range(len(lista)):
        print(letras[fila], end=" ")
        for columna in range(len(lista[fila])):
            print(f'{fila}{lista[fila][columna]}', end = " ")
        print(end = "\n")

imprimirTablero()

def posBarco(casilla, tamano):
    if casilla[0] == casilla[3]:
        var = int(casilla[0]) - int(casilla[3]) 
        var = abs(var) + 1
        if var == tamano:
            return True
        else:
            return False
    elif casilla[1] == casilla[4]:
        print("NO FUNCTION")
        #FALTA EL DICCIONARIO PARA LAS LETRAS Y SUS VALORES NUMERICOS
    else:
        return False
