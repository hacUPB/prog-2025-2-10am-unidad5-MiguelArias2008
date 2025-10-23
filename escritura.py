ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
nombre_archivo = "frutipipa.txt"
modo = "x"
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding = "utf-8")
frase = input("Ingrese una frase: ")
edad = int(input("Por favor ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
fp.write(frase + "\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura))
fp.write("\n")
fp.close()