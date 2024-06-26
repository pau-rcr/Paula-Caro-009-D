import os
from funciones import agregarCategoria, editarCategoria, eliminarCategoria, buscarCategoria

opciones = ["Mantenedor de categorías.","Reportes.","Salir.\n"]
opcionesMantenedor = ["Agregar categoría.","Editar categoría.","Eliminar categoría.","Buscar categoría.","Volver.\n"]

while True:
    contador = 0
    print("***********************\n*     MUNDO LIBRO     *\n***********************\n")
    for i in opciones:
        contador += 1
        print(f"[{contador}] - {i}")
    eleccion = input("Escriba el número de la operación que desea realizar a continuación: ")
    os.system("cls")
    if eleccion == "1":
        while True:
            print("****************************\n* Mantenedor de categorías *\n****************************\n")
            contador = 0
            for i in opcionesMantenedor:
                contador += 1
                print(f"[{contador}] - {i}")
            eleccionMantenedor = input("Escriba el número de la operación que desea relizar a continuación: ")
            if eleccionMantenedor == "1":
                nombreCategoria = input("Ingrese el nombre de la categoría a agregar: ")
                agregarCategoria(nombreCategoria)
                print("Ha agregado una categoría. ")

            elif eleccionMantenedor == "2":
                id = int(input("Ingrese el ID de la categoría que quiere editar: "))
                nuevoNombre = input("Ingrese el nuevo nombre de la categoría: ")
                editarCategoria(nuevoNombre,id)
                print(f"Ha editado el nombre de la categoría de ID {id} a {nuevoNombre}.")

            elif eleccionMantenedor =="3":
                id = int(input("Ingrese el ID de la categoría que desea eliminar: "))
                eliminarCategoria(id)
                print("Ha eliminado la categoría de con éxito. ")

            elif eleccionMantenedor == "4":
                id = int(input("Ingrese el ID  de la categoría que quiere buscar: "))
                buscarCategoria(id)

            elif eleccionMantenedor == "5":
                os.system("cls")
                break

            enter = input("ENTER para continuar")
            os.system("cls")
    elif eleccion == "2":
        print("Aquí se debería generar el reporte pero no me dio el tiempo.")
    elif eleccion == "3":
        os.system("cls")
        break