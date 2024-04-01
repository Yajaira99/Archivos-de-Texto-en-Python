# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    #Escribir al menos tres lineas de notas personales
    file.write("arroz.\n")
    file.write("sal.\n")
    file.write("aceite.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    #Leer el contenido del archivo linea por linea
    line = file.readline()
    while line:
        #Mostrar en la consola cada linea leida
        print(line.strip()) # strip() elimina los saltos de línea al final
        line = file.readline()