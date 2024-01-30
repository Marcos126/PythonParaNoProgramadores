listaNombres = []
while True:
    print("Ingrese la cantidad de nombres que desea ingresar")
    cantidadNombre = int(input())
    contador = 0
    for a in range(0, cantidadNombre):
        print("Ingrese el nombre a añadir a la lista")
        ingresoNombre = input()
        listaNombres.append(ingresoNombre)
    print("")
    for b in listaNombres:
        print(b)
    break
