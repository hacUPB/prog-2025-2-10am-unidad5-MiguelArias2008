#!/usr/bin/env python3
"""
CLI de análisis y graficación de datos
Archivo: cli_data_tool.py
Descripción: Herramienta de línea de comandos para procesar archivos .txt y .csv según el Reto Unidad 5.
Requisitos: Python 3.8+, matplotlib

Cómo usar:
    python cli_data_tool.py

El archivo también incluye al final una variable llamada ANALISIS_MD con el contenido del documento docs/analisis.md

Nota: Evité el uso de list comprehensions y librerías no vistas en clase.
"""
import os
import sys
import csv
import statistics
import matplotlib.pyplot as plt
open ( C:\Users\Usuario\Desktop\archivop)
# ---------------------- Funciones auxiliares ----------------------

def listar_archivos(ruta):
    """Lista archivos en la ruta indicada (o en la actual si ruta es cadena vacía)."""
    if ruta == "":
        ruta = os.getcwd()
    try:
        archivos = os.listdir(ruta)
    except Exception as e:
        print("Error al listar archivos:", e)
        return []
    # Solo retornamos nombres (sin filtros) para que el usuario vea exactamente lo que hay
    return archivos

# ---------------------- Funciones para .txt ----------------------

def contar_palabras_caracteres(ruta_archivo):
    """Cuenta palabras y caracteres (con y sin espacios) en el archivo de texto."""
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return
    texto = f.read()
    f.close()

    # Contar caracteres con espacios
    num_caracteres_con_espacios = 0
    i = 0
    while i < len(texto):
        num_caracteres_con_espacios += 1
        i += 1

    # Contar caracteres sin espacios
    num_caracteres_sin_espacios = 0
    j = 0
    while j < len(texto):
        if texto[j] != ' ' and texto[j] != '\n' and texto[j] != '\t':
            num_caracteres_sin_espacios += 1
        j += 1

    # Contar palabras: separadas por espacios en blanco (simple)
    palabras = []
    palabra_actual = ''
    k = 0
    while k < len(texto):
        ch = texto[k]
        if ch.isspace():
            if palabra_actual != '':
                palabras.append(palabra_actual)
                palabra_actual = ''
        else:
            palabra_actual = palabra_actual + ch
        k += 1
    if palabra_actual != '':
        palabras.append(palabra_actual)

    num_palabras = 0
    m = 0
    while m < len(palabras):
        num_palabras += 1
        m += 1

    print('Resultado:')
    print('  Palabras:', num_palabras)
    print('  Caracteres (con espacios):', num_caracteres_con_espacios)
    print('  Caracteres (sin espacios):', num_caracteres_sin_espacios)

    return {
        'palabras': num_palabras,
        'caracteres_con_espacios': num_caracteres_con_espacios,
        'caracteres_sin_espacios': num_caracteres_sin_espacios
    }


def reemplazar_palabra(ruta_archivo, buscar, reemplazar, guardar_como=None):
    """Reemplaza todas las ocurrencias exactas de 'buscar' por 'reemplazar'.
    Si guardar_como es None, sobrescribe el archivo original previo respaldo.
    """
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return False
    contenido = f.read()
    f.close()

    # Reemplazo simple (case-sensitive). Para hacerlo insensible a mayúsculas usar lower(), pero
    # eso podría cambiar el caso de las palabras originales; mantenemos case-sensitive por claridad.
    contenido_nuevo = contenido.replace(buscar, reemplazar)

    destino = ruta_archivo
    if guardar_como is not None and guardar_como != '':
        destino = guardar_como
    else:
        # Hacer copia de respaldo
        respaldo = ruta_archivo + '.bak'
        try:
            g = open(respaldo, 'w', encoding='utf-8')
            g.write(contenido)
            g.close()
            print('Creado respaldo:', respaldo)
        except Exception as e:
            print('No se pudo crear respaldo:', e)

    try:
        h = open(destino, 'w', encoding='utf-8')
        h.write(contenido_nuevo)
        h.close()
        print('Archivo guardado en', destino)
        return True
    except Exception as e:
        print('No se pudo guardar el archivo:', e)
        return False


