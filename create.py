from mod_json import*

def create_empanadas ():
    # Primero se importo lo escrito en el mod_json 
    datos = read_json
    # Se crea la variable datos que tendra como valor el read_json
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
            # Se pediran las caracteristicas de la empanada
            ingredientes = []
            # Ingredientes puede contener una cantidad sin fin de ingredientes de la empanada por lo cual se hace una lista 
            while True:
                ingrediente=input("Escriba el nombre del ingrediente o 'S' para salir al menu de creacion : ").strip().lower()
                if ingrediente == "s":
                    break
                elif ingrediente:
                    # Se añade los valores puesto en la variable ingrediente a la lista INGREDIENTES
                    ingredientes.append(ingrediente)
            dis=input("¿Esta disponible actualmente la empanada? S/N : ").strip().lower
            # Se pide verificacion de si estara o no dispoible la empanada 
            if dis == "s":
                dis = True
            else:
                dis = False
            # Se creo una lista llamada empanadas que ira dentro del diccionario de json debido a que de esta forma se facilita el trabajo 
            empanadas = [{
                "nombre":n,
                "precio $ ":p,
                "ingredientes":ingredientes,
                "disponibilidad":dis
            }]
            # Se añaden la lista empanadas
            datos[empanadas].append(empanadas)
            save_json(datos)
            print("Empanada guardada con exito")
            # Se saldra del programa dependiendo de su respuesta, si o no 
        if o == "2":
            op=input("Estas a punto de salir del programa, ¿Estas seguro que quieres hacerlo? S/N").lower
            if op == "s":
                print("Saliendo al menu principal . . .")
                break
            if op == "n":
                print("Regresando al menu de creacion . . .")
            else:
                print("Opcion invalida, regresando al menu de creacion . . .")

            

