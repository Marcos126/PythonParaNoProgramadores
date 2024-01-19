lista = []
while True:
    print("Ingrese el numero de la operacion que desea ejecutar:")
    print("1 - Ver la lista de alumno")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")

    seleccion = input()

    seleccion = int(seleccion)

    if seleccion == 1:
        print(lista)
    elif seleccion == 2:
        print("ingrese el nombre que desea agregar a la lista")
        insert = input()
        lista.append(insert)
    elif seleccion == 3:
        print("Adios")
        break
    else:
        print("el numero ingresado es incorrecto")
