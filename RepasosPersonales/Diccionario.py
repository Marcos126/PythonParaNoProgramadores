alumno1 = {"nombre": "Pedro", "Cursos": 3}


print(alumno1["nombre"])
print(alumno1["Cursos"])
print("")


alumno1["nombre"] = "Martin"
alumno1["Cursos"] = 4
alumno1["CursoActual"] = "Python"

for clave in alumno1:
    print(alumno1[clave])

print("done")
