inicio = input("Ingrese el inicio del rango: ")
final = input("Ingrese el final del rango: ")
multiplos3 = []
multiplos5 = []
for i in range(int(inicio),int(final) + 1):
    valor3 = 3 * i
    valor5 = 5 * i
    multiplos3.append(valor3) 
    multiplos5.append(valor5)
print(multiplos5)
print(multiplos3)
