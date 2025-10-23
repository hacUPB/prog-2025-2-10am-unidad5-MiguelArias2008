lista = ["Daga adicta",  "Calor",  "Yogurcito remix",  "Bebe lean",  "Besos en la boca" ]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "w"
nombre_archivo = "canciones.txt"
fp = open(ubicacion +"\\" + nombre_archivo, modo)
#p.writelines(lista)
for cancion in lista:
    fp.write(cancion+"\n")
fp.close()