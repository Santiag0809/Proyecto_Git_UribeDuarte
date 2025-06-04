import json

def read_json():
    with open("data/content.json", "r") as file:
        # JSON LOAD, LEE UNA ESTRUCTURA JSON Y LA CONVIERTE A ESTRUCTURA PYTHON
         return json.load(file)
    # SE RETORNA PARA QUE DEVUELVA EL CONTENIDO Y SE LEA

def save_json(archivos):
    with open("data/content.json", "w") as outfile:
        # JSON DUMP, GUARDA EL PYTHON COMO ESTRUCTURA JSON
         json.dump(archivos,outfile,indent=4)
    