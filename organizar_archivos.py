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

# Pedir al usuario que ingrese la ruta de la carpeta a organizar
ruta_carpeta = input("Ingrese la ruta de la carpeta que quiere organizar: ")

# Verificar si la carpeta existe
if not os.path.exists(ruta_carpeta):
    print("La carpeta no existe. Por favor, ingrese una ruta válida.")
    exit()

# Pedir al usuario que ingrese el nombre de la carpeta de PDF
nombre_carpeta_pdf = input("Ingrese el nombre de la carpeta donde quiere guardar los archivos PDF: ")


# '/home/exe/Descargas'
os.chdir(ruta_carpeta)
# print(os.getcwd())
# print(os.system("ls"))

lista_archivos = os.listdir()
#carperta de pdfs verificar la existencia
existe_dir = os.path.exists(nombre_carpeta_pdf)
if not existe_dir: 
        print('Creando carperta pdf')
        os.mkdir(nombre_carpeta_pdf) 

long = len(lista_archivos)
# print(long)
print('Recorriendo archivos...')
for i in range(long):
    # print(lista_archivos[i])
  
    nombre_ext = os.path.splitext(lista_archivos[i])
    # print(nombre_ext[1])
    #verificar extension
    if nombre_ext[1] == '.pdf':
            # print("es un pdf")
            print('Moviendo archivos...')
            shutil.move(lista_archivos[i],'PDF/'+lista_archivos[i])
    #mover archivo a carpeta PDF

print('Script Finalizado!')
