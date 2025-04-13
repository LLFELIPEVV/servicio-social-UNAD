import os
import shutil


def organizar_por_tamano(ruta):
    if not os.path.isdir(ruta):
        print(f"La ruta '{ruta}' no existe o no es un directorio")
        return

    # Definir umbrales en bytes (ajusta según tus necesidades)
    umbral_pequeno = 1 * 1024 * 1024  # Menos de 1 MB
    umbral_mediano = 10 * 1024 * 1024  # Entre 1 MB y 10 MB

    categorias = {
        "Pequeños": lambda tam: tam < umbral_pequeno,
        "Medianos": lambda tam: umbral_pequeno <= tam < umbral_mediano,
        "Grandes": lambda tam: tam >= umbral_mediano,
    }

    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            tamano = os.path.getsize(ruta_archivo)
            categoria_asignada = None
            for categoria, condicion in categorias.items():
                if condicion(tamano):
                    categoria_asignada = categoria
                    break

            destino = os.path.join(ruta, categoria_asignada)
            if not os.path.exists(destino):
                os.makedirs(destino)
                print(f"Creada carpeta: {categoria_asignada}")

            shutil.move(ruta_archivo, os.path.join(destino, archivo))

    print("Archivos organizados por tamaño.")


# Ejemplo de uso:
if __name__ == "__main__":
    ruta_de_prueba = r"C:\Users\FELIPE\Documents\TAREAS UNAD\4° Semestre 2025\PRESTACION DEL SERVICIO SOCIAL\prueba"
    organizar_por_tamano(ruta_de_prueba)
