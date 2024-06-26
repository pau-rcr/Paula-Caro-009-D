import json

def agregarCategoria(nombreCategoria:str):
    with open("biblioteca.json", mode = "r") as leerJson:
       archivoJson = json.load(leerJson)
       indice = len(archivoJson["Categoria"]) + 1
       nuevaCategoria = {
            "CategoriaID": indice,
            "Nombre": nombreCategoria
       }
       archivoJson["Categoria"].append(nuevaCategoria)
    with open("biblioteca.json", mode = "w") as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)

def editarCategoria(nuevoNombre:str,id:int):
    with open("biblioteca.json", mode = "r") as leerJson:
       archivoJson = json.load(leerJson)
       contador = 0
       for i in archivoJson["Categoria"]:
        if i["CategoriaID"] == id:
           archivoJson["Categoria"][contador]["CategoriaID"] = nuevoNombre
        contador += 1
    with open("biblioteca.json", mode = "w") as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)

def eliminarCategoria(id:int):
    with open("biblioteca.json", mode = "r") as leerJson:
        archivoJson = json.load(leerJson)
        contador = 0
        for i in archivoJson["Categoria"]:
            if i["CategoriaID"] == id:
                del archivoJson["Categoria"][contador]
            contador += 1
    with open("biblioteca.json", mode = "w") as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)

def buscarCategoria(id:int):
    with open("biblioteca.json", mode = "r") as leerJson:
        archivoJson = json.load(leerJson)
        contador = 0
        for i in archivoJson["Categoria"]:
            if i["CategoriaID"] == id:
                print(f"La categoría que busca es la siguiente:\n",archivoJson["Categoria"][contador])
            contador += 1
    with open("biblioteca.json", mode = "w") as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)
