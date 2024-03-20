def rango(desde, hasta):
    numeros = []
    while desde < hasta + 1:
        numeros.append(desde)
        desde = desde + 1
    return numeros

lista = rango(1,6)
print(lista)              