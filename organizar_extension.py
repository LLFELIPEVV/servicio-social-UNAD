import os
import shutil


def organizar_archivos(ruta):
    # Verifica si la carpeta existe
    if not os.path.isdir(ruta):
        print("La ruta especificada no existe")
        return
    else:
        print("La ruta especificada existe")
        print(os.listdir(ruta))

    # Recorre todos los archivos en la carpeta
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        # Procesa solo si es un archivo
        if os.path.isfile(ruta_completa):
            # Extraer la extensión del archivo y convertirla a mayúsculas
            ext = archivo.split(".")[-1].upper()
            carpeta_destino = os.path.join(ruta, ext)

            # Crea la carpeta de destino si no existe
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Mueve el archivo a la carpeta correspondiente
            shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))

    print("Archivos organizados por extensión.")


# Ejemplo de uso:
ruta_de_prueba = r"C:\Users\FELIPE\Documents\TAREAS UNAD\4° Semestre 2025\PRESTACION DEL SERVICIO SOCIAL\prueba"
organizar_archivos(ruta_de_prueba)
