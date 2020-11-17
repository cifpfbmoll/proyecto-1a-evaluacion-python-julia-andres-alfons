def instrucciones():
    print("------Como se juega a este juego------")


# def juego():
#     seguir = True
#     while seguir:
#         print ("1 --- Comenzar Partida\n2 --- Instrucciones\n3 --- Salir")
#         ent = str(input())
#         if ent == "1":
#             print ("OPCION1")
#         elif ent == "2":
#             instrucciones()
#         elif ent == "3":
#             print ("Adios")
#             seguir = False
#         else:
#             print ("Vuelve a Introducir")

# juego()


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

<<<<<<< HEAD
lista = [[j for j in range(0,10)] for i in range(0,10)]
print('esta es la lista origianl',lista)

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
    lista[int(equivalencias[letra_inicio])][numero_inicio-1] = 'X'


colocarBarco(lista,'A3' )
print('esta es la lista con un barco en la casilla A3',lista)
=======
#ASUMIMOS QUE LA ENTRADA DEL USUARIO VA ASER SIEMPRE ALGO COMO ESTO: "B3 B7", "A5 A1"
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
>>>>>>> d45023b3f1c538b5b2c3666623179a31a658ff6e
