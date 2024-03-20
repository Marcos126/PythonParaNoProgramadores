#Isdecimal es una opcion que se le puede aplicar a un dato que va a detectar si es un numero decimal, falla en indicar numeros negativos y numeros con coma.

while True:
    variable = input("Ingrese un numero por favor:")

    if variable.strip().isdecimal() == True:
        variable = int(variable)
        print(type(variable))
        break
    else:
        print("No ha ingresado un numero")
print("done")