import argparse
import os
import soundfile as sf

def convert_aiff_to_wav(input_file):
    # Comprobar si el archivo de entrada existe
    if not os.path.exists(input_file):
        print("El archivo de entrada no existe.")
        return

    # Determinar el nombre y la extensión del archivo de entrada
    file_name, file_extension = os.path.splitext(input_file)

    # Comprobar si el archivo es un archivo AIFF
    if file_extension.lower() != ".aif":
        print("El archivo de entrada no es un archivo AIFF.")
        return

    # Nombre del archivo de salida (sustituir la extensión por .wav)
    output_file = file_name + ".wav"

    # Leer el archivo AIFF y escribir el archivo WAV
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate, format='WAV', subtype='PCM_16')
    print(f"Se ha convertido {input_file} a {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte un archivo AIFF a WAV.")
    parser.add_argument("-f", "--file", required=True, help="Ruta al archivo AIFF a convertir")
    args = parser.parse_args()

    convert_aiff_to_wav(args.file)