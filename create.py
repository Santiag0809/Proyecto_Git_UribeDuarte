from modular_functions import*
def create_empanadas ():
    # Primero se importo lo escrito en el mod_json 
    datos = read_json()
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

            # Ingredientes puede contener una cantidad sin fin de ingredientes de la empanada por lo cual se hace una lista 
            ingredientes = []

            while True:
                ingrediente=input("Escriba el nombre del ingrediente o 'S' para salir al menu de creacion : ").strip().lower()
                if ingrediente == "s":
                    break
                elif ingrediente:
                    # Se añade los valores puesto en la variable ingrediente a la lista INGREDIENTES
                    ingredientes.append(ingrediente)

            dis=input("¿Esta disponible actualmente la empanada? S/N : ").strip().lower()

            # Se pide verificacion de si estara o no dispoible la empanada 
            if dis == "s":
                dis = True
            else:
                dis = False

            # Se creo una lista llamada empanadas que ira dentro del diccionario de json debido a que de esta forma se facilita el trabajo 
            nueva_empanada = [{
                "nombre":n,
                "precio $ ":p,
                "ingredientes":ingredientes,
                "disponibilidad":dis
            }]
            # Los valores escritos por el usuario se añadiran a la lista de diccionario nueva_empanada

            # De esta forma se verifica que la clave de valor empanadas exista, si esta no existe se creara
            if "empanadas" not in datos:
                datos["empanadas"] = []
                
            # Ahora datos que abre y lee el json junto con la clave de valor empandas que es una lista añadira nueva empanada
            datos["empanadas"].append(nueva_empanada)

            # Mediante la funcion que pasa de contenido PYTHON a json se guardaran nuestras implementaciones de nueva empanada
            save_json(datos)
            print("Empanada guardada con exito")

            # Se saldra del menu dependiendo de su respuesta, si o no 
        if o == "2":
            op=input("Estas a punto de salir del menu de creacion, ¿Estas seguro que quieres hacerlo? S/N : ").strip().lower()
            if op == "s":
                print("Saliendo al menu principal . . .")
                break
            if op == "n":
                print("Regresando al menu de creacion . . .")
            # Si la respuesta del usuario fue diferente a la esperada, el usuario permanecera en el menu de creacion 
            else:
                print("Opcion invalida, regresando al menu de creacion . . .")