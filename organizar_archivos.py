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
nombre_dir ='PDF'
os.chdir('/home/exe/Descargas')
# print(os.getcwd())
# print(os.system("ls"))

lista_archivos = os.listdir()
#carperta de pdfs verificar la existencia
existe_dir = os.path.exists(nombre_dir)
if not existe_dir: 
        print('Creando carperta pdf')
        os.mkdir(nombre_dir) 

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