while True:
    print("Que rol cumple en esta institucion?")
    nombreUsuario = input()

    if nombreUsuario == "admin" or nombreUsuario == "Profesor":
        print("Ingrese su password")
        password = input()
        if password == "1234":
            print("Ingrese su nombre, por favor")
            nombrePersona = input()
            if nombrePersona.strip() != "":
                print("Hola, bienvenido", nombrePersona)
                break
            else:
                print("El Nombre ingresado es invalido")
        else:
            print("El password ingresado es incorrecto")
    else:
        print("El nombre de usuario es invalido")