def histograma_vocales(ruta_archivo):
    """Cuenta las vocales en el texto y muestra un histograma con matplotlib."""
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return
    texto = f.read()
    f.close()

    # Inicializar conteo
    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    idx = 0
    while idx < len(texto):
        ch = texto[idx].lower()
        if ch == 'a' or ch == 'á':
            vocales['a'] += 1
        elif ch == 'e' or ch == 'é':
            vocales['e'] += 1
        elif ch == 'i' or ch == 'í':
            vocales['i'] += 1
        elif ch == 'o' or ch == 'ó':
            vocales['o'] += 1
        elif ch == 'u' or ch == 'ú':
            vocales['u'] += 1
        idx += 1

    # Mostrar datos en consola
    print('Ocurrencias de vocales:')
    for v in ['a','e','i','o','u']:
        print(' ', v, ':', vocales[v])

    # Graficar
    etiquetas = ['a','e','i','o','u']
    valores = []
    t = 0
    while t < len(etiquetas):
        valores.append(vocales[etiquetas[t]])
        t += 1

    plt.figure()
    plt.bar(etiquetas, valores)
    plt.title('Histograma de vocales')
    plt.xlabel('Vocal')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

# ---------------------- Funciones para .csv ----------------------

def mostrar_primeras_filas(ruta_archivo, n=15):
    """Muestra las primeras n filas del archivo CSV.
    No usa pandas; lee con csv.reader.
    """
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return
    reader = csv.reader(f)

    contador = 0
    for fila in reader:
        print(fila)
        contador += 1
        if contador >= n:
            break
    f.close()


def calcular_estadisticas_columna(ruta_archivo, nombre_columna):
    """Calcula estadísticas básicas de una columna indicada por nombre de encabezado.
    Retorna un diccionario con conteo, promedio, mediana, desviacion, max, min.
    Solo considera valores numéricos; ignora entradas vacías o no-numéricas.
    """
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return None
    reader = csv.reader(f)

    # Leer encabezados
    try:
        encabezados = next(reader)
    except StopIteration:
        print('CSV vacío')
        f.close()
        return None

    # Buscar índice de la columna
    indice = -1
    i = 0
    while i < len(encabezados):
        if encabezados[i].strip() == nombre_columna.strip():
            indice = i
            break
        i += 1

    if indice == -1:
        print('No se encontró la columna', nombre_columna)
        f.close()
        return None

    valores = []
    for fila in reader:
        # Proteger filas más cortas
        if indice < len(fila):
            celda = fila[indice].strip()
            if celda != '':
                try:
                    val = float(celda)
                    valores.append(val)
                except Exception:
                    # Ignorar valores no numéricos
                    pass
    f.close()

    if len(valores) == 0:
        print('No se encontraron valores numéricos en la columna', nombre_columna)
        return None

    # Calcular estadísticas usando statistics
    try:
        conteo = len(valores)
        promedio = statistics.mean(valores)
        mediana = statistics.median(valores)
        desviacion = 0.0
        if conteo > 1:
            desviacion = statistics.pstdev(valores)  # desviación poblacional
        maxima = max(valores)
        minima = min(valores)
    except Exception as e:
        print('Error al calcular estadísticas:', e)
        return None

    resultado = {
        'conteo': conteo,
        'promedio': promedio,
        'mediana': mediana,
        'desviacion': desviacion,
        'maximo': maxima,
        'minimo': minima
    }
    return resultado


def graficar_columna_scatter(ruta_archivo, nombre_columna, color_codigo='#1f77b4'):
    """Grafica una columna numérica como scatter. El eje x será el índice (orden de fila leída).
    color_codigo es una cadena aceptada por matplotlib. Devuelve True si lo grafica.
    """
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return False
    reader = csv.reader(f)
    try:
        encabezados = next(reader)
    except StopIteration:
        print('CSV vacío')
        f.close()
        return False

    indice = -1
    i = 0
    while i < len(encabezados):
        if encabezados[i].strip() == nombre_columna.strip():
            indice = i
            break
        i += 1

    if indice == -1:
        print('No se encontró la columna', nombre_columna)
        f.close()
        return False

    valores = []
    for fila in reader:
        if indice < len(fila):
            celda = fila[indice].strip()
            if celda != '':
                try:
                    val = float(celda)
                    valores.append(val)
                except Exception:
                    pass
    f.close()

    if len(valores) == 0:
        print('No hay datos numéricos para graficar')
        return False

    # Eje x: 0..n-1
    xs = []
    j = 0
    while j < len(valores):
        xs.append(j)
        j += 1

    plt.figure()
    plt.scatter(xs, valores, c=color_codigo)
    plt.title('Gráfico de dispersión - ' + nombre_columna)
    plt.xlabel('Índice de fila')
    plt.ylabel(nombre_columna)
    plt.grid(True)
    plt.show()
    return True


