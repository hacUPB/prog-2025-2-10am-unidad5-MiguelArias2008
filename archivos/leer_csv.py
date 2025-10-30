import csv

with open ("C:\\Users\\Usuario\\Desktop\\variables.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    presion = []
    print(encabezado[-1])
    for fila in lector:
        fila [-1] = fila [-1].replace(",", ".")
        dato = float(fila[-1])
        presion.append(dato)
print (presion)
suma = sum(presion)
print(suma)
promedio = sum(presion) / len(presion)
print(promedio)


