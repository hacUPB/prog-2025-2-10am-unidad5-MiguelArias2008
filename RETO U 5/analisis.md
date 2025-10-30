
# Análisis del Código - Reto Unidad 5

Este documento explica de forma básica los procedimientos realizados en el código del reto de la Unidad 5.

## Organización del Código

El código está dividido en funciones que permiten trabajar con archivos **.txt** y **.csv** Cada grupo de funciones tiene su propio submenú para facilitar la navegación.

### Funciones para archivos **.txt**
- Contar palabras y caracteres.
- Reemplazar una palabra por otra.
- Graficar la ocurrencia de vocales.

### Funciones para archivos **.csv**
- Mostrar filas del archivo.
- Calcular estadísticas básicas.
- Graficar una columna numérica.

## Estructura del Menú

- Menú principal con opciones para listar archivos, procesar **.txt**, procesar **.csv** y salir.
- Submenú **.txt** con tres opciones.
- Submenú **.csv** con tres opciones.

## Conceptos Utilizados

Se usaron conceptos básicos de programación como:
- Condicionales (**if**, **elif**, **else**)
- Bucles (**while**, **for**)
- Listas
- Manejo de archivos (**open()**)
- Excepciones (**try**, **except**)
- Gráficos (**matplotlib.pyplot**)

## Tabla de Comandos Usados

| Comando              | Función                                                                 |
|---------------------|------------------------------------------------------------------------|
| **open()**            | Abrir archivos para lectura o escritura                                |
| **split()**           | Separar texto en palabras                                               |
| **replace()**         | Reemplazar una palabra por otra en un texto                            |
| **count()**           | Contar ocurrencias de una letra o palabra                              |
| **os.listdir()**      | Listar archivos en una carpeta                                          |
| **csv.reader**        | Leer archivos **.csv** por filas                                          |
| **csv.DictReader**    | Leer archivos **.csv** por columnas con nombre                           |
| **try-except**        | Evitar errores al convertir datos                                      |
| **matplotlib.pyplot** | Crear gráficos de barras y dispersión                                  |
| **input()**           | Recibir datos del usuario                                               |
| **int()** / **float()** | Convertir texto a número                                                |
| **len()**             | Contar elementos en una lista o caracteres en un texto                 |

## Conclusión

El código está diseñado para ser claro y fácil de entender. Utiliza funciones básicas que permiten trabajar con archivos de texto y datos numéricos sin usar herramientas avanzadas.
