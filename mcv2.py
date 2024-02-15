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

def obtener_tamaño_estimado(audio_cd, formato):
    # Exportar el audio en el formato especificado y calcular el tamaño
    output = BytesIO()
    audio_cd.export(output, format=formato)
    size_bytes = len(output.getvalue())
    size_kb = size_bytes / 1024  # Convertir bytes a kilobytes
    size_mb = size_kb / 1024
    return size_mb

def main():
    # Cargar el archivo de audio CD-A
    audio_cd = AudioSegment.from_file("musictest.cdda", format="cdda")

    # Calcular el tamaño estimado para cada formato de audio
    tamaño_mp3 = obtener_tamaño_estimado(audio_cd, "mp3")
    tamaño_aac = obtener_tamaño_estimado(audio_cd, "ogg")
    tamaño_flac = obtener_tamaño_estimado(audio_cd, "flac")

    # Mostrar opciones disponibles al usuario con los tamaños estimados
    print("Opciones disponibles:")
    print(f"1. MP3 (Tamaño estimado: {tamaño_mp3:.2f} MB)")
    print(f"2. AAC (Tamaño estimado: {tamaño_aac:.2f} MB)")
    print(f"3. FLAC (Tamaño estimado: {tamaño_flac:.2f} MB)")

    opcion = input("Elija el formato que desea guardar en disco: ")

    if opcion == "1":
        guardar_archivo("archivo_convertido.mp3", convertir_a_mp3(audio_cd))
    elif opcion == "2":
        guardar_archivo("archivo_convertido.ogg", convertir_a_ogg(audio_cd))
    elif opcion == "3":
        guardar_archivo("archivo_convertido.flac", convertir_a_flac(audio_cd))
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