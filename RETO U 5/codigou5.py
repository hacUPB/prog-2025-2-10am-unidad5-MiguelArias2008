import os
import csv
import matplotlib.pyplot as plt

ruta_base = "C:/Users/Usuario/prog-2025-2-10am-unidad5-MiguelArias2008/RETO U 5/"

def listar_archivos():
    archivos = os.listdir(ruta_base)
    for archivo in archivos:
        print(archivo)

def contar_palabras_caracteres():
    archivo = input("Nombre del archivo .txt: ")
    with open(ruta_base + archivo, "r", encoding="utf-8") as f:
        texto = f.read()
        palabras = texto.split()
        total_palabras = len(palabras)
        total_caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", ""))
        print("Palabras:", total_palabras)
        print("Caracteres con espacios:", total_caracteres)
        print("Caracteres sin espacios:", sin_espacios)

def reemplazar_palabra():
    archivo = input("Nombre del archivo .txt: ")
    palabra1 = input("Palabra a reemplazar: ")
    palabra2 = input("Nueva palabra: ")
    with open(ruta_base + archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    nuevo_texto = texto.replace(palabra1, palabra2)
    with open(ruta_base + archivo, "w", encoding="utf-8") as f:
        f.write(nuevo_texto)
    print("Reemplazo hecho.")

def histograma_vocales():
    archivo = input("Nombre del archivo .txt: ")
    with open(ruta_base + archivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    vocales = ["a", "e", "i", "o", "u"]
    conteo = []
    for v in vocales:
        conteo.append(texto.count(v))
    plt.bar(vocales, conteo, color="purple")
    plt.title("Veces que se repiten las vocales")
    plt.show()

def mostrar_csv():
    archivo = input("Nombre del archivo .csv: ")
    with open(ruta_base + archivo, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        for i, fila in enumerate(lector):
            print(fila)
            if i == 14:
                break

def calcular_estadisticas():
    archivo = input("Nombre del archivo .csv: ")
    columna = input("Nombre de la columna: ")
    with open(ruta_base + archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = []
        for fila in lector:
            valor = fila[columna]
            try:
                numero = float(valor)
                datos.append(numero)
            except:
                pass
    if len(datos) == 0:
        print("No se encontraron datos numéricos en esa columna.")
        return
    calculo = len(datos)
    promedio = sum(datos) / calculo
    minimo = min(datos)
    maximo = max(datos)
    print("Cantidad:", calculo)
    print("Promedio:", promedio)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)

def graficar_columna():
    archivo = input("Nombre del archivo .csv: ")
    columna = input("Nombre de la columna: ")
    with open(ruta_base + archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = []
        for fila in lector:
            valor = fila[columna]
            try:
                numero = float(valor)
                datos.append(numero)
            except:
                pass
    if len(datos) == 0:
        print("No se encontraron datos numéricos en esa columna.")
        return
    plt.scatter(range(len(datos)), datos, color="orange")
    plt.title("Gráfico de dispersión")
    plt.xlabel("Índice")
    plt.ylabel(columna)
    plt.show()
    datos_ordenados = sorted(datos)
    plt.bar(range(len(datos_ordenados)), datos_ordenados, color="red")
    plt.title("Gráfico de barras")
    plt.xlabel("Índice")
    plt.ylabel(columna)
    plt.show()

def menu_txt():
    while True:
        print("\n1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            contar_palabras_caracteres()
        elif opcion == "2":
            reemplazar_palabra()
        elif opcion == "3":
            histograma_vocales()
        elif opcion == "4":
            break

def menu_csv():
    while True:
        print("\n1. Mostrar primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            mostrar_csv()
        elif opcion == "2":
            calcular_estadisticas()
        elif opcion == "3":
            graficar_columna()
        elif opcion == "4":
            break

def main():
    while True:
        print("\n Menú Principal ")
        print("1. Listar archivos")
        print("2. Procesar archivo .txt")
        print("3. Procesar archivo .csv")
        print("4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            break

main()