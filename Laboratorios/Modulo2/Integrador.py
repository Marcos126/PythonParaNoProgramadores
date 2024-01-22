# Declaracion de variables de la lista de los alumnos y la cantidad de cursos

listaNombres = []
cantidadCursos = []
# Lista con bucle while para que te devuelva al menu cada vez que termines de ingresar la operacion

while True:
    contador = 0
    print("\n Ingrese el numero de la operacion que desea ejecutar:")
    print("1 - Ver la lista de alumno")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")

    # seleccionador

    seleccion = input()

    seleccion = int(seleccion)

    # ifs para hacer uso del seleccionador

    if seleccion == 1:
        if len(listaNombres) == 0:
            print("Todavia no hay nadie inscripto en el sistema \n")
        else:
            while contador != len(cantidadCursos):
                print(
                    "El alumno ",
                    listaNombres[contador],
                    "esta inscripto a ",
                    cantidadCursos[contador],
                    "cursos!",
                )
                contador = contador + 1
    elif seleccion == 2:
        print("ingrese el nombre que desea agregar a la lista")
        nombreAlumno = input()
        print("Ingrese a cuantos cursos esta inscripto")
        cursosCantidad = input()
        listaNombres.append(nombreAlumno)
        cantidadCursos.append(cursosCantidad)
        print("Se ha agregado", nombreAlumno, "Con", cursosCantidad, "cursos! \n")
    elif seleccion == 3:
        print("Adios")
        break
    else:
        print("el numero ingresado es incorrecto")


print("done!")
