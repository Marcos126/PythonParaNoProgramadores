listaNombres = []
listaApellidos = []
contador = 0

listaNombres.append("Martin")
listaNombres.append("Pedro")
listaNombres.append("Rodrigo")


listaApellidos.append("Martinez")
listaApellidos.append("Rodriguez")
listaApellidos.append("Natale")

while contador != len(listaNombres):
    print(listaNombres[contador], listaApellidos[contador])
    contador = contador + 1
