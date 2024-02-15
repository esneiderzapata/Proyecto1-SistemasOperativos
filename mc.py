import argparse
import os
from pydub import AudioSegment
from io import BytesIO

def convertir_a_mp3(audio_cd):
    output = BytesIO()
    audio_cd.export(output, format="mp3")
    return output.getvalue()

def convertir_a_ogg(audio_cd):
    output = BytesIO()
    audio_cd.export(output, format="ogg")
    return output.getvalue()

def convertir_a_flac(audio_cd):
    output = BytesIO()
    audio_cd.export(output, format="flac")
    return output.getvalue()

def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "wb") as f:
        f.write(contenido)
    print(f"Archivo guardado como {nombre_archivo}")

def main():
    # Cargar el archivo de audio CD-A
    #audio_cd = AudioSegment.from_file("08 Taken.aif", format="aiff")

    # Crear y configurar Parser para obtener argumentos
    parser = argparse.ArgumentParser(description="---")
    parser.add_argument("-f", "--file", required=True, help="Ruta al archivo AIFF a convertir o a la carpeta")
    args = parser.parse_args()

    #Comprobar si file es una carpeta o un archivo .aif
    if os.path.isdir(args.file):
        print("es una carpeta")
        return

    #Si es un archivo .aif cargarlo
    audio_cd = AudioSegment.from_file(args.file, format="aiff")

    # Convertir a MP3, AAC y FLAC
    mp3_content = convertir_a_mp3(audio_cd)
    ogg_content = convertir_a_ogg(audio_cd)
    flac_content = convertir_a_flac(audio_cd)

    # Calcular Pesos de cada archivo
    sizeMP3 = len(mp3_content)/1024/1024
    sizeOGG = len(ogg_content)/1024/1024
    sizeFLAC = len(flac_content)/1024/1024

    # Mostrar opciones al usuario
    print("\nOpciones disponibles:")
    print(f"1. MP3 (Tamaño Estimado: {sizeMP3:.2f}MB)")
    print(f"2. OGG (Tamaño Estimado: {sizeOGG:.2f}MB)")
    print(f"3. FLAC (Tamaño Estimado: {sizeFLAC:.2f}MB)")

    opcion = input("Elija el formato que desea guardar en disco: ")

    if opcion == "1":
        guardar_archivo("archivo_convertido.mp3", mp3_content)
    elif opcion == "2":
        guardar_archivo("archivo_convertido.ogg", ogg_content)
    elif opcion == "3":
        guardar_archivo("archivo_convertido.flac", flac_content)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

#SE NECESITA INSTALAR PYDUB CON: pip install pydub
#SE NECESITA INSTALAR FFmpeg Y AGREGARLO AL PATH
#PRIMER ERROR: NO FUNCIONA LA CONVERSIÓN A M4A (ACC) SOLUCIÓN USAR FORMAT="adts"
#MP3 AL SER EL FORMATO MÁS POPULAR Y COMPATIBLE DE AUDIO
#OGG AL SER EL FORMATO CON MENOR PESO
#FLAC AL SER EL FORMATO QUE ES UNA REPLICA EXACTA DEL AUDIO