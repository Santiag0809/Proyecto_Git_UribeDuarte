from mod_json import*

def create_empanadas ():
    datos = read_json
    print ("Bienvenido al sistema de creacion de empanadas")
    while True:
        print("==============================")
        print("1. Crear Empanada")
        print("2. Salir del programa")
        print("==============================")
        o=input("Escoja su opcion numerica : ")
        if o == "1" :
            print("==============================")
            n=input("Crea el nombre de tu empanada : ")
            p=input("El precio que contendra tu empanada : ")
            ingredientes = []
            while True:
                ingrediente=input("Escriba el nombre del ingrediente o 'S' para salir al menu de creacion : ").strip().lower()
                if ingrediente == "s":
                    break
                elif ingrediente:
                    ingredientes.append(ingrediente)
            dis=input("¿Esta disponible actualmente la empanada? S/N : ").strip().lower
            if dis == "s":
                dis = True
            else:
                dis = False
            empanadas = [{
                "nombre":n,
                "precio $ ":p,
                "ingredientes":ingredientes,
                "disponibilidad":dis
            }]

            datos[empanadas].append(empanadas)
            save_json(datos)
            print("Empanada guardada con exito")

        if o == "2":
            op=input("Estas a punto de salir del programa, ¿Estas seguro que quieres hacerlo? S/N").lower
            if op == "s":
                print("Saliendo al menu principal . . .")
                break
            if op == "n":
                print("Regresando al menu de creacion . . .")
            else:
                print("Opcion invalida, regresando al menu de creacion . . .")

            

