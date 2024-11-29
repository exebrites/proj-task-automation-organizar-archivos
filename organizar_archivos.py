#Crear un script que organice tus archivos descargados 
# en carpetas según tipo (PDFs, imágenes, etc.).

# 1. entrar en la carpeta

# 2. recorrer la lista de archivos de la carpeta

# 3. crear una carperta por cada tipo de ext que haya
# 3.1 crear un carpeta pdf 
# 4. verificar la extension del file y mover el file a la carpeta adecuada

import os
import shutil

print('Ejecutando script...')


# Pedir al usuario que seleccione una carpeta desde un menú
print("Seleccione una carpeta para organizar:")
print("1. Descargas")
print("2. Documentos")
print("3. Imágenes")
print("4. Otra carpeta")

opcion = input("Ingrese el número de la opción: ")

if opcion == "1":
    ruta_carpeta = "/home/"+os.environ['USER']+"/Descargas"
elif opcion == "2":
    ruta_carpeta = "/home/"+os.environ['USER']+"/Documentos"
elif opcion == "3":
    ruta_carpeta = "/home/"+os.environ['USER']+"/Imágenes"
elif opcion == "4":
    ruta_carpeta = input("Ingrese la ruta de la carpeta: ")
else:
    print("Opción inválida. Por favor, ingrese un número válido.")
    exit()

# Verificar si la carpeta existe
if not os.path.exists(ruta_carpeta):
    print("La carpeta no existe. Por favor, ingrese una ruta válida.")
    exit()

# Pedir al usuario que ingrese el nombre de la carpeta de PDF
nombre_carpeta_pdf = input("Ingrese el nombre de la carpeta donde quiere guardar los archivos: ")

#mover a ruta actual y listar archivos
os.chdir(ruta_carpeta)
lista_archivos = os.listdir()

#carperta de pdfs verificar la existencia
existe_dir = os.path.exists(nombre_carpeta_pdf)
if not existe_dir: 
        print('Creando carperta y subcarpetas...')
        # 1. creo directorio
        os.mkdir(nombre_carpeta_pdf)
        # 2. me muevo dentro del directorio creado
        directorio_actual = os.getcwd()
        # print(directorio_actual)
        directorio_hijo = os.path.join(directorio_actual, nombre_carpeta_pdf)
        # print(directorio_hijo)
        os.chdir(directorio_hijo)
        # 3. creo la sub carperta pdf y img
        os.mkdir('pdf')
        os.mkdir('img')
        # 4. me muevo un directorio atras
        os.chdir(ruta_carpeta)
long = len(lista_archivos)
print('Recorriendo archivos...')
for i in range(long):
    nombre_ext = os.path.splitext(lista_archivos[i])
   
    #verificar extension y mover archivo
    print('Moviendo archivos...')
    if nombre_ext[1] == '.pdf':
            shutil.move(lista_archivos[i],nombre_carpeta_pdf+'/pdf/'+lista_archivos[i])
    elif nombre_ext[1] == '.jpg':
            shutil.move(lista_archivos[i],nombre_carpeta_pdf+'/img/'+lista_archivos[i])
    elif nombre_ext[1] == '.jpeg':
            shutil.move(lista_archivos[i],nombre_carpeta_pdf+'/img/'+lista_archivos[i])
    elif nombre_ext[1] == '.png':
            shutil.move(lista_archivos[i],nombre_carpeta_pdf+'/img/'+lista_archivos[i])
     
print('Script Finalizado!')
