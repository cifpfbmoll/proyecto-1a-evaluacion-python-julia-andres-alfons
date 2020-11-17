def juego():
    seguir = True
    while seguir:
        print ("1 --- Comenzar Partida\n2 --- Instrucciones\n3 --- Salir")
        ent = str(input())
        if ent == "1":
            print ("OPCION1")
        elif ent == "2":
            print ("OPCION2")
        elif ent == "3":
            print ("Adios")
            seguir = False
        else:
            print ("Vuelve a Introducir")

juego()