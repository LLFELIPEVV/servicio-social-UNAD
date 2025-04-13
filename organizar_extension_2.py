import os
import shutil


def organizar_archivos(ruta):
    # Verifica que la ruta exista
    if not os.path.isdir(ruta):
        print(f"La ruta '{ruta}' no existe o no es un directorio")
        return

    print(f"Organizando archivos en: {ruta}")

    # Define las categorías y sus extensiones
    categorias = {
        "Imagenes": [".JPG", ".JPEG", ".PNG", ".GIF", ".BMP", ".TIFF", ".WEBP", ".SVG"],
        "Documentos": [
            ".PDF",
            ".DOC",
            ".DOCX",
            ".TXT",
            ".RTF",
            ".ODT",
            ".XLS",
            ".XLSX",
            ".PPT",
            ".PPTX",
        ],
        "Videos": [".MP4", ".AVI", ".MOV", ".WMV", ".MKV", ".FLV", ".WEBM", ".3GP"],
        "Audio": [".MP3", ".WAV", ".FLAC", ".AAC", ".OGG", ".M4A", ".WMA"],
        "Comprimidos": [".ZIP", ".RAR", ".7Z", ".TAR", ".GZ", ".BZ2"],
        "Codigo": [
            ".PY",
            ".JAVA",
            ".JS",
            ".HTML",
            ".CSS",
            ".CPP",
            ".C",
            ".PHP",
            ".R",
            ".GO",
            ".SWIFT",
        ],
    }

    archivos_movidos = 0

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_completa):
            # Obtiene la extensión en mayúsculas
            _, ext = os.path.splitext(archivo)
            ext = ext.upper()

            # Asigna la categoría según la extensión (si no coincide, es 'Otros')
            categoria_asignada = "Otros"
            for categoria, extensiones in categorias.items():
                if ext in extensiones:
                    categoria_asignada = categoria
                    break

            # Crea la carpeta destino si no existe
            carpeta_destino = os.path.join(ruta, categoria_asignada)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
                print(f"Creada carpeta: {categoria_asignada}")

            # Define la ruta destino y maneja nombres duplicados
            ruta_destino = os.path.join(carpeta_destino, archivo)
            contador = 1
            nombre_base, extension = os.path.splitext(archivo)
            while os.path.exists(ruta_destino):
                nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
                contador += 1

            try:
                shutil.move(ruta_completa, ruta_destino)
                archivos_movidos += 1
            except Exception as e:
                print(f"Error al mover '{archivo}': {e}")

    print(f"\nTotal de archivos movidos: {archivos_movidos}")
    print("¡Archivos organizados!")


# Ejemplo de uso:
if __name__ == "__main__":
    ruta_de_prueba = r"C:\Users\FELIPE\Documents\TAREAS UNAD\4° Semestre 2025\PRESTACION DEL SERVICIO SOCIAL\prueba"
    organizar_archivos(ruta_de_prueba)
