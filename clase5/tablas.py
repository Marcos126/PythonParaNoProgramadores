n = input("Ingrese la tabla a consultar")
i = 0

n = int(n)

while True:
    x = n * i
    print(n, "x", i, "=", x)
    i = i + 1
    if i == 21:
        break

print("done")