def graficar_barras_reordenado(ruta_archivo, nombre_columna_x, nombre_columna_y):
    """Ejemplo de reorganización de datos: toma dos columnas (x categórica, y numérica),
    suma valores por categoría y grafica barras. Retorna True si lo grafica.
    """
    try:
        f = open(ruta_archivo, 'r', encoding='utf-8')
    except Exception as e:
        print('No se pudo abrir el archivo:', e)
        return False

    reader = csv.reader(f)
    try:
        encabezados = next(reader)
    except StopIteration:
        print('CSV vacío')
        f.close()
        return False

    idx_x = -1
    idx_y = -1
    k = 0
    while k < len(encabezados):
        if encabezados[k].strip() == nombre_columna_x.strip():
            idx_x = k
        if encabezados[k].strip() == nombre_columna_y.strip():
            idx_y = k
        k += 1

    if idx_x == -1 or idx_y == -1:
        print('No se encontraron las columnas indicadas')
        f.close()
        return False

    # Crear diccionario que sume valores por categoría
    suma_por_categoria = {}
    for fila in reader:
        if idx_x < len(fila) and idx_y < len(fila):
            cat = fila[idx_x].strip()
            val_celda = fila[idx_y].strip()
            if cat != '' and val_celda != '':
                try:
                    val = float(val_celda)
                except Exception:
                    continue
                if cat in suma_por_categoria:
                    suma_por_categoria[cat] = suma_por_categoria[cat] + val
                else:
                    suma_por_categoria[cat] = val
    f.close()

    if len(suma_por_categoria) == 0:
        print('No se encontraron pares válidos para graficar')
        return False

    categorias = []
    valores = []
    for llave in suma_por_categoria:
        categorias.append(llave)
        valores.append(suma_por_categoria[llave])

    plt.figure()
    plt.bar(categorias, valores)
    plt.title('Suma por categoría (' + nombre_columna_x + ')')
    plt.xlabel(nombre_columna_x)
    plt.ylabel('Suma de ' + nombre_columna_y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return True

# ---------------------- Menús ----------------------

def submenu_txt():
    while True:
        print('\nSubmenú - Archivos .txt')
        print('1. Contar número de palabras y caracteres')
        print('2. Reemplazar una palabra por otra')
        print('3. Histograma de ocurrencia de las vocales')
        print('4. Volver al menú principal')
        opcion = input('Elija una opción: ').strip()
        if opcion == '1':
            ruta = input('Ruta al archivo .txt: ').strip()
            contar_palabras_caracteres(ruta)
        elif opcion == '2':
            ruta = input('Ruta al archivo .txt: ').strip()
            buscar = input('Palabra a buscar (case-sensitive): ')
            reemplazar = input('Palabra reemplazo: ')
            guardar = input('Guardar como (dejar vacío para sobrescribir con respaldo): ').strip()
            if guardar == '':
                guardar = None
            reemplazar_palabra(ruta, buscar, reemplazar, guardar)
        elif opcion == '3':
            ruta = input('Ruta al archivo .txt: ').strip()
            histograma_vocales(ruta)
        elif opcion == '4':
            break
        else:
            print('Opción no válida')


def submenu_csv():
    while True:
        print('\nSubmenú - Archivos .csv')
        print('1. Mostrar las 15 primeras filas')
        print('2. Calcular estadísticas de una columna')
        print('3. Graficar columna (dispersión)')
        print('4. Reorganizar y graficar (barras por categoría)')
        print('5. Volver al menú principal')
        opcion = input('Elija una opción: ').strip()
        if opcion == '1':
            ruta = input('Ruta al archivo .csv: ').strip()
            mostrar_primeras_filas(ruta, 15)
        elif opcion == '2':
            ruta = input('Ruta al archivo .csv: ').strip()
            col = input('Nombre exacto de la columna (encabezado): ')
            res = calcular_estadisticas_columna(ruta, col)
            if res is not None:
                print('Estadísticas para', col)
                for llave in res:
                    print(' ', llave, ':', res[llave])
        elif opcion == '3':
            ruta = input('Ruta al archivo .csv: ').strip()
            col = input('Nombre exacto de la columna (encabezado): ')
            color = input('Código de color Matplotlib (ej: "red" o "#FF5733") o dejar vacío para defecto: ').strip()
            if color == '':
                color = '#1f77b4'
            graficar_columna_scatter(ruta, col, color)
        elif opcion == '4':
            ruta = input('Ruta al archivo .csv: ').strip()
            colx = input('Nombre de la columna categórica (ej: ciudad): ')
            coly = input('Nombre de la columna numérica a sumar (ej: consumo): ')
            graficar_barras_reordenado(ruta, colx, coly)
        elif opcion == '5':
            break
        else:
            print('Opción no válida')


def main():
    print('Herramienta CLI de análisis y graficación de datos - Unidad 5')
    while True:
        print('\nMenú Principal')
        print('1. Listar archivos en ruta actual o especificada')
        print('2. Procesar archivo de texto (.txt)')
        print('3. Procesar archivo separado por comas (.csv)')
        print('4. Salir')
        opcion = input('Escoja una opción: ').strip()
        if opcion == '1':
            ruta = input('Ingrese ruta (dejar vacío para la ruta actual): ').strip()
            archivos = listar_archivos(ruta)
            if archivos is None:
                print('No se pudieron listar archivos')
            else:
                print('Archivos encontrados:')
                p = 0
                while p < len(archivos):
                    print(' ', archivos[p])
                    p += 1
        elif opcion == '2':
            submenu_txt()
        elif opcion == '3':
            submenu_csv()
        elif opcion == '4':
            print('Saliendo...')
            break
        else:
            print('Opción no válida')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrumpido por usuario. Saliendo...')


# ---------------------- Documento de análisis (docs/analisis.md) ----------------------
ANALISIS_MD = r"""
# docs/analisis.md

## 1. Organización del código

El proyecto contiene un único archivo `cli_data_tool.py` que implementa:

- Funciones auxiliares para manejo de archivos y listados (`listar_archivos`).
- Subconjunto de funciones para manejo de archivos de texto (`contar_palabras_caracteres`, `reemplazar_palabra`, `histograma_vocales`).
- Subconjunto de funciones para manejo de archivos CSV (`mostrar_primeras_filas`, `calcular_estadisticas_columna`, `graficar_columna_scatter`, `graficar_barras_reordenado`).
- Menús interactivos (`submenu_txt`, `submenu_csv`, `main`) que controlan el flujo de la aplicación.

El código prioriza claridad y explica cada bloque con comentarios. Se evitó el uso de herramientas avanzadas no vistas en clase (por ejemplo, no se usaron list comprehensions ni pandas).

## 2. Uso de condicionales, bucles y listas

- Condicionales: `if/elif/else` se usan para navegación en los menús y validaciones de errores.
- Bucles: `while` y `for` se utilizan para recorrer cadenas, listas y leer líneas de archivos. Los `while` se usaron ampliamente para cumplir la restricción de no usar list comprehensions.
- Listas: Se usan listas para almacenar palabras, encabezados y valores numéricos leídos desde CSV.

## 3. Manejo de cadenas y archivos

- Para archivos de texto se usan métodos como `str.isspace()`, `str.lower()`, `str.strip()` y concatenación de caracteres para construir palabras.
- Para reemplazos se usa `str.replace()` y se crea un respaldo del archivo original antes de sobrescribirlo.

## 4. Manejo de archivos CSV

- Se usa el módulo estándar `csv` para leer archivos separados por comas.
- El programa busca la columna indicada por el nombre del encabezado (comparación `strip()` exacta) y convierte cada celda a `float` usando `try/except` para filtrar valores no numéricos.

## 5. Estadísticas y gráficos

- Estadísticas básicas (conteo, promedio, mediana, desviación poblacional, máximo y mínimo) se calculan con el módulo `statistics`.
- Las visualizaciones se realizan con `matplotlib.pyplot`. Hay un histograma de vocales, un scatter plot para columnas numéricas y un gráfico de barras que suma valores por categoría (reorganización de datos).

## 6. Limitaciones y posibles mejoras

- Actualmente el reemplazo de palabras es case-sensitive y no distingue palabras por límites morfológicos (e.g., reemplazar "la" cambiará "lago" si se busca con imprecisión). Se puede mejorar usando expresiones regulares `re` si está permitido.
- La lectura de CSV es simple y no usa dialectos personalizados; si el CSV tiene separadores diferentes o comillas complejas, podría fallar.
- Para grandes archivos (millones de filas) habría que usar streaming y procesamiento por bloques.

## 7. Recomendaciones para la sustentación (video 5-8 min)

- Inicio (30s): Presentar objetivo y estructura del programa.
- Código (4-5 min): Mostrar las funciones principales: conteo en .txt, reemplazo, histograma de vocales; luego mostrar cálculo de estadísticas y gráficas en .csv.
- Demostración (1.5-2.5 min): Ejecutar la herramienta en consola y probar 2-3 opciones rápidas.
- Conclusión (30s): Resumen de limitaciones y mejoras futuras.

"""
