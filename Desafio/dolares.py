""" 
Declaracion del sueldo por mes que cobraba el empleado
"""
enero = 300
febrero = 300
marzo = 300
abril = 300
mayo = 300
junio = 300
julio = 500
agosto = 500
septiembre = 500
octubre = 500
noviembre = 900
diciembre = 900

""""
Operacion de promedio del sueldo del empleado
"""
sueldo_promedio = (
    enero
    + febrero
    + marzo
    + abril
    + mayo
    + junio
    + julio
    + agosto
    + septiembre
    + octubre
    + noviembre
    + diciembre
) / 12

""" 
Declaracion de condicionales para saber si el sueldo de la persona es alto o bajo
"""

if sueldo_promedio < 300:
    print("En promedio cobra por debajo de lo normal")
elif sueldo_promedio >= 300 or sueldo_promedio <= 900:
    print("En promedio cobra un sueldo normal")
elif sueldo_promedio > 900:
    print("En promedio cobra un sueldo mejor que lo normal")
print(int(sueldo_promedio))
