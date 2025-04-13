import os
import shutil


def organizar_por_alfabeticamente(ruta):
    # Verifica que la ruta exista y sea un directorio
    if not os.path.isdir(ruta):
        print(f"La ruta '{ruta}' no existe o no es un directorio")
        return

    print(f"Organizando archivos en: {ruta} por orden alfabético")
    archivos_movidos = 0

    # Recorre todos los elementos de la carpeta
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        # Procesar solo si es un archivo
        if os.path.isfile(ruta_archivo):
            # Toma la primera letra del nombre del archivo; si no es letra, asigna 'Otros'
            if archivo and archivo[0].isalpha():
                primera_letra = archivo[0].upper()
            else:
                primera_letra = "Otros"

            # Define la carpeta destino según la primera letra
            carpeta_destino = os.path.join(ruta, primera_letra)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
                print(f"Creada carpeta: {primera_letra}")

            # Define la ruta de destino y maneja archivos duplicados
            ruta_destino = os.path.join(carpeta_destino, archivo)
            contador = 1
            nombre_base, extension = os.path.splitext(archivo)
            while os.path.exists(ruta_destino):
                nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
                contador += 1

            # Mueve el archivo a la carpeta correspondiente
            try:
                shutil.move(ruta_archivo, ruta_destino)
                archivos_movidos += 1
            except Exception as e:
                print(f"Error al mover '{archivo}': {e}")

    print(f"\nTotal de archivos movidos: {archivos_movidos}")


# Ejemplo de uso:
if __name__ == "__main__":
    ruta_de_prueba = r"C:\Users\FELIPE\Documents\TAREAS UNAD\4° Semestre 2025\PRESTACION DEL SERVICIO SOCIAL\prueba"  # Cambia esta ruta por la de tus archivos
    organizar_por_alfabeticamente(ruta_de_prueba)
