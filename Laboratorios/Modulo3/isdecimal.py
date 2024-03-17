while True:
    variable = input("Ingrese un numero por favor:")

    if variable.strip().isdecimal() == True:
        variable = int(variable)
        print(type(variable))
        break
    else:
        print("No ha ingresado un numero")
print("done")