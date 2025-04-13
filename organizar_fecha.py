import os
import shutil
import datetime


def organizar_por_fecha(ruta):
    if not os.path.isdir(ruta):
        print(f"La ruta '{ruta}' no existe o no es un directorio")
        return

    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            # Obtener la fecha de la última modificación y formatearla (por ejemplo, "2025-04")
            fecha_mod = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
            carpeta_fecha = fecha_mod.strftime("%Y-%m")

            # Crear la carpeta si no existe
            destino = os.path.join(ruta, carpeta_fecha)
            if not os.path.exists(destino):
                os.makedirs(destino)
                print(f"Creada carpeta: {carpeta_fecha}")

            # Mover el archivo
            shutil.move(ruta_archivo, os.path.join(destino, archivo))

    print("Archivos organizados por fecha exitosamente.")


# Ejemplo de uso:
if __name__ == "__main__":
    ruta_de_prueba = r"C:\Users\FELIPE\Documents\TAREAS UNAD\4° Semestre 2025\PRESTACION DEL SERVICIO SOCIAL\prueba"
    organizar_por_fecha(ruta_de_prueba)
