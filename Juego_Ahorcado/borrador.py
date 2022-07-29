#asd
while True:
    choise_admin = input(
        " 1 -- Modificar VIDAS\n 2 -- Modificar PUNTOS\n 3 -- Modificar BONUS\n 4 -- Modificar PALABRAS\n 5 -- SALIR\n")
    # 1 - MODIFICAR VIDAS
    if choise_admin == 1:
        print("Seleccione el modo al que desea cambiar las VIDAS")
        cat_seleccionada = input(
            " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")

        if cat_seleccionada.lower() == "d":
            cambio_vida = input("¿Cuantas vidas desea poner en DIFICIL?")
            VIDASD = cambio_vida
            break
        elif cat_seleccionada.lower() == "m":
            cambio_vida = input("¿Cuantas vidas desea poner en MEDIO?")
            VIDASM = cambio_vida
            break
        elif cat_seleccionada.lower() == "f":
            cambio_vida = input("¿Cuantas vidas desea poner en FACIL?")
            VIDASF = cambio_vida
            break
        else:
            print("Por favor no sea manco seleccione un modo correcto")
            cat_seleccionada = input(
                "Ingrese D para el modo DIFICIL, M para el modo MEDIO, F para el modo FACIL: ")

    # 2 - MODIFICAR PUNTOS
    elif choise_admin == 2:
        print("Seleccione el modo al que desea cambiar las PUNTOS")
        cat_seleccionada = input(
            " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
        if cat_seleccionada.lower() == "d":
            print("")
            break
        elif cat_seleccionada.lower() == "m":
            print("")
            break
        elif cat_seleccionada.lower() == "f":
            print("")
            break

    # 3 - MODIFICAR BONUS
    elif choise_admin == 3:
        print("Seleccione el modo al que desea cambiar las BONUS")
        cat_seleccionada = input(
            " D -- modo DIFICIL\n M -- modo MEDIO \n F -- modo FACIL: ")
        if cat_seleccionada.lower() == "d":
            print("")
            break
        if cat_seleccionada.lower() == "m":
            print("")
            break
        if cat_seleccionada.lower() == "f":
            print("")
            break

    # 4 - MODIFICAR PALABRAS
    elif choise_admin == 4:
        print("Seleccione el modo al que desea cambiar las PALABRAS")
        if cat_seleccionada.lower() == "d":
            print("1 -- CAMBIAR PALABRA EN DIFICIL \n 2 -- PALABRAS DEFAULT")
            break
        elif cat_seleccionada.lower() == "m":
            print("CAMBIAR PALABRA EN MEDIO \n 2 -- PALABRAS DEFAULT")
            break
        elif cat_seleccionada.lower() == "f":
            print("CAMBIAR PALABRA EN FACIL \n 2 -- PALABRAS DEFAULT")
            break
    # 5 - SALIR
    elif choise_admin == 5:
        print("Fin del juego")
        break
    else:
        print("ojo modo incorrecttttt")
        exit()
