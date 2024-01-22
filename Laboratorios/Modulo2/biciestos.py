while True:
    print("Ingrese el Año que desea verificar")
    numero = input()
    numero = int(numero)
    if numero % 400 == 0:
        print("El año ingresado es biciesto")
        continue
    elif numero % 4 == 0 and numero % 100 != 0:
        print("El año ingresado es biciesto")
        continue
    else:
        print("El año ingresado no es biciesto")
        continue
