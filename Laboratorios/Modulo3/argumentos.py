#adentro de los parentecis del nombre de la funcion, va el argumento, el argumento puede ser una variable ya declarada u otros elementos, se puede declarar variables en el mismo argumento

def imprimir_elementos(lista):
    for elemento in lista:
        print(elemento)

alumnos = ["Pablo", "Juan","Matias","Martin"]
notas = [5.5, 9, 6.25, 8]

print("Alumnos:")
imprimir_elementos(alumnos)
    
print("Notas:")
imprimir_elementos(notas)