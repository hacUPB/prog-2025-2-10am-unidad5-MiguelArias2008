import csv
ubicacion = ("C:\\Users\\Usuario\\Desktop\\Archivos")
with open('C:\\Users\\Usuario\\Desktop\\Archivos\\example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([
        ['Name', 'Age', 'City'],
        ['John', 25, 'New York'],
        ['Jane', 30, 'Los Angeles'],
        ['Bob', 35, 'Chicago']
    ])