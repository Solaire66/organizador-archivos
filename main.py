import os
import shutil
import datetime


def organizar_archivos(carpeta_descargas):
        """
        Organiza los archivos de la carpeta de descargas en subcarpetas basadas en el tipo de archivo.
        Args:
            carpeta_descargas (str): La ruta a la carpeta de descargas.
        """

    # Define un diccionario que mapea extensiones de archivo a nombres de carpetas
    # Esto hace que sea mas fail extender y mantener
        tipos_de_archivo = {
            "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
            "documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
            "videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
            "audio": [".mp3", ".wav", ".ogg", ".flac"],
            "programas": [".exe", ".msi"],
            "comprimidos": [".zip", ".rar", ".tar", ".gz", ".bz2"],
            "otros": []  # Para archivos sin una categoría clara
        }
        # Crea las carpetas destino si no existen.
        for carpeta in tipos_de_archivo:
            ruta_carpeta = os.path.join(carpeta_descargas, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f"Carpeta creada: {ruta_carpeta}")

            # Recorre todos los archivos en la carpeta de descargas.
            for nombre_archivo in os.listdir(carpeta_descargas):
                ruta_archivo = os.path.join(carpeta_descargas, nombre_archivo)

            # Verifica si es un archivo (no una carpeta)
            if os.path.isfile(ruta_archivo):
                #Obtiene el nombre base y la extension delk archivo.
                nombre_base, extension = os.path.splitext(nombre_archivo)
                extension = extension.lower() # convierte la extension a minuscula


            #Encuentra la carpeta destino basada en la extension del archivo
            carpeta_destino = "otros" # valor por defecto
            for carpeta, extensiones in tipos_de_archivo.items():
                if extension in extensiones:
                    carpeta_destino = carpeta
                    break

                ruta_destino = os.path.join(carpeta_descargas,carpeta_destino, nombre_archivo)

                #Mueve el archivo
                try:
                    shutil.move(ruta_archivo,ruta_destino)
                    print(f"Movido: {nombre_archivo} a {ruta_destino}")
                except Exception as e:
                    print(f"Error al mover {nombre_archivo}: {e}")

def organizar_por_fecha(carpeta_descargas):
    """
    Organiza los archivos de la carpeta de descargas en subcarpetas basadas en la fecha de creación.
    Crea carpetas por año y mes (ej., 2024/01, 2024/02, etc.)
    Args:
        carpeta_descargas (str): La ruta a la carpeta de descargas.
    """
    for nombre_archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            try:
                # Obtiene la fechga de la creacion del archivo
                fecha_creacion = datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo))
                año = str(fecha_creacion.year)
                mes = str(fecha_creacion.month)
                carpeta_destino = os.path.join(carpeta_descargas, año)

                # Crea la carpeta destino si no existe
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                    print(f"Carpeta creada: {carpeta_destino}")

                ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
                shutil.move(ruta_archivo, ruta_destino)
                print(f"Movido: {nombre_archivo} a {ruta_destino}")
            except Exception as e:
                print(f"Error al mover {nombre_archivo}: {e}")

def main():
    """
    Función principal que ejecuta la organización de archivos.
    """
    # Pide al ususario la ruta de la carpeta de descarga.
    carpeta_descargas = input("Ingresa la ruta de la carpeta de descargas: ")
    # Se asegura quie la ruta exista
    if not os.path.exists(carpeta_descargas):
        print(f"Error: La carpeta '{carpeta_descargas}' no existe.")
        return

    #Pregunta al usuario como quiere organizar los archivos
    print("¿Cómo quieres organizar los archivos?")
    print("1. Por tipo de archivo")
    print("2. Por fecha de creación")
    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        organizar_archivos(carpeta_descargas)
    elif opcion == "2":
        organizar_por_fecha(carpeta_descargas)
    else:
        print("Opcion Invalida.")

if __name__ == "__main__":
    main()