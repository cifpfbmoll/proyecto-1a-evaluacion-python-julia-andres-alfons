def instrucciones():
    print("------Como se juega a este juego------")


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