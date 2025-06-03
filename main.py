print("Bienvenido al programa de empanadas ")

while True:
    print("===============================================")
    print(" 1. Añadir empanadas")
    print(" 2. Actualizar o editar lista de empanadas")
    print(" 3. Borrar empanada")
    print(" 4. Salir del programa de empanadas")
    print("===============================================")
    opcion=input("Escoja su opcion numerica : ")

    if opcion == "1":
        print("Funcion de añadir empanadas")


    if opcion == "2":
        print("FUncion de actualizar o editar empanadas")

    if opcion == "3":
        print("FUncion de borrar empanadas")

    if opcion == "4":
        salida=input("Estas saliendo del programa, ¿estas seguro que quires hacerlo? S/N : ").lower()
        if salida == "s":
            print("Estas saliendo del programa, adiooooooooooos")
            break
        if salida == "n":
            print("Perfecto, devolviendo al programa")
        else:
            print("Opcion invalida, devolviendote al programa")
    else:
        print("Opcion invalida")
    
